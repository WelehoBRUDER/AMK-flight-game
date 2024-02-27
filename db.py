import os
import geopy.distance
import mysql.connector
from dotenv import load_dotenv

db = {}


def connect_to_db():
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
    db["database"] = mysql.connector.connect(**db_variables)
    db["cursor"] = db["database"].cursor()


def distance_between_airports(port_1, port_2):
    db["cursor"].execute(
        f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{port_1}' OR ident = '{port_2}'")
    airport_data = db["cursor"].fetchmany(2)
    distance = geopy.distance.distance(airport_data[0], airport_data[1])
    return distance


connect_to_db()
print(distance_between_airports("EFHK", "EFIV"))
