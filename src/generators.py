from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Функция выдает по очереди операции, в которых указана заданная валюта.
    :param transactions: list[dict]
    :param currency: str
    :return: lost[dict]
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transaction_1: list[dict]) -> Generator:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди
    :param transaction_1: list[dict]
    :return: str
    """
    for transaction in transaction_1:
        yield transaction["description"]


def card_number_generator(start: int, finish: int) -> Generator:
    """
    Генератор номера карт в формате "XXXX XXXX XXXX XXXX
    :param start: int
    :param finish: int
    :return: str
    """
    number_zero = 16 - len(str(finish))
    for number in range(start, finish + 1):
        number_generator = (number_zero * "0") + str(number)
        yield f'{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[12:17]}'
