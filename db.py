import os
import geopy.distance as geopy
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
    db["cursor"] = db["database"].cursor(dictionary=True)


def get_some_airports():
    db["cursor"].execute(
        f"SELECT * FROM airport ORDER BY RAND() LIMIT 16")
    return db["cursor"].fetchall()


# This function returns 16 random airports, 2 in each direction
# The origin point is the latitude and longitude of the current airport
# The return value is a list of dictionaries with the keys "flight_direction", "distance" and "airport"
# Distance is returned in kilometers.
# [{"flight_direction: "North-West", "distance": 129, "airport": {...}}, ...]
def draw_airports_from_origin(lat, lon):
    # North, North-East, East, South-East, South, South-West, West, North-West
    flight_bearings = (0, 45, 90, 135, 180, 225, 270, 315)
    bearings_text = ("North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West")
    flight_points = []
    flights = []
    # Minimum and maximum distance from current airport in miles
    min_dist = 300
    max_dist = 950
    for i in range(len(flight_bearings)):
        bearing = flight_bearings[i]
        # Randomly pick distance to travel to
        distance = random.randint(min_dist, max_dist)
        # Get latitude and longitude of randomly selected place using the origin point
        destination = geopy.distance(miles=distance).destination((lat, lon), bearing=bearing)
        # Add flight point and the point's direction
        flight_points.append({"dest": destination, "dir": bearings_text[i]})
    # Find two airports per flight point
    for point in flight_points:
        # Gets the latitude and longitude of the desired point
        lat, lon = point["dest"][0], point["dest"][1]
        # Request two airports that are as close as possible to the point
        # This is done by adding the latitude and longitude together and sorting the absolute value
        db["cursor"].execute(
            f"SELECT * FROM airport ORDER BY ABS({lat} - latitude_deg) + ABS({lon} - longitude_deg) LIMIT 2;")
        # This could also be fetchall() since the query is limited to 2
        # But things might break if somehow more were to slip past
        airport_data = db["cursor"].fetchmany(2)
        # If airports were found, add them to the list that will be returned
        if airport_data:
            for airport in airport_data:
                # Calculate the distance between origin and flight point
                point_a, point_b = [lat, lon], [airport["latitude_deg"], airport["longitude_deg"]]
                dist_to_port = int(distance_between_two_points(point_a, point_b))
                flights.append({"flight_direction": point["dir"], "distance": dist_to_port, "airport": airport})

    return flights


def distance_between_two_points(point_a, point_b):
    distance = geopy.distance(point_a, point_b).km
    return distance


connect_to_db()
# print(distance_between_airports("EFHK", "EFIV"))
# print(get_some_airports())
print(draw_airports_from_origin(34, 130))
