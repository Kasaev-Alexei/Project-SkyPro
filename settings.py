from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath(ROOT_PATH, 'data')
OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'operations.json')
TEST_OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'test_operation.json')
TEST_OPERATIONS_EMPTY = DATA_PATH.joinpath(DATA_PATH, 'empty_list_of_operations.json')
