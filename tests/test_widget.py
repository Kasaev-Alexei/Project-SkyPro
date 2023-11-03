import pytest

from src.widget import chek_card_and_account, date_and_time


@pytest.mark.parametrize(
    "x, y",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_parametrize_card_account(x: str, y: str) -> None:
    assert chek_card_and_account(x) == y


@pytest.mark.parametrize("z, v", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_date_time(z: str, v: str) -> None:
    assert date_and_time(z) == v
