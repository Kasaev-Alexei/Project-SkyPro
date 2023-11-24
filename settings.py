from pathlib import Path
import os

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath(ROOT_PATH, 'data')
OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'operations.json')
TEST_OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'test_operation.json')
TEST_OPERATIONS_EMPTY = DATA_PATH.joinpath(DATA_PATH, 'empty_list_of_operations.json')

FILE_PATH_CSV = ROOT_PATH.joinpath("data", "transactions.csv")
FILE_PATH_EXCEL = ROOT_PATH.joinpath("data", "transactions_excel.")


