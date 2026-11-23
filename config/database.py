import mysql.connector


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root123",
            database="employee_management"
        )

        return connection

    except mysql.connector.Error as error:
        print("Database connection error:", error)
        return None