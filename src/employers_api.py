from src.api_hunter import APIHunter


class EmployersAPI(APIHunter):
    """
    Класс для получения API о компаниях.
    """

    def __init__(self):
        """
         Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self._base_url='https://api.hh.ru/employers'



    def get_employers_names_with_id(self)->dict:
        """

        :return:
        """
        pass




if __name__ =="__main__":
    ea=EmployersAPI()
    print(ea._request_api_datas())