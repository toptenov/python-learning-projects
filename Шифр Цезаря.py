eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def questions():
    """
    Ввод данных от пользователя.
    :return: is_encrypt (шифрование или дешифрование),
    is_russian (True/False),
    pace (шаг шифрования или дешифрования),
    text (текст от пользователя)
    """
    print("Привет, эта программа поможет зашифровать или расшифровать текст (Шифр Цезаря)")
    print("Если вы хотите зашифровать текст - введите 1. Если вы хотите расшифровать текст - введите 2")
    while True:
        is_encrypt = input()
        if is_encrypt in "1":
            is_encrypt = True
            break
        elif is_encrypt in "2":
            is_encrypt = False
            break
        else:
            print("Вы ввели неправильно. Зашифровать - 1, расшифровать - 2")

    print("Выберите язык ru или en")
    while True:
        language = input().lower()
        if language in "ru":
            is_russian = True
            break
        elif language in "en":
            is_russian = False
            break
        else:
            print("Вы ввели неправильно. Выберите язык ru или en")

    if is_russian:
        print("Введите шаг сдвига. Число от 1 до 31")
        while True:
            pace = input()
            if pace.isdigit():
                if 1 <= int(pace) <= 31:
                    pace = int(pace)
                    break
            else:
                print("Вы ввели неправильно. Введите шаг сдвига. Число от 1 до 31")
    else:
        print("Введите шаг сдвига. Число от 1 до 25")
        while True:
            pace = input()
            if pace.isdigit():
                if 1 <= int(pace) <= 25:
                    pace = int(pace)
                    break
            else:
                print("Вы ввели неправильно. Введите шаг сдвига. Число от 1 до 25")

    if is_encrypt:
        print("Введите текст, который нужно зашифровать")
        text = input()
    else:
        print("Введите шифр, который нужно расшифровать")
        text = input()

    return is_encrypt, is_russian, pace, text


def encrypt_decrypt(is_encrypt, is_russian, pace, text):
    """
    Функция шифрования / дешифрования.
    :param is_encrypt: Шифрование или дешифрование.
    :param is_russian: Русский или английский язык.
    :param pace: Шаг шифрования или дешифрования.
    :param text: Текст от пользователя
    :return: Результат шифрования или дешифрования
    """
    result = ""
    if is_russian:
        for i in text:
            if i.isalpha():
                if i.islower():
                    if is_encrypt:
                        if rus_lower_alphabet.index(i) + pace <= len(rus_lower_alphabet):
                            result += rus_lower_alphabet[rus_lower_alphabet.index(i) + pace]
                        else:
                            result += rus_lower_alphabet[rus_lower_alphabet.index(i) + pace - 32]
                    else:
                        if rus_lower_alphabet.index(i) - pace >= 0:
                            result += rus_lower_alphabet[rus_lower_alphabet.index(i) - pace]
                        else:
                            result += rus_lower_alphabet[rus_lower_alphabet.index(i) - pace + 32]
                else:
                    if is_encrypt:
                        if rus_upper_alphabet.index(i) + pace <= len(rus_upper_alphabet):
                            result += rus_upper_alphabet[rus_upper_alphabet.index(i) + pace]
                        else:
                            result += rus_upper_alphabet[rus_upper_alphabet.index(i) + pace - 32]
                    else:
                        if rus_upper_alphabet.index(i) - pace >= 0:
                            result += rus_upper_alphabet[rus_upper_alphabet.index(i) - pace]
                        else:
                            result += rus_upper_alphabet[rus_upper_alphabet.index(i) - pace + 32]
            else:
                result += i
    else:
        for i in text:
            if i.isalpha():
                if i.islower():
                    if is_encrypt:
                        if eng_lower_alphabet.index(i) + pace <= len(eng_lower_alphabet):
                            result += eng_lower_alphabet[eng_lower_alphabet.index(i) + pace]
                        else:
                            result += eng_lower_alphabet[eng_lower_alphabet.index(i) + pace - 26]
                    else:
                        if eng_lower_alphabet.index(i) - pace >= 0:
                            result += eng_lower_alphabet[eng_lower_alphabet.index(i) - pace]
                        else:
                            result += eng_lower_alphabet[eng_lower_alphabet.index(i) - pace + 26]
                else:
                    if is_encrypt:
                        if eng_upper_alphabet.index(i) + pace <= len(eng_upper_alphabet):
                            result += eng_upper_alphabet[eng_upper_alphabet.index(i) + pace]
                        else:
                            result += eng_upper_alphabet[eng_upper_alphabet.index(i) + pace - 26]
                    else:
                        if eng_upper_alphabet.index(i) - pace >= 0:
                            result += eng_upper_alphabet[eng_upper_alphabet.index(i) - pace]
                        else:
                            result += eng_upper_alphabet[eng_upper_alphabet.index(i) - pace + 26]
            else:
                result += i
    print(f"Результат: {result}")


def main():
    is_encrypt, is_russian, pace, text = questions()
    encrypt_decrypt(is_encrypt, is_russian, pace, text)


if __name__ == "__main__":
    main()
