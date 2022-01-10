from random import randint

DIGITS = "23456789"
LOWERCASE_LETTERS = "abcdefghjkmnpqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKMNPQRSTUVWXYZ"
PUNCTUATION = "!/#$%&*+-=?@^_"
AMBIGUOUS_SYMBOLS = "il1Lo0O"


def configuration():
    """
    Функция, в которой пользователь определяет конфигурацию генерируемого пароля.
    :return:
    """
    chars = ""  # Список допустимых символов в пароле

    print("Добро пожаловать в генератор безопасных паролей")

    print("Введите количество паролей для генерации:")
    quantity = int(input())

    print("Введите длину пароля:")
    length = int(input())

    print("Пароль может содержать цифры? Введите Y или N:")
    while True:
        include_digits = input().lower()
        if include_digits in "y":
            chars += DIGITS
            break
        elif include_digits in "n":
            break
        else:
            print("Вы ввели неправильно. Пароль может содержать цифры? Введите Y или N:")

    print("Пароль может содержать прописные буквы? Введите Y или N:")
    while True:
        include_upper = input().lower()
        if include_upper in "y":
            chars += UPPERCASE_LETTERS
            break
        elif include_upper in "n":
            break
        else:
            print("Вы ввели неправильно. Пароль может содержать прописные буквы? Введите Y или N")

    print("Пароль может содержать строчные буквы? Введите Y или N")
    while True:
        include_lower = input().lower()
        if include_lower in "y":
            chars += LOWERCASE_LETTERS
            break
        elif include_lower in "n":
            break
        else:
            print("Вы ввели неправильно. Пароль может содержать строчные буквы? Введите Y или N:")

    print("Пароль может содержать символы пунктуации !#$%&*+-=?@^_? Введите Y или N:")
    while True:
        include_symbols = input().lower()
        if include_symbols in "y":
            chars += PUNCTUATION
            break
        elif include_symbols in "n":
            break
        else:
            print("Вы ввели неправильно. Пароль может содержать символы пунктуации !#$%&*+-=?@^_? Введите Y или N:")

    print("Пароль может содержать неоднозначные символы il1Lo0O? Введите Y или N:")
    while True:
        include_ambiguous_symbols = input().lower()
        if include_ambiguous_symbols in "y":
            chars += AMBIGUOUS_SYMBOLS
            break
        elif include_ambiguous_symbols in "n":
            break
        else:
            print("Вы ввели неправильно. Пароль может содержать неоднозначные символы il1Lo0O? Введите Y или N:")

    return list(chars), quantity, length


def generate_passwords(chars, quantity, length):
    """
    Функция генерации случайного пароля.
    :param chars: Допустимые в пароле символы.
    :param quantity: Количество генерируемых паролей.
    :param length: Длина пароля.
    """
    for i in range(quantity):
        password = ""
        for j in range(length):
            password += chars[randint(0, len(chars) - 1)]
        print(f"Пароль: №{i + 1}: {password}")


def main():
    chars, quantity, length = configuration()
    generate_passwords(chars, quantity, length)


if __name__ == "__main__":
    main()
