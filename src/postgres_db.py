import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()


class PostgresDB:
    def __init__(self):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.connection_params = {
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASS"),
            "host": os.getenv("POSTGRES_HOST"),
            "port": os.getenv("POSTGRES_PORT"),
        }
        self.conn = None
        self.cur = None

    def connect(self, dbname: str = "postgres"):
        """Установление соединения с базой данных"""
        try:
            if not self.conn:
                self.conn = psycopg2.connect(**self.connection_params,dbname=dbname)
                print("Connection to PostgresSQL successful.")
        except Error as e:
            print(f"Error connecting to PostgresSQL: {e}")

    def close(self):
        """Метод закроет курсор и соединение с базой данных."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
