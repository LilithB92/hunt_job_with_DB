import pprint

from src.api_hunter import APIHunter


class EmployersAPI(APIHunter):
    """
    Класс для получения API о компаниях.
    """

    _base_url: str
    _employers: list

    def __init__(self):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self._base_url = "https://api.hh.ru/employers"
        self._employers = []
        super().__init__(self._base_url)

    def get_employers_datas(self, params: dict) -> list:
        """
        Получает данные компании из API, если не найдет возвращать пустой лист
        :param params:API параметр для конкретизации получение данных.
        :return:Список API данных.
        """
        try:

            response = self._request_api_datas(params)
            return response.get("items", [])
        except ValueError():
            return []

    def get_ten_employers(self, text: str = "разработчик", area: int = None) -> list:
        """
        Получает данные 10 компании из text(IT сфере по умолчанию). Возвращает список словарей компании.
        :param text: Переданное значение ищется в названии и описании работодателя
        :param area:Идентификатор региона работодателя
        :return:Список словарей компании
        """
        params = {"text": text, "area": area, "per_page": 10, "page": 0}
        employers_data = self.get_employers_datas(params)
        self._employers = [
            {"id": emp.get("id"), "name": emp.get("name"), "url": emp.get("url")}
            for emp in employers_data
            if employers_data
        ]
        return self._employers


if __name__ == "__main__":
    ea = EmployersAPI()
    pprint.pprint(ea.get_ten_employers(area=1))
