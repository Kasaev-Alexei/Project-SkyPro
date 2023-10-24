def mask_user_card(name_card: str, user_card: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param user_card: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(user_card) == 16:
        return f"{name_card} {user_card[0:4]} {user_card[5:7]}** **** {user_card[-4:]}"
    else:
        return "Введен короткий или длинный номер карты"


def mask_user_account(name_account: str, user_account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param user_account: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    if len(user_account) == 20:
        return f"{name_account} **{user_account[-4:]}"
    else:
        return "Введен короткий или длинный номер счета"


def date_and_time(test):
    """
    Функция принимает на вход дату и время
    :param test: принимает дату и время
    :return: Дату в формате ДД.ММ.ГГ
    """
    return f"{test[8:10]}.{test[5:7]}.{test[0:4]}"


print(mask_user_card("Maestro", "1234567890123456"))
print(mask_user_account("Счет", "12345678901234567890"))
print(date_and_time("2018-07-11T02:26:18.671407"))
