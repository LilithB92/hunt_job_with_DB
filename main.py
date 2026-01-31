import pprint
from typing import Any

from src.db_manager import DBManager
from src.utils import create_db_with_tables, fill_api_to_db


def user_interaction() -> Any:
    """
    Функция для взаимодействия с пользователем
    :return:
    """
    db_manager = DBManager()
    print("Вам представим список всех компаний и количество вакансий у каждой компании.")
    pprint.pprint(db_manager.get_companies_and_vacancies_count())

    print("\n Если Вам интересно все вакансии,введите да")
    query = input(" введите да: ").strip().lower()
    if query == "да":
        pprint.pprint(db_manager.get_all_vacancies())

    print("\n Если Вам интересно  средняя зарплата по вакансиям введите да")
    query = input("\nЕсли Вам интересно средняя зарплата по вакансиям указывайте да : ").strip().lower()
    if query == "да":
        print(db_manager.get_avg_salary())

    print("Хотите получать список всех вакансий, у которых зарплата выше " "средней по всем вакансиям, то введите да")
    query = input("\nЕсли Вам интересно вакансии, у которых зарплата выше средней  введите да: ").strip().lower()
    if query == "да":
        pprint.pprint(db_manager.get_vacancies_with_higher_salary())

    print(
        "\nХотите получать всех вакансий, в названии которых содержатся переданные Вам слово, "
        "например инженер,то введите Ваша слово "
    )
    query = input("\nвведите Ваша слово: ").strip().lower()
    if query:
        vacancies = db_manager.get_vacancies_with_keyword(query)
        if vacancies:
            pprint.pprint(vacancies)
        else:
            print("\nК сожалению пока нет вакансии по вашему запросу\n")


if __name__ == "__main__":
    create_db_with_tables()
    fill_api_to_db()
    user_interaction()
