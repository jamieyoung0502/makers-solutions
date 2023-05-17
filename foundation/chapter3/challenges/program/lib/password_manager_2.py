# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime


class PasswordManager2():
    def __init__(self):
        self.passwords = {}

    def add(self, service, password):
        if self.__check_if_password_is_valid(password) and self.__password_is_unique(password):
            self.passwords[service] = {
                'password': password,
                'added_on': datetime.now()
            }

    def remove(self, service):
        self.passwords.pop(service)

    def update(self, service, password):
        if self.__check_if_password_is_valid(password) and self.__password_is_unique(password):
            self.passwords[service]['password'] = password

    def list_services(self):
        return list(self.passwords.keys())

    def sort_services_by(self, sort_by, reverse=False):
        reverse = (reverse == 'reverse')
        if sort_by != 'added_on':
            return sorted([service for service in self.passwords.keys()], reverse=reverse)
        else:
            return sorted(self.passwords.keys(), key=lambda service: self.passwords[service]['added_on'], reverse=reverse)

    def get_for_service(self, service):
        # refactored: if service not found, an empty dictionary is returned, and then the password key is retrieved from that dictionary.
        # this will return None if either the service key or the password key is not found
        return self.passwords.get(service, {}).get('password')

        # original:
        # service_dict = self.passwords.get(service)
        # return None if service_dict == None else service_dict.get('password')

    def __password_is_unique(self, password):
        return password not in [self.passwords[service]['password']for service in self.passwords]

    def __check_if_password_is_valid(self, password):
        return len(password) > 7 and any(char in '!@$%&' for char in password)
