from _thread import start_new_thread
import locale
import utils
from telebot.types import Message
from telebot import TeleBot
import os

locale.setlocale(locale.LC_ALL)

#with open("bot_token.txt", "r") as bot_token_file:
    #bot_token = bot_token_file.read()

bot_token = os.environ.get('BOT_TOKEN', None)

bot = TeleBot(bot_token)
greeting = '''АЛЁ ЕБЛАНЫ ИГРА НАЧАЛАСЬ
ДЕЛАЕМ СТАВКИ
'''
is_predictions_going = True


@bot.message_handler(commands=["start"])
def start_func(message: Message):
    bot.send_message(message.chat.id, greeting)
    start_new_thread(utils.playing, (message,))


@bot.message_handler(commands=["reg"])
def register_user(message: Message):
    utils.save_user(message.from_user)
    bot.send_message(message.chat.id, f"Зарегал тебя {message.from_user.username}")


@bot.message_handler(commands=["cube"])
def throw_cube(message: Message):
    dice_value = bot.send_dice(chat_id=message.chat.id, emoji="🎲").dice.value
    bot.send_message(message.chat.id, str(dice_value))


@bot.message_handler(func=lambda message: message.text in ["1", "2", "3", "4", "5", "6"], content_types=['text'])
def create_prediction(message: Message):
    if is_predictions_going:
        bot.send_message(message.chat.id, f"Записал {message.from_user.username} ты поставил на " + message.text)
        utils.save_prediction(message)
    else:
        bot.send_message(message.chat.id, "КУДЫ ПАЛЬЦЕМ ТЫЧЕШЬ? Я ЩАС ТЕБЕ ЕГО В ЖОПУ ЗАСУНУ")


@bot.message_handler(commands=["time"])
def create_prediction(message: Message):
    bot.send_message(message.chat.id, f"Сейчас {message.date}")


bot.infinity_polling()
