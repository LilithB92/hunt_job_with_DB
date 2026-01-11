from abc import ABC, abstractmethod


class BaseAPIHunter(ABC):
    """
    Абстрактный базовый класс для работы с API.
    """

    def __init__(self, base_url):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param base_url:Сылака API
        """
        self.base_url = base_url

    @abstractmethod
    def get_api_datas(self, params: dict = None) -> list:
        """
        Абстрактный метод получает API данные и возвращает в виде списка.
        :param params:Параметры API
        :return:Список api данных
        """
        pass
