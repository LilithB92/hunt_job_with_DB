import requests

from src.base_api_hunter import BaseAPIHunter


class EmployersAPI(BaseAPIHunter):
    """
    Класс для получения API о компаниях.
    """

    def __init__(self):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self._base_url='https://api.hh.ru/employers'

    def _request_api_datas(self, params: dict = None) -> list:
        resp = requests.get(f"{self._base_url}", params)
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError("No datas")




if __name__ =="__main__":
    ea=EmployersAPI()
    print(ea._request_api_datas())