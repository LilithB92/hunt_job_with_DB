from src.db_creator import DBCreator
from src.employers_api import EmployersAPI
from src.vacancies_api import VacanciesAPI


def create_db_with_tables(db_name: str = "hh_api_db") -> None:
    """
    Создает база данных с таблицами(vacancies, employees)
    :param db_name: название база данных (по умолчанию "hh_api_db")
    :return: None
    """
    db = DBCreator()
    db.create_database(db_name)
    db.create_tables(db_name)


def fill_api_to_db(db_name: str = "hh_api_db") -> None:
    """
    Заполняет таблицы (vacancies, employees) с данными API
    :param db_name:  название база данных (по умолчанию "hh_api_db")
    :return: None
    """
    db = DBCreator()
    employers_api = EmployersAPI()
    employers_list = employers_api.get_ten_employers()
    employers_id = [employer["id"] for employer in employers_list]
    vacancies_api = VacanciesAPI()
    vacancies_list = vacancies_api.get_all_companies_vacancies(employers_id)
    db.fill_employers_in_db(db_name, employers_list)
    db.fill_vacancies_in_db(db_name, vacancies_list)


