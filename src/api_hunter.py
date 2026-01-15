import requests

from src.base_api_hunter import BaseAPIHunter


class APIHunter(BaseAPIHunter):
    """
    Класс для получения данные API.
    """

    def __init__(self, base_url):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self._base_url = base_url

    def _request_api_datas(self, params: dict = None) -> dict:
        """"""
        resp = requests.get(f"{self._base_url}", params)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError("No datas")
