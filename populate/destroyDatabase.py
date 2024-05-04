"""Destroy Database Schema."""

from utils import *


def destroyDatabase():
    """Destroy All Tables In Database."""
    # get table names from database
    table_names = getTableNames()

    # connect to postgress database
    try:
        conn = getConnection()
        cur = conn.cursor()
        print("Connected to Postgress Database Successfully")

    except Exception as e:
        print(f"Error When Connecting to Postgress Database: {e}")

    try:
        # loop through table names and drop each table from database
        for name in table_names:
            command = f"DROP TABLE IF EXISTS {name} CASCADE;"
            # drop table from database
            cur.execute(command)
        # commit commands
        conn.commit()
        print("Successfully Dropped All Tables in Database")

    except Exception as e:
        conn.rollback()
        print(f"Error When Trying to Delete Tables From Database {e}")

    # close connection and cursor to database
    try:
        cur.close()
        conn.close()
        print("Successfully Closed Connection to Database")
    except Exception as e:
        print("Failed to Close Connection to Database")


def main():
    """Main Function For Creating Database Structure."""
    destroyDatabase()


if __name__ == "__main__":
    main()