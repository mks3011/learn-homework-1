"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    """
    Замените pass на ваш код
    """
    """
    # v1
    user_say = input('Как дела?').capitalize()
    while user_say != 'Хорошо':
        user_say = input('Как дела?')


    # v2
    key_word = 'Хорошо'
    while True:
        user_say = input('Как дела?').capitalize()
        if key_word == user_say:
            break
    """
    # v3
    while True:
        user_say = input('Как дела?').capitalize()
        if user_say == 'Хорошо':
            break



if __name__ == "__main__":
    hello_user()
