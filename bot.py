import os

import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'Hello, ' + f'<b>{message.chat.first_name} {message.chat.last_name}</b>', parse_mode='html')




bot.polling(none_stop=True)
