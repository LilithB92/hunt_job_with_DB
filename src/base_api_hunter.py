from abc import ABC, abstractmethod


class BaseAPIHunter(ABC):
    """
    Абстрактный базовый класс для работы с API.
    """

    @abstractmethod
    def _request_api_datas(self, params: dict = None) -> list:
        """
        Абстрактный метод получает API данные и возвращает в виде списка.
        :param params:Параметры API
        :return:Список api данных
        """
        pass


