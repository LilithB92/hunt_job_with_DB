import pytest

from src.employers_api import EmployersAPI


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
