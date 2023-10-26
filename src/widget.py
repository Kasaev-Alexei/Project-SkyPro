from src.masks import mask_user_account, mask_user_card


def chek_card_and_account(info: str) -> str:
    """
    Функция принимает на вход номер карты/счета и название карты/счета и проверяет их
    :param name_card: Номер для маскирования карты/счета и название карты/счета
    :return: название карты/счета и маску карты/счета
    """
    list_of_info = info.split()
    payment_type = list_of_info[0]
    payment_number = list_of_info[1]

    if payment_type == "Maestro" and len(payment_number) == 16:
        return f"{payment_type} {mask_user_card(payment_number)}"
    elif payment_type == "Счет" and len(payment_number) == 20:
        return f"{payment_type} {mask_user_account(payment_number)}"
    return f"Не верно введен номер карты или название карты"


def date_and_time(date: str) -> str:
    """
    Функция принимает на вход дату и время
    :param test: принимает дату и время
    :return: Дату в формате ДД.ММ.ГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(chek_card_and_account("Maestro 1234567890123456"))
print(chek_card_and_account("Счет 12345678901234567890"))
print(date_and_time("2018-07-11T02:26:18.671407"))
