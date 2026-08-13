import mysql.connector

connection = None


def open_connection():
    global connection

    if connection is None or not connection.is_connected():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YourNewPasswordHere!",
            database="ResearchExpertiseDB"
        )

    return connection


def close_connection():
    global connection

    if connection is not None and connection.is_connected():
        connection.close()