import psycopg2
from psycopg2.sql import NULL

from src.employers_api import EmployersAPI
from src.postgres_db import PostgresDB
from src.vacancies_api import VacanciesAPI


class DBCreator(PostgresDB):
    """
    Класс для создания база данных и таблиц.
    """

    def create_database(self, db_name: str) -> None:
        """
        Создание базы данных
        :param db_name: Название база данных
        :return: None
        """
        try:
            # Подключаемся
            self.connect()
            self.conn.autocommit = True

            # Формирование запроса
            with self.conn.cursor() as self.cur:

                self.cur.execute(
                    f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '{db_name}'"
                )  # Закрываем сессии
                self.cur.execute(f"DROP DATABASE IF EXISTS {db_name}")  # Удаляем БД
                self.cur.execute(f"CREATE DATABASE {db_name}")  # Создаем БД
            print(f'База "{db_name}" успешно пересоздана!')

        except psycopg2.Error as e:
            print(f"Ошибка при создании БД: {e}")
            raise
        finally:
            self.close()

    #
    def create_tables(self, db_name: str) -> None:
        """
        Создаем таблицу employers и vacancies в базе данных
        :param db_name: Название база данных, где создаются таблицы.
        :return: None
        """
        try:
            self.connect(db_name)
            with self.conn.cursor() as self.cur:
                self.cur.execute(
                    """
                    CREATE TABLE employees (
                    employer_id VARCHAR(50) PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    url VARCHAR(255) NOT NULL
                    )
                """
                )
                self.cur.execute(
                    """
                    CREATE TABLE vacancies (
                        vacancy_id  SERIAL PRIMARY KEY,
                        employer_id VARCHAR(50) REFERENCES employees(employer_id),
                        title VARCHAR(255) NOT NULL,
                        requirement TEXT,
                        salary_from INTEGER,
                        salary_to INTEGER,
                        currency VARCHAR(10),
                        url VARCHAR(255)
                    )
                """
                )
            self.conn.commit()
            print("Таблицы 'employees' и 'vacancies' успешно созданы.")

        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Ошибка при создании таблицы: {e}")
            raise
        finally:
            self.close()

    def fill_employers_in_db(self, db_name: str, employers: list[dict]) -> None:
        """
        Сохранение данных в таблицу работодателя
        :param db_name: Название база данных.
        :param employers: Список словарей работодателей
        :return: None
        """
        try:
            self.connect(db_name)
            with self.conn.cursor() as self.cur:
                for employer in employers:
                    self.cur.execute(
                        """
                        INSERT INTO employees (employer_id, name, url)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (employer_id) DO NOTHING
                    """,
                        (
                            employer["id"],
                            employer["name"],
                            employer["url"],
                        ),
                    )
            self.conn.commit()
            print(f"Работодатель '{employer['name']}' сохранен в БД > 'employees'.")

        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Ошибка при создании работодателя {employer.get('name')}: {e}")
            raise
        finally:
            self.close()

    def fill_vacancies_in_db(self, db_name: str, vacancies: list[dict]) -> None:
        """
        Сохранение списков вакансий в таблицу vacancies
        :param db_name:
        :param vacancies:
        :return:
        """
        try:
            self.connect(db_name)
            with self.conn.cursor() as cur:
                for vacancy in vacancies:
                    if vacancy["salary_from"] is None and vacancy["salary_to"] is None:
                        continue
                    else:
                        cur.execute(
                            """
                            INSERT INTO vacancies 
                            (employer_id, title, requirement, salary_from, salary_to, currency, url)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (vacancy_id) DO NOTHING
                            """,
                            (
                                vacancy["employer_id"],
                                vacancy["title"],
                                vacancy["requirement"],
                                vacancy.get("salary_from", NULL),
                                vacancy.get("salary_to", NULL),
                                vacancy.get("currency", NULL),
                                vacancy.get("url", NULL),
                            ),
                        )
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rellback()
            print(f"Ошибка при сохранении вакансии: {e}")
            raise
        finally:
            self.close()


if __name__ == "__main__":
    db = DBCreator()
    db.create_database("esim")
    db.create_tables("esim")
    ea = EmployersAPI()
    emp_list = ea.get_ten_employers(area=1)
    emp_id = [emp["id"] for emp in emp_list]
    vac = VacanciesAPI()
    vac_list = vac.get_all_companies_vacancies(emp_id)
    db.fill_employers_in_db("esim", emp_list)
    db.fill_vacancies_in_db("esim", vac_list)
