from dotenv import load_dotenv
from typing import Literal, Optional, Generator
from contextlib import contextmanager
from mysql.connector import Error
import os
import random
import datetime
import mysql.connector

load_dotenv()

HOST = os.environ.get('DB_HOST', '')
PORT = os.environ.get('DB_PORT', '')
USER = os.environ.get('DB_USER', '')
PASSWORD = os.environ.get('DB_PASSWORD', '')
DATABASE = os.environ.get('DB_DATABASE', '')

def get_process_id() -> str:
    """
    Generate a random process ID.

    Returns:
        str: A random process ID.
    """
    return str(random.randint(10000000, 99999999))


def create_connection():
    """Create a connection to the MariaDB database."""
    try:
        connection = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if connection.is_connected():
            print("Connected to MariaDB database")
            return connection
    except Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

# Esempio di utilizzo della funzione
conn = create_connection()
if conn:
    # Chiudi la connessione al termine
    conn.close()
    print("Connection closed")