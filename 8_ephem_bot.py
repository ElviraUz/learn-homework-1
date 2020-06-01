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
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ephem import constellation


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me( , update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def constellation_planet (bot,update):
  platent_u = "/planet Mars"
  planet = platent_u.split()[1].capitalize()

  if planet=="Mars":
    search_planet = ephem.Mars('2020/05/26')
    ephem.constellation(search_planet)

def main():
    mybot = Updater("1194195192:AAGKl_omijTQf_27flOlb1oA21T1uTpwQBo", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler(("planet",constellation_planet))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
