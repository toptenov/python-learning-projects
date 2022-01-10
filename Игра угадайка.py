import random

count_of_attempts = 0  # Количество попыток


def ask_to_guess():
    """
    Функция, получения начальных данных от пользователя.
    :return: Введенное пользователем число и верхняя граница допустимого случайного числа.
    """
    print("Добро пожаловать в числовую угадайку")
    print("Задача угадать число от 1 до n. Для начала введите n")
    n = input_n()
    print(f"Угадайте число от 1 до {n}")
    typed_number = type_valid_number()
    return typed_number, n


def generate_random_number(n):
    """
    Генерация случайного числа.
    :param n: Верхняя граница допустимого случайного числа.
    :return: Случайное число.
    """
    return random.randint(1, n)


def guessing(random_number, typed_number):
    """
    Функция попыток угадать число.
    :param random_number: Случайное число.
    :param typed_number: Введенное пользователем число
    :return:
    """
    wrong_answer = True
    while wrong_answer:
        if check(random_number, typed_number):
            return
        else:
            typed_number = type_valid_number()


def check(random_number, typed_number):
    """
    Проверка введенного числа.
    :param random_number: Случайное число.
    :param typed_number: Введенное пользователем число.
    :return: Угадал или нет (True/False).
    """
    global count_of_attempts
    if random_number < typed_number:
        count_of_attempts += 1
        print("Ваше число больше загаданного, попробуйте еще разок")
        return False
    elif random_number > typed_number:
        count_of_attempts += 1
        print("Ваше число меньше загаданного, попробуйте еще разок")
        return False
    else:
        count_of_attempts += 1
        print(f"Вы угадали число! Количество попыток: {count_of_attempts}. Поздравляем!")
        return True


def input_n():
    """
    Ввод верхней границы допустимого случайного числа.
    :return: Верхняя граница допустимого случайного числа.
    """
    n = input()
    while True:
        if n.isdigit() and int(n) > 0:
            return int(n)
        else:
            print("Вы ввели n неправильно. Введите n")
            n = input()


def type_valid_number():
    """
    Функция приема числа от пользователя.
    :return: Корректно введенное пользователем число.
    """
    while True:
        typed_number = input()
        if typed_number.isdigit() and 1 <= int(typed_number) <= 100:
            typed_number = int(typed_number)
            return typed_number
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")


def start_new_game():
    """
    Старт новой игры.
    :return:
    """
    print("Вы хотите начать новую игру? Введите Y или N")
    answer = input()
    while True:
        if answer.upper() in "Y":
            return True
        elif answer.upper() in "N":
            return False
        else:
            print("Вы хотите начать новую игру? Введите Y или N")
            answer = input()


def main():
    while True:
        global count_of_attempts
        typed_number, n = ask_to_guess()
        random_number = generate_random_number(n)
        guessing(random_number, typed_number)
        count_of_attempts = 0
        if start_new_game():
            continue
        else:
            break

    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


if __name__ == '__main__':
    main()
