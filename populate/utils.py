"""Utility Functions For Posgress Database."""

import psycopg2


def getConnection():
    """Get Connection Cursor To Postgress Database."""
    db_name = "verceldb"
    db_user = "default"
    db_pass = "bsf5qumCo6OQ"
    db_host = "ep-autumn-night-a4d74qm2-pooler.us-east-1.aws.neon.tech"
    db_port = "5432"

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port
    )
    return conn


def getTableNames():
    """Return List of Table Names In Database."""
    table_names = [
        "units",
        "foodnames",
        "nutritiondata"
    ]
    return table_names


def constructInsertQuery(table_name, col_names):
    """Construct Query To Send To Database."""
    # enumerate through col_names to construct first part
    # of insert query
    query = f"INSERT INTO {table_name} ("
    for col_name in col_names:
        query += f"{col_name}, "
    query += ")"

    # correct parts of query string
    query = query.rstrip(" ,)") + ")"

    # construct ? string at end of query
    # for number of columns
    query += " VALUES ("
    for num in range(len(col_names)):
        query += "%s, "
    query += ")"

    # correct parts of query string
    query = query.rstrip(" ,)") + ")"
    query += ";"
    return query


def handleFoodJSON(foodJson, cur, conn):
    """Handle Food JSON."""
    # construct insert query for inserting
    # food name into database
    query = constructInsertQuery(
        "foodnames",
        ["food_name"]
    )

    # insert food name into database
    try:
        cur.execute(query, (foodJson["Name"], ))
        conn.commit()
        print("Successfully Executed INSERT Command")

    except Exception as e:
        conn.rollback()
        print(f"Error When Executing Insert Statement {e}")

    # get food name's id from foodnames look up table
    try:
        cur.execute(
            "SELECT food_id FROM foodnames WHERE food_name = %s",
            (foodJson["Name"], )
        )
        result = cur.fetchone()
        food_id = result[0]
        print(f"{foodJson['Name']}'s id is {food_id}")

    except Exception as e:
        print(f"Error When Retrieving {foodJson['Name']}'s id {e}")

    # construct insert query for inserting
    # nutrition data into nutritiondata table
    query = constructInsertQuery(
        "nutritiondata",
        [
            "food_id",
            "serving_size",
            "calories",
            "total_fat",
            "saturated_fat",
            "trans_fat",
            "polyunsaturated_fat",
            "monounsaturated_fat",
            "cholesterol",
            "sodium",
            "potassium",
            "total_carbohydrates",
            "dietary_fiber",
            "soluble_fiber",
            "dietary_sugars",
            "total_sugars",
            "added_sugars",
            "erythritol",
            "protein",
        ]
    )

    # insert nutrition facts for food_id into database
    values = (
        food_id,
        foodJson["Serving Size"],
        foodJson["Food Data"]["Calories"],
        foodJson["Food Data"]["Total Fat"],
        foodJson["Food Data"]["Saturated Fat"],
        foodJson["Food Data"]["Trans Fat"],
        foodJson["Food Data"]["Polyunsaturated Fat"],
        foodJson["Food Data"]["Monounsaturated Fat"],
        foodJson["Food Data"]["Cholesterol"],
        foodJson["Food Data"]["Sodium"],
        foodJson["Food Data"]["Potassium"],
        foodJson["Food Data"]["Total Carbohydrates"],
        foodJson["Food Data"]["Dietary Fiber"],
        foodJson["Food Data"]["Soluble Fiber"],
        foodJson["Food Data"]["Dietary Sugars"],
        foodJson["Food Data"]["Total Sugars"],
        foodJson["Food Data"]["Added Sugars"],
        foodJson["Food Data"]["Erythritol"],
        foodJson["Food Data"]["Protein"],
    )
    try:
        cur.execute(
            query,
            values
        )
        conn.commit()
        print("Successfully Executed INSERT Command")

    except Exception as e:
        conn.rollback()
        print(f"Error When Executing Insert Statement {e}")


