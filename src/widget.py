from src.masks import mask_user_account, mask_user_card


def card_name_and_number(name_card: str) -> str:
    """
    Функция принимает на вход номер карты и название карты и проверяет их
    :param name_card: Номер для маскирования карты и название карты
    :return: название карты и маску карты
    """
    name_number_card = name_card.split()
    check_name_card = name_number_card[0]
    check_number_card = name_number_card[1]

    if check_name_card == "Maestro" and len(check_number_card) == 16:
        return f"{check_name_card} {mask_user_card(check_number_card)}"
    else:
        return f"Не верно введен номер карты или название карты"


def account_name_and_number(name_account: str) -> str:
    """
    Функция принимает на вход номер счета и название счета и проверяет их
    :param name_account: Номер для маскирования счета и название счета
    :return: название счета и маску счета
    """
    name_number_account = name_account.split()
    check_name_account = name_number_account[0]
    check_number_account = name_number_account[1]

    if check_name_account == "Счет" and len(check_number_account) == 20:
        return f"{check_name_account} {mask_user_account(check_number_account)}"
    else:
        return f"Не верно введен номер карты или название карты"


def date_and_time(date: str) -> str:
    """
    Функция принимает на вход дату и время
    :param test: принимает дату и время
    :return: Дату в формате ДД.ММ.ГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(card_name_and_number("Maestro 1234567890123456"))
print(account_name_and_number("Счет 12345678901234567890"))
print(date_and_time("2018-07-11T02:26:18.671407"))
