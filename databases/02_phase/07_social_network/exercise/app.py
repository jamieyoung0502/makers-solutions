from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")
