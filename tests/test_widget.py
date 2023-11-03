import pytest

from src.widget import chek_card_and_account, date_and_time


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_parametrize_card_account(data: str, expected: str) -> None:
    assert chek_card_and_account(data) == expected


@pytest.mark.parametrize("data, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_date_time(data: str, expected: str) -> None:
    assert date_and_time(data) == expected
