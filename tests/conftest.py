import pytest

from src.employers_api import EmployersAPI
from src.vacancies_api import VacanciesAPI


@pytest.fixture
def employers() -> object:
    return EmployersAPI()


@pytest.fixture
def employer_api_data() -> dict:
    return {
        "alternate_url": "https://hh.ru/employer/872241",
        "id": "872241",
        "is_identified_by_esia": False,
        "logo_urls": {
            "240": "https://img.hhcdn.ru/employer-logo-round/762447.png",
            "90": "https://img.hhcdn.ru/employer-logo-round/762446.png",
            "original": "https://img.hhcdn.ru/employer-logo-original-round/762445.png",
        },
        "name": "AB Development",
        "open_vacancies": 7,
        "url": "https://api.hh.ru/employers/872241",
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=872241",
    }


@pytest.fixture
def employers_to_dict_result() -> dict:
    return {"id": "872241", "name": "AB Development", "url": "https://api.hh.ru/employers/872241"}


@pytest.fixture
def vacancies_api() -> object:
    return VacanciesAPI()


@pytest.fixture
def vacancies_api_datas() -> dict:
    return {
        "alternate_url": "https://hh.ru/vacancy/129519984",
        "name": "Бухгалтер по расчету выручки (ЖКХ)",
        "salary": {"currency": "RUR", "from": 40000, "gross": False, "to": 45000},
        "employer": {
            "accredited_it_employer": False,
            "alternate_url": "https://hh.ru/employer/872241",
            "country_id": 1,
            "id": "872241",
        },
        "salary_range": {"currency": "RUR", "from": 40000, "to": 45000},
        "snippet": {
            "requirement": "Опыт работы от 1 до 3 лет в аналогичной "
            "должности. Ответственность и внимательность к "
            "деталям."
        },
        "url": "https://api.hh.ru/vacancies/129519984?host=hh.ru",
    }


@pytest.fixture
def vacancies_to_dict_result() -> dict:
    return {
        "currency": "RUR",
        "employer_id": "872241",
        "requirement": "Опыт работы от 1 до 3 лет в аналогичной должности. "
        "Ответственность и внимательность к деталям.",
        "salary_from": 40000,
        "salary_to": 45000,
        "title": "Бухгалтер по расчету выручки (ЖКХ)",
        "url": "https://hh.ru/vacancy/129519984",
    }
