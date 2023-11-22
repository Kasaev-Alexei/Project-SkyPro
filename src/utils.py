import json
from typing import Any
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_read_json(the_path_to_the_file: str) -> Any:
    """
    Принимает на вход путь до JSON-файла
    :param the_path_to_the_file: str
    :return: Any
    """
    try:
        with open(the_path_to_the_file, encoding="utf8") as file:
            bank_transactions = json.load(file)
    except FileNotFoundError as error:
        logger.error(f"Файл {the_path_to_the_file} не найден: {error}")
        bank_transactions = []
    except json.JSONDecodeError as error:
        logger.error(f"Ошибка при декодировании JSON в файле{the_path_to_the_file}: {error}")
        bank_transactions = []
    return bank_transactions


def transactions(transaction_data: dict) -> float | str:
    """
    Принимает на вход одну транзакцию
    :param transaction_data: dict
    :return: float | str
    """
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        logger.info(f"вернул сумму транзакции в рублях {transaction_data['operationAmount']['amount']}")
        return float(transaction_data["operationAmount"]["amount"])
    else:
        logger.error("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
