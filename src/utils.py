import json
from typing import Any


def get_read_json(the_path_to_the_file: str) -> Any:
    """
    Принимает на вход путь до JSON-файла
    :param the_path_to_the_file: str
    :return: Any
    """
    try:
        with open(the_path_to_the_file, encoding="utf8") as file:
            bank_transactions = json.load(file)
    except FileNotFoundError:
        bank_transactions = []
    except json.JSONDecodeError:
        bank_transactions = []
    return bank_transactions


def transactions(transaction_data: dict) -> float | str:
    """
    Принимает на вход одну транзакцию
    :param transaction_data: dict
    :return: float | str
    """
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_data["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
