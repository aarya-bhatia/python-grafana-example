import mysql.connector
from mysql.connector import Error

db_host = 'localhost'
db_user = 'root'
db_password = 'password'


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )

        print("MySQL Database connection successful")
        return connection

    except Error as err:
        print(f"Error: '{err}'")
        exit(1)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
        return True
    except Error as err:
        print(query)
        print(f"Error: '{err}'")
        return False


def read_query(connection, query):
    cursor = connection.cursor()
    result = []

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
    except Error as err:
        print(f"Error: '{err}'")

    return result


create_products_table = """
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    quantity INT NOT NULL DEFAULT 0
);
"""

add_products_query = """
INSERT INTO products (name, quantity) VALUES
('A', 10),
('B', 10),
('C', 10),
('D', 10);
"""
