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
        self.base_url = base_url

    def _request_api_datas(self, params: dict = None) -> dict:
        """"""
        resp = requests.get(f"{self.base_url}", params)
        if resp.status_code == 200:
            return resp.json()
        else:
            # raise ValueError("No datas")
            return {}

    def get_api_datas(self, params: dict = None) -> list:
        """
        Получает данные компании из API, если не найдет возвращать пустой лист
        :param params:API параметр для конкретизации получение данных.
        :return:Список API данных.
        """
        try:
            response = self._request_api_datas(params)
            return response["items"]
        except Exception:
            return []
