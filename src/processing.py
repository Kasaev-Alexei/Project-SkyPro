from operator import itemgetter
from typing import Dict, List, Optional

from src.data_file import data_list, date


def get_sorted_data(data: List[Dict[str, str]], state: Optional[str] = "EXECUTED") -> List[Dict[str, str]]:
    """
    Функция принимает на вход список словарей и значение для ключа state
    :param data: Список словарей
    :param state: Значение для ключа
    :return: Список словарей с ключом state
    """
    filter_data = list(filter(lambda x: x.get("state") == state, data))
    return filter_data


def sorted_date(data: list[dict], sort: bool = True) -> list[dict]:
    """
    Сортировка по возрастанию или убыванию даты в зависимости от условия
    :param data:Список словарей
    :param sort: Булевое значение
    :return: Отсортированный список словарей
    """
    date_sort = sorted(data, key=itemgetter("date"), reverse=sort)
    return date_sort


print(get_sorted_data(data_list, "CANCELED"))
print(sorted_date(date))
