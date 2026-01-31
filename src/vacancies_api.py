from src.api_hunter import APIHunter


class VacanciesAPI(APIHunter):
    """
    Класс для получения API о вакансиях.
    """

    def __init__(self):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        """
        self.base_url = "https://api.hh.ru/vacancies"
        super().__init__(self.base_url)
        self.company_vacancies = []

    def add_one_company_vacancies(self, emp_id: str) -> None:
        """
        Получение списка вакансий работодателя по его emp_id
        :param emp_id: идентификатор компании
        :return: список словарей вакансии
        """
        page = 0
        while True:
            par = {"employer_id": emp_id, "per_page": 10, "page": page}
            if self.get_api_datas(par):
                company_vacancies = self.get_api_datas(par)
                [
                    self.company_vacancies.append(self.vacancy_to_dict(vacancy))
                    for vacancy in company_vacancies
                    if vacancy
                ]
            else:
                break
            page += 1
        del page

    @staticmethod
    def vacancy_to_dict(vacancy: object) -> dict:
        """
        Метод из JSON ответа вакансии выбирает нужные данные и возвращает словарь.
        :param vacancy:  JSON ответ вакансии.
        :return: Словарь с данными вакансиями
        """
        return {
            "employer_id": vacancy["employer"]["id"],
            "title": vacancy["name"],
            "url": vacancy["alternate_url"],
            "salary_from": vacancy["salary"].get("from", None) if vacancy["salary"] else None,
            "salary_to": vacancy["salary"].get("to", None) if vacancy["salary"] else None,
            "currency": vacancy["salary"].get("currency", None) if vacancy["salary"] else None,
            "requirement": vacancy["snippet"]["requirement"],
        }

    def get_all_companies_vacancies(self, id_list: list[str]) -> list:
        """
        Получает все вакансии из компании, чей id присутствует в списке. И возвращает все вакансии.
        :param id_list: Список компании id.
        :return: Список Вакансии
        """
        try:
            for emp_id in id_list:
                self.add_one_company_vacancies(emp_id)
            return self.company_vacancies
        except TypeError:
            return []


if __name__ == "__main__":
    vac = VacanciesAPI()
    vac.add_one_company_vacancies(emp_id="872241")
    # vac.add_company_vacancies(emp_id="10413982")
    # pprint.pprint(vac.company_vacancies)
    # pprint.pprint(vac.get_all_companies_vacancies(["872241"]))
