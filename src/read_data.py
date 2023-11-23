import csv
from typing import Any

import pandas as pd


def read_csv(the_path_to_the_file: Any) -> Any:
    """
    Считывает данные из файла csv о финансовых операциях
    :param the_path_to_the_file: Путь к файлу csv
    :return: Возвращает, список транзакций из файла сым
    """
    transactions = []
    with open(the_path_to_the_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def read_xlsx(the_path_to_the_file: Any) -> Any:
    """
    Преобразовывает данные из файла xlsx
    :param the_path_to_the_file: Путь к файлу xlsx
    :return: Возвращает, список транзакций из файла xlsx
    """
    df = pd.read_excel(the_path_to_the_file)
    transactions = df.to_dict("records")
    return transactions
