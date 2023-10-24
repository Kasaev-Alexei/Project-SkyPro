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


print(mask_user_card("Maestro", "1234567890123456"))
print(mask_user_account("Счет", "12345678901234567890"))
