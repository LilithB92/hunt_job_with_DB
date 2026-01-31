from typing import Any
from unittest.mock import patch

from src.employers_api import EmployersAPI


def test_employers_api(employers) -> None:
    assert employers.base_url == "https://api.hh.ru/employers"


@patch("src.api_hunter.requests.get")
def test_employers_api_request_error(mocked_get: Any, employer_api_data) -> None:
    employers_api = EmployersAPI()
    mocked_get.return_value.status_code = 400
    assert employers_api.get_ten_employers() == []


@patch("src.api_hunter.requests.get")
def test_employers_api_request(mocked_get: Any, employer_api_data: list) -> None:
    employers_api = EmployersAPI()
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value.items.return_value = employer_api_data
    print(employers_api.get_ten_employers())


def test_employer_to_dict(employer_api_data: dict, employers_to_dict_result: dict) -> None:
    employers_api = EmployersAPI()
    assert employers_api.employer_to_dict(employer_api_data) == employers_to_dict_result
