import pytest
from src.masks import mask_user_account, mask_user_card


@pytest.fixture()
def test_data() -> list:
    return ["12345678901234567890", "123456789012345678900", "1234567890123456789",
            "1234567890123456", "123456789012345", "15968378687051990"]


def test_mask_user_account(test_data: str) -> None:
    assert mask_user_account(test_data[0]) == "**7890"
    assert mask_user_account(test_data[1]) == "Введен короткий или длинный номер счета"
    assert mask_user_account(test_data[2]) == "Введен короткий или длинный номер счета"


def test_mask_user_card(test_data: str) -> None:
    assert mask_user_card(test_data[3]) == "1234 56** **** 3456"
    assert mask_user_card(test_data[4]) == "Введен короткий или длинный номер карты"
    assert mask_user_card(test_data[5]) == "Введен короткий или длинный номер карты"
