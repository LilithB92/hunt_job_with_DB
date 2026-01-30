from src.postgres_db import PostgresDB


def test_postgres_data_init() -> None:
    postgres_db = PostgresDB()
    assert postgres_db.conn is None


def test_close() -> None:
    postgres_db = PostgresDB()
    postgres_db.connect()
    postgres_db.close()
    assert postgres_db.conn is None
