from typing import Any
from unittest.mock import patch

from src.vacancies_api import VacanciesAPI


def test_vacancies_api(vacancies_api) -> None:
    assert vacancies_api.base_url == "https://api.hh.ru/vacancies"


@patch("src.api_hunter.requests.get")
def test_vacancies_api_request_error(mocked_get: Any) -> None:
    vacancies_api = VacanciesAPI()
    mocked_get.return_value.status_code = 400
    assert vacancies_api.add_one_company_vacancies("1") is None


@patch("src.api_hunter.requests.get")
def test_vacancies_api_request(mocked_get: Any, vacancies_api_datas, vacancies_to_dict_result) -> None:
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value.items.return_value = vacancies_api_datas


def test_get_all_company_error() -> None:
    vac_api = VacanciesAPI()
    assert vac_api.get_all_companies_vacancies([]) == []


def test_employer_to_dict(vacancies_api_datas: dict, vacancies_to_dict_result: dict) -> None:
    vac_api = VacanciesAPI()
    assert vac_api.vacancy_to_dict(vacancies_api_datas) == vacancies_to_dict_result
