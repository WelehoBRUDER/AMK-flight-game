import os
import geopy.distance
import mysql.connector
import random
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

    # Connect to SQL-database using the .env variables
    db["database"] = mysql.connector.connect(**db_variables)
    db["cursor"] = db["database"].cursor()


def get_some_airports():
    db["cursor"].execute(
        f"SELECT * FROM airport ORDER BY RAND() LIMIT 16")
    return db["cursor"].fetchall()


# This function returns 16 random airports, 2 in each direction
def draw_airports_from_origin(origin):
    flight_bearings = (0, 45, 90, 135, 180, 225, 270, 315)
    ports = []
    # origin_coords = {'lat': origin["latitude_deg"], 'lon': origin["longitude_deg"]}
    dist = (600, 1000)
    for bearing in flight_bearings:
        distance = random.randint(dist[0], dist[1])
        destination = geopy.distance.distance(miles=distance).destination((34, 148), bearing=bearing)
        ports.append(destination)
    print(ports)
    for port in ports:
        db["cursor"].execute(
            f"SELECT TOP 2 * FROM airport WHERE latitude_deg = {port[0]} AND longitude_deg = {port[1]} ORDER BY ABS({port[0]} - latitude_deg)")
        airport_data = db["cursor"].fetchmany(2)
        print(airport_data)


def distance_between_airports(port_1, port_2):
    db["cursor"].execute(
        f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{port_1}' OR ident = '{port_2}'")
    airport_data = db["cursor"].fetchmany(2)
    distance = geopy.distance.distance(airport_data[0], airport_data[1])
    return distance


connect_to_db()
# print(distance_between_airports("EFHK", "EFIV"))
# print(get_some_airports())
# draw_airports_from_origin({})
