import pytest

from src.db_creator import DBCreator


def test_create_database() -> None:
    db_creator = DBCreator()
    db_creator.connect()
    db_creator.conn.autocommit = True
    with db_creator.conn.cursor() as cur:
        cur.execute("DROP DATABASE IF EXISTS test")
        db_creator.create_database("test")


def test_create_table() -> None:
    db_creator = DBCreator()
    db_creator.create_database("test")
    db_creator.create_tables("test")


def test_fill_employers_in_db(employer_api_data) -> None:
    emp_list = [employer_api_data]
    db_creator = DBCreator()
    db_creator.create_database("test")
    db_creator.create_tables("test")
    db_creator.fill_employers_in_db("test", emp_list)
    with pytest.raises(AttributeError):
        db_creator.fill_employers_in_db("error_db", emp_list)


def test_fill_vacancies_in_db(vacancies_to_dict_result) -> None:
    vac_list = [vacancies_to_dict_result]
    db_creator = DBCreator()
    db_creator.create_database("test")
    db_creator.create_tables("test")
    db_creator.fill_vacancies_in_db("test", vac_list)
