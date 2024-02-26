import os
import geopy.distance
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_variables = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE')
}
print(db_variables)

db = mysql.connector.connect(**db_variables)
cursor = db.cursor()


def distance_between_airports(port_1, port_2):
    cursor.execute(
        f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{port_1}' OR ident = '{port_2}'")
    airport_data = cursor.fetchmany(2)
    distance = geopy.distance.distance(airport_data[0], airport_data[1])
    return distance
