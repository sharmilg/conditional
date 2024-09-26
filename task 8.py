#Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
# the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes
# are stored in the ident column of the airport table.

import mysql.connector

def get_airport_info(icao_code):
    query = "select name, municipality from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    if result:
        name, municipality = result
        print(f"Airport Name: {name}")
        print(f"Location (Town): {municipality}")
    else:
        print("No airport found with the given ICAO code.")

    cursor.close()
    connection.close()
    return

connection = mysql.connector.connect(
    user="sharmu",
    password="sharmilg",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

# Prompt the user to enter the ICAO code
icao_code = input("Enter the ICAO code of the airport: ").strip().upper()

get_airport_info(icao_code)


#Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the
# corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are
# stored in the ident column of the airport table.

import mysql.connector
from tabulate import tabulate
def get_airport_by_country(iso_country):
    query = "select name, type from airport where airport.iso_country = %s order by type"
    cursor = connection.cursor()
    cursor.execute(query, (iso_country,))
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers = ["Name", "Type"], tablefmt="fancy_grid"))
    else:
        print("No airport found with the given ISO country code.")

    cursor.close()
    connection.close()
    return

connection = mysql.connector.connect(
    user="sharmu",
    password="sharmilg",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
iso_country = input("Enter the ISO country code of the airport: ").upper()
get_airport_by_country(iso_country)

#Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance
# between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the
# database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the
# library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search
# field and finish the installation.

import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    query = "select latitude_deg, longitude_deg from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result
def calculate_distance(icao1, icao2):
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if not coords1 or not coords2:
        print("No airport found with the given ICAO code(s).")
        return

    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    return distance

connection = mysql.connector.connect(
    user="sharmu",
    password="sharmilg",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci")

icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()
calculate_distance(icao1,icao2)
connection.close()