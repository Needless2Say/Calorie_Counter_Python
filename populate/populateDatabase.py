"""Populate Database With Food Data From Excel Spreadsheet."""

import os
import json
from utils import *


def populateDatabase():
    """Populate Database With Food Data."""
    # connect to postgress database
    try:
        conn = getConnection()
        cur = conn.cursor()
        print("Connected to Postgress Database Successfully")

    except Exception as e:
        print(f"Error When Connecting to Postgress Database: {e}")

    # loop through all json files in the to_input folder
    path = "../To_Input/Foods"
    for filename in os.listdir(path):
        # define file path
        file_path = os.path.join(path, filename)

        # check if file_path leads to a file
        if os.path.isfile(file_path):
            # open file
            with open(file_path, 'r') as file:
                # read json file
                foodJson = json.load(file)

                # handle food JSON INSERT commands
                handleFoodJSON(foodJson, cur, conn)

    # close connection and cursor to postgress database
    try:
        cur.close()
        conn.close()
        print("Closed Connection to Database Successfully")

    except Exception as e:
        print("Failed to Close Connection to Database")


def main():
    """Main Function For Creating Database Structure."""
    populateDatabase()


if __name__ == "__main__":
    main()
