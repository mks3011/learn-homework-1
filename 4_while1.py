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
    user_say = input('Как дела?')
    while user_say != 'Хорошо':
        user_say = input('Как дела?')

    """
    # v2
    key_word = 'Хорошо'
    while True:
        user_say = input('Как дела?')
        if key_word == user_say:
            break
    """

if __name__ == "__main__":
    hello_user()
