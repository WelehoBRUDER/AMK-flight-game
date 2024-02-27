import os
import geopy.distance
import mysql.connector
from dotenv import load_dotenv

# Loads .env to current os.environ
load_dotenv()

# Load database credentials from .env
# This is to prevent having to commit sensitive information
# like password and username
db_variables = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE')
}
# Debug to see if .env is working
print(db_variables)

# Connect to SQL-database using the .env variables
db = mysql.connector.connect(**db_variables)
cursor = db.cursor()


def distance_between_airports(port_1, port_2):
    cursor.execute(
        f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{port_1}' OR ident = '{port_2}'")
    airport_data = cursor.fetchmany(2)
    distance = geopy.distance.distance(airport_data[0], airport_data[1])
    return distance
