from src.masks import mask_user_account, mask_user_card

check_name_account = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]


def chek_card_and_account(info: str) -> str:
    """
    Функция принимает на вход номер карты/счета и название карты/счета и проверяет их
    :param info : Номер для маскирования карты/счета и название карты/счета
    :return: название карты/счета и маску карты/счета
    """
    list_of_info = info.split()
    join_mask = " ".join(list_of_info[:-1])

    if len(mask_user_account(list_of_info[1])) == 20 or "счет" == list_of_info[0].lower():
        return f"{join_mask} {mask_user_account(list_of_info[1])}"
    elif len(list_of_info[-1]) == 16 and join_mask in check_name_account:
        return f"{join_mask} {mask_user_card(list_of_info[-1])}"
    else:
        return "Не верно введен номер карты/счета или название карты/счета"


def date_and_time(date: str) -> str:
    """
    Функция принимает на вход дату и время
    :param test: принимает дату и время
    :return: Дату в формате ДД.ММ.ГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(chek_card_and_account("Visa Platinum 1234567890123456"))
print(chek_card_and_account("Счет 12345678901234567890"))
print(date_and_time("2018-07-11T02:26:18.671407"))
