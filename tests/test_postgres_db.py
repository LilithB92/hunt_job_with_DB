import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

from src.postgres_db import PostgresDB

load_dotenv()

def test_postgres_data_init()->None:
    postgres_db =PostgresDB()
    assert postgres_db.conn is None