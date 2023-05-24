# Import CSV Data into MySQL Table

This Python code snippet demonstrates how to import data from a CSV file into a MySQL database table. It uses the `csv` and `mysql.connector` modules to read the CSV file and establish a connection with MySQL.

## Prerequisites

- Python 3.x
- `csv` module
- `mysql.connector` module

## Usage

1. Make sure you have the necessary Python modules installed. You can install them using pip:

   ```shell
   pip install mysql-connector-python

2. Adjust the database connection details:

   - `host`: The hostname or IP address of your MySQL server.
   - `database`: The name of the target database.
   - `user`: Your MySQL username.
   - `password`: Your MySQL password.

3. Provide the CSV file path:

   Modify the `csv_file` variable to point to the path of your CSV file.

4. Run the code:

   ```shell
   python your_script_name.py