from src.utils import create_db_with_tables, fill_api_to_db


def test_create_db_with_tables()->None:
    create_db_with_tables()


def test_fill_api_to_db()->None:
    fill_api_to_db()