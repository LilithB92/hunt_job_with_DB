from src.api_hunter import APIHunter


class EmployersAPI(APIHunter):
    """
    Класс для получения API о компаниях.
    """

    base_url: str
    _employers: list

    def __init__(self):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.base_url = "https://api.hh.ru/employers"
        self._employers = []
        super().__init__(self.base_url)

    def get_ten_employers(self, text: str = "разработчик", area: int = None) -> list:
        """
        Получает данные 10 компании из text(IT сфере по умолчанию). Возвращает список словарей компании.
        :param text: Переданное значение ищется в названии и описании работодателя
        :param area:Идентификатор региона работодателя
        :return:Список словарей компании
        """
        params = {"text": text, "area": area, "only_with_vacancies": True, "per_page": 10, "page": 0}
        employers_data = self.get_api_datas(params)
        self._employers = [self.employer_to_dict(emp) for emp in employers_data if employers_data]
        return self._employers

    @staticmethod
    def employer_to_dict(employer: object) -> dict:
        """
        Метод из JSON ответа компании выбирает нужные данные и возвращает словарь.
        :param employer:  JSON ответ компании.
        :return: Словарь с данными вакансиями
        """
        return {"id": employer.get("id"), "name": employer.get("name"), "url": employer.get("url")}
