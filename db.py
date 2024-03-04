import os
import geopy.distance as distance
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


# This function returns 16 random airports, 2 in each direction
# The origin point is the latitude and longitude of the current airport
# The return value is a list of dictionaries with the keys "flight_direction", "distance" and "airport"
# Distance is returned in kilometers.
# [{"flight_direction: "North-West", "distance": 129, "airport": {...}}, ...]
def draw_airports_from_origin(lat, lon):
    # North, North-East, East, South-East, South, South-West, West, North-West
    flight_bearings = (0, 45, 90, 135, 180, 225, 270, 315)
    bearings_text = ("North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West")
    flights = []
    # Minimum and maximum distance from current airport in miles
    min_dist = 250
    max_dist = 850
    for i in range(len(flight_bearings)):
        bearing = flight_bearings[i]
        # Randomly pick distance to travel to
        flight_distance = random.randint(min_dist, max_dist)
        # Get latitude and longitude of randomly selected place using the origin point
        destination = distance.distance(miles=flight_distance).destination((lat, lon), bearing=bearing)
        # Gets the latitude and longitude of the desired point
        point_lat, point_lon = destination.latitude, destination.longitude
        # Request two airports that are as close as possible to the point
        # This is done by adding the latitude and longitude together and sorting the absolute value
        db["cursor"].execute(
            f"""SELECT * FROM airport
             ORDER BY ABS({point_lat} - latitude_deg) + ABS({point_lon} - longitude_deg) ASC
              LIMIT 2;""")
        # This could also be fetchall() since the query is limited to 2
        # But things might break if somehow more were to slip past
        airport_data = db["cursor"].fetchmany(2)
        # If airports were found, add them to the list that will be returned
        if airport_data:
            for airport in airport_data:
                # Calculate the distance between origin and flight point
                point_a, point_b = [lat, lon], [airport["latitude_deg"], airport["longitude_deg"]]
                dist_to_port = int(distance_between_two_points(point_a, point_b))
                flights.append({"flight_direction": bearings_text[i], "distance": dist_to_port, "airport": airport})

    return flights


# This function calculates the distance between two geographical points
# It takes the latitude and longitude of both places as tuples or lists
# Example: distance_between_two_points((25, 67), (34, 100))
def distance_between_two_points(point_a, point_b):
    flight_distance = distance.distance(point_a, point_b).km
    return flight_distance


# This function returns data about the requested airport from the db
# It requires the airports ident code as a parameter
# Example: get_airport("EFHK")
def get_airport(code):
    if code:
        db["cursor"].execute(f"SELECT * FROM airport WHERE ident = '{code}';")
        airport = db["cursor"].fetchone()
        if airport:
            return airport
        return print(f"Airport {code} doesn't exist.")
    return print("Airport code can't be empty!")


# This function returns data about the requested country from the db
# It requires the country's ISO-code as a parameter
# Example: get_country("FI")
def get_country(iso_country):
    if iso_country:
        db["cursor"].execute(f"SELECT * FROM country WHERE iso_country = '{iso_country}';")
        country = db["cursor"].fetchone()
        if country:
            return country
        return print(f"ISO-code {iso_country} doesn't exist.")
    return print("No ISO-code in parameters!")


def delete_unnecessary_airports():
    db["cursor"].execute("""
    DELETE FROM airport
    WHERE NOT type = "small_airport" AND NOT type = "medium_airport" AND NOT type = "large_airport";
    db["database"].commit()


def modify_game_table():
    db["cursor"].execute("ALTER TABLE game ADD money INT;")
    db["database"].commit()


connect_to_db()
# print(distance_between_airports("EFHK", "EFIV"))
# print(get_some_airports())
# port = get_airport(code="EFHK")
# _flights = draw_airports_from_origin(port["latitude_deg"], port["longitude_deg"])
# for flight in _flights:
#     print(flight["distance"], flight["airport"]["iso_country"], flight["airport"]["type"])
# print(get_country("FI"))

# modify_game_table()

# delete_unnecessary_airports()
