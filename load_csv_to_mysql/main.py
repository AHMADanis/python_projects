import csv
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost/IP', database='database_name', user='your_user', password='your_password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to the database:", record)

        # CSV file path
        csv_file = 'csv/suppliers.csv'

        # Determine table name from CSV file name
        table_name = csv_file.split('/')[-1].split('.')[0]

        # Open the CSV file and read its contents
        with open(csv_file, 'r') as file:
            csv_data = csv.DictReader(file)
            columns = csv_data.fieldnames

            # Create the table if it doesn't exist
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
            column_definitions = []
            for column in columns:
                column_name = column.strip()
                column_type = 'VARCHAR(255)'  # Default column type
                column_definitions.append(f"{column_name} {column_type}")
            create_table_query += ', '.join(column_definitions) + ")"
            cursor.execute(create_table_query)

            # Iterate over each row in the CSV data
            for row in csv_data:
                # Prepare the INSERT query
                insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) " \
                               f"VALUES ({', '.join(['%s'] * len(columns))})"

                # Execute the query with the row values
                values = [row[column] for column in columns]
                cursor.execute(insert_query, values)

        # Commit the changes and close the connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Data inserted successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)
