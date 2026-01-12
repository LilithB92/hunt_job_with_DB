from src.api_hunter import APIHunter


class VacanciesAPI(APIHunter):
    """
    Класс для получения API о вакансиях.
    """
    def __init__(self):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self._base_url = "https://api.hh.ru/vacancies"
        super().__init__(self._base_url)
