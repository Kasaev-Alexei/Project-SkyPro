import unittest.mock

import pandas as pd

from settings import FILE_PATH_CSV, FILE_PATH_EXCEL
from src.read_data import read_csv, read_xlsx


def test_read_csv_with_mock() -> None:
    with unittest.mock.patch("src.read_data.csv.DictReader") as mock_csv_reader:
        mock_csv_reader.return_value = [{"id": "1", "name": "Alexei"}]
        result = read_csv(FILE_PATH_CSV)
    assert result == [{"id": "1", "name": "Alexei"}]


def test_read_xlsx_with_patch() -> None:
    with unittest.mock.patch("src.read_data.pd.read_excel") as mock_exel_reader:
        mock_exel_reader.return_value = pd.DataFrame({"id": [1], "name": ["Alexei"]})
        result = read_xlsx(FILE_PATH_EXCEL)
    assert result == [{"id": 1, "name": "Alexei"}]
