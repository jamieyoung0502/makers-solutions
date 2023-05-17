import os
# import csv

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==


# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    return os.path.exists(filename)

    # alternative:
    # a try clause is executed up until the point where the first exception is encountered
    # if no exception occurs, the except clause is skipped and execution of the try statement is finished.
    try:
        # `with` ensures that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown
        with open(filename, 'r'):
            return True
    # specify how the program responds to a particular exception
    except FileNotFoundError:
        return False

    # bonus notes!
    # assert is used to test that certain assumptions are true:
    # def add_numbers(x, y):
    #     assert isinstance(x, int) and isinstance(y, int), "x and y must be integers"
    #     return x + y

    # `with` clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed like closing a file
    # `raise` allows you to throw an exception at any time.
    # `finally` enables you to execute sections of code that should always run


# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if does_file_exist(filename):
        # 'r' is for read-only mode
        with open(filename, "r") as file:
            # readlines() returns all lines in the file as a list where each line is an item in the list object
            return file.readlines()
    else:
        return "This file cannot be found!"

        # using csv:
        # the delimiter is used to separate the values in each row into individual columns
        # reader = csv.reader(file, delimiter=';', lineterminator=';;')
        # for row in reader:
        #     print(row)


# print(type(get_file_contents(('AirQuality.csv'))))


# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    if include_header_row:
        headers = [get_file_contents(filename)[0]]
        return headers + [row for row in get_file_contents(filename) if '25/12' in row.split(';')[0]]
    else:
        return [row for row in get_file_contents(filename) if '25/12' in row.split(';')[0]]


# print(get_file_contents(('AirQuality.csv'))[0])
# print(get_file_contents(('AirQuality.csv'))[1].split(';')[0])
# print(christmas_day_air_quality('AirQuality.csv', True))

# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    headers = get_file_contents(filename)[0].split(';')

    christmas_days = [
        dict(zip(headers, row.split(';'))) for row in christmas_day_air_quality(filename, False)
    ]

    total = sum(float(day['PT08.S1(CO)']) for day in christmas_days)

    return round((total / len(christmas_days)), 2)


# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    headers = get_file_contents(filename)[0].split(';')
    monthly_average = {}
    for month in range(1, 13):
        search_month = f'{month:02d}'
        # search_month = str(month) if month > 9 else f'0{month}'

        monthly_data_list = [
            row for row in get_file_contents(filename) if f'/{search_month}/' in row.split(';')[0]
        ]

        monthly_data_dict = [
            dict(zip(headers, row.split(';'))) for row in monthly_data_list
        ]

        day_count = len(monthly_data_list)
        total = sum(float(day['PT08.S1(CO)']) for day in monthly_data_dict)
        average = round((total / day_count), 2)
        monthly_average.update({month: average})

    return monthly_average


# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    # Get the file contents
    file_contents = get_file_contents(filename)

    # Extract the headers
    headers = file_contents[0].split(';')

    # Filter the rows for March data
    march_data = [row for row in file_contents if f'/03/' in row.split(';')[0]]

    # 'x' will only create a new file; 'w' will create and write to if it already exists
    with open('AirQualityMarch.csv', 'w') as file:
        # insert multiple strings at a time
        file.writelines((headers + march_data))


# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    # Create the directory if it doesn't exist
    if not os.path.exists("monthly_responses"):
        os.makedirs("monthly_responses")

    file_contents = get_file_contents(filename)
    headers = file_contents[0].split(';')
    first_row_date = file_contents[1].split(';')[0]
    first_year = int(first_row_date.split('/')[-1])

    for row in reversed(list(file_contents)):
        if row.split(';')[0] == '':
            next
        else:
            last_row_date = row.split(';')[0]
            break

    last_year = int(last_row_date.split('/')[-1])
    year_range = range(first_year, (last_year + 1))

    for year in year_range:
        for month in range(1, 13):

            monthly_data_list = [
                row for row in file_contents if f'/{month:02d}/{year}' in row.split(';')[0]
            ]

            if len(monthly_data_list) > 1:
                # Create the file inside the directory
                with open(os.path.join("monthly_responses", f"{month:02d}-{year}.csv"), 'w') as file:
                    file.writelines(headers + monthly_data_list)
