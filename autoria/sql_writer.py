import csv
import sqlite3


def autoria_sql_writer():
    # Create a database file and a connection object
    conn = sqlite3.connect("cars.db")

    # Create a cursor object
    cur = conn.cursor()

    # Drop the table if it already exists
    # cur.execute("DROP TABLE IF EXISTS cars")

    # Create a table with the same column names as the csv file if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS cars "
                "(car_id INTEGER, "
                "data_link_to_view VARCHAR(255), "
                "model_and_year VARCHAR(255), "
                "engine VARCHAR(255), "
                "color VARCHAR(255))")

    # Open the csv file
    with open("cars_no_header.csv", "r") as f:
        # Use csv.reader to read each row
        reader = csv.reader(f)
        # Use a for loop to iterate over each row and insert its values to the db
        for row in reader:
            # Use a list comprehension to fill in the missing values with None
            row = [x if x else None for x in row] + [None] * (5 - len(row))
            # Use a list comprehension to fill in the missing values with None
            cur.execute("INSERT INTO cars VALUES (?,?,?,?,?)", row)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
