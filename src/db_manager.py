import pprint
from typing import Optional

from psycopg2 import OperationalError

from src.postgres_db import PostgresDB


class DBManager(PostgresDB):
    """Взаимодействие с базой данных"""

    def __init__(self, db_name: str = "hh_api_db"):
        super().__init__()
        self.db_name = db_name

    def execute_query(self, query, params=None) -> list[tuple]:
        """
        Выполняет один sql запрос и при необходимости получает результаты.
        :param query: SQL запрос
        :param params: Параметры запроса
        :return: Ответ запроса
        """
        if not self.conn:
            print("No database connection. Please connect first.")
        try:
            self.connect(self.db_name)
            with self.conn.cursor() as self.cur:
                self.cur.execute(query, params)
                return self.cur.fetchall()  # Use fetchall() for multiple rows
        except OperationalError as e:
            print(f"An error occurred during query execution: {e}")
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()

    def get_companies_and_vacancies_count(self) -> list[tuple]:
        """
        получает список всех компаний и количество вакансий у каждой компании
        :return:
        """
        query = (
            "SELECT employees.name, COUNT(vacancies.vacancy_id) AS total_vacancies "
            "FROM employees "
            "LEFT JOIN vacancies USING(employer_id) "
            "GROUP BY employees.employer_id "
            "ORDER BY total_vacancies DESC"
        )
        return self.execute_query(query)

    def get_all_vacancies(self) -> list[tuple]:
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        :return:
        """
        query = (
            "SELECT employees.name, vacancies.title, vacancies.salary_from, vacancies.salary_to, vacancies.url "
            "FROM vacancies "
            "LEFT JOIN employees USING(employer_id)"
        )
        return self.execute_query(query)

    def get_avg_salary(self) -> Optional[float]:
        """
        получает среднюю зарплату по вакансиям
        :return:
        """
        query = (
            "SELECT "
            "(AVG(COALESCE(salary_from, salary_to))+ AVG(COALESCE(salary_to, salary_from)))/2  as  avg_salary "
            "FROM vacancies"
        )
        avg_salary = self.execute_query(query)
        return round(avg_salary[0][0], 2)

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        """
        avg_salary = self.get_avg_salary()
        query = f"SELECT * FROM vacancies WHERE (salary_from+salary_to)/2 > {avg_salary}"
        return self.execute_query(query)

    def get_vacancies_with_keyword(self, text: str) -> list[tuple]:
        """
         получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        :return:
        """
        query = (
            f"SELECT * FROM vacancies WHERE (LOWER(vacancies.requirement) LIKE LOWER('%{text}%')) OR "
            f"(LOWER(vacancies.title) LIKE LOWER('%{text}%'))"
        )
        return self.execute_query(query)


if __name__ == "__main__":
    db_man = DBManager()

    pprint.pprint(db_man.get_vacancies_with_keyword("Бухгалтер"))
