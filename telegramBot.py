# import telebot
# from telebot import apihelper
# import requests
#
# bot = telebot.TeleBot("833239097:AAFPPkwv5lOIroe4GM9zZl5xGEd1eDdeaSo")
#
# ip = '198.50.217.202'
# port = '1080'
# apihelper.proxy = {
#   'https': 'socks5://{}:{}@{}:{}'.format(ip, port)
# }
#
# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     bot.reply_to(message, message.text)
#
#
# bot.polling(none_stop=True)

import telebot
from telebot import apihelper

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

# token = '833239097:AAFPPkwv5lOIroe4GM9zZl5xGEd1eDdeaSo'
login = 0
password = 0
ip = 0
port = 0

apihelper.proxy = {
    'https': 'socks5://login:password@ip:port'
    }

bot = telebot.TeleBot('833239097:AAFPPkwv5lOIroe4GM9zZl5xGEd1eDdeaSo')


@bot.message_handler()
def handle(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)