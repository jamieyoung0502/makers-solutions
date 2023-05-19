# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

from urllib.request import urlopen
import json

# == EXERCISES ==


# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
def load_data_from_url(url):
    #  pass a URL and it returns a file-like object that represents the data retrieved from the specified URL
    url = urlopen(url)
    # reads data from the file and returns it as a string or bytes, latter of which we need to convert to string using decode()
    response = url.read().decode('UTF-8')
    # json.loads() takes a String as input, and converts it to a JSON object
    return json.loads(response)


# print(load_data_from_url("https://api.open-meteo.com/v1/forecast?latitude=51.5002&longitude=-0.1262&current_weather=true"))

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Purpose: Load the sample JSON from file, and returns a list of films
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    films = load_data_from_file(filename)
    return [movie['name'] for movie in films if movie['director'] == director]


# Purpose: Load the sample JSON from file, and returns a list of films
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    films = load_data_from_file(filename)
    return [movie['name'] for movie in films if desired_actor in movie['stars']]


# Purpose: Load the sample JSON from file, and returns a list of films
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    films = load_data_from_file(filename)
    return [movie['name'] for movie in films if movie['imdb_rating'] >= rating]


# Purpose: Load the sample JSON from file, and returns a list of films
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    films = load_data_from_file(filename)

    def between_years(release_year):
        return start_year <= release_year <= end_year
        # return release_year >= start_year and release_year <= end_year

    return [movie['name'] for movie in films if between_years(movie['year'])]


# Purpose: Load the sample JSON from file, and returns a list of films
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    films = load_data_from_file(filename)
    return [movie['name'] for movie in sorted(films, key=lambda film: film['year'])]

# sorted: returns a new sorted list
# films: the iterable to be sorted.
# key: optional parameter that specifies a function (or other callable) to be called on each list element prior to making comparisons
# lambda: an anonymous function (i.e., without a name) that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression

# def sorted_movie_names(films):
#     sorted_films = sorted(films, key=lambda film: film['year'])
#     movie_names = []
#     for film in sorted_films:
#         movie_names.append(film['name'])
#     return movie_names


# Purpose: Load the sample JSON from file, and returns a list of films
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    films = load_data_from_file(filename)
    return [movie['name'] for movie in sorted(films, key=lambda film: film['year'], reverse=True)]


# Purpose: Load the sample JSON from file, and returns a deduplicated list
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    films = load_data_from_file(filename)

    actors = []
    for movie in films:
        for actor in movie['stars']:
            actors.append(actor) if actor.lower().startswith(letter) else next

    # one-liner:
    # actors = [actor for movie in films for actor in movie['stars'] if actor.lower().startswith(letter)]

    return sorted(list(set(actors)))
