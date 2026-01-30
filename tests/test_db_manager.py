from src.db_manager import DBManager
from src.utils import create_db_with_tables




def test_db_manager(employers_to_dict_result, vacancies_to_dict_result, )->None:
    create_db_with_tables('test')
    db_manager = DBManager('test')
    assert db_manager.get_all_vacancies() == []
    assert db_manager.get_vacancies_with_keyword('test') == []
    assert  db_manager.get_avg_salary() == 0.00
    assert db_manager.get_vacancies_with_higher_salary() == []
    assert db_manager.get_companies_and_vacancies_count() == []




