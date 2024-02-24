"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
# import settings
import ephem


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
today = date.today()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    print("Нажат /start")
    # print(update)
    # print(context)
    username = update.message.chat.username
    # print(username)
    update.message.reply_text(f"Привет {username}")


def talk_to_me(update, context):
    text = update.message.text
    # print(text)
    update.message.reply_text(text)


def planets(update, context):
    planet_name = update.message.text.split()[1]
    print(planet_name)
    if planet_name == 'Neptune':
        n = ephem.constellation(ephem.Neptune(today))
        update.message.reply_text(f'Сегодня планета {planet_name} находится в созвездии {n}')
    elif planet_name == 'Mars':
        m = ephem.constellation(ephem.Mars(today))
        update.message.reply_text(f'Сегодня планета {planet_name} находится в созвездии {m}')
    elif planet_name == 'Sun':
        s = ephem.constellation(ephem.Sun(today))
        update.message.reply_text(f'Сегодня планета {planet_name} находится в созвездии {s}')
    else:
        update.message.reply_text(f'Ушел искать планету {planet_name}')


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
