"""Create Database Schema."""

from utils import *


def createDatabase():
    """Create Schemas For Database."""
    sql_script = None
    # read in sql commands from databaseSchema.sql file
    try:
        with open("databaseSchema.sql", 'r') as file:
            sql_script = file.read()
        print("SQL file read successfully")

    except Exception as e:
        print(f"An error occurred while reading the SQL file: {e}")

    # connect to postgress database
    try:
        conn = getConnection()
        cur = conn.cursor()
        print("Connected to Postgress Database Successfully")

    except Exception as e:
        print(f"Error When Connecting to Postgress Database: {e}")

    # run sql commands in postgress database
    try:
        # split commands by semi-colons
        sql_commands = sql_script.split(';')

        # loop through commands and run them
        # on postgress database
        for command in sql_commands:
            if command.strip():
                cur.execute(command)
        # commit commands
        conn.commit()
        print("Ran All SQL Commands Successfully")

    except Exception as e:
        # roll back commands in case of error
        conn.rollback()
        print(f"Error executing SQL script: {e}")

    # close connection and cursor to postgress database
    try:
        cur.close()
        conn.close()
        print("Closed Connection to Database Successfully")

    except Exception as e:
        print("Failed to Close Connection to Database")


def main():
    """Main Function For Creating Database Structure."""
    createDatabase()


if __name__ == "__main__":
    main()