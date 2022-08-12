from _thread import start_new_thread
from db import set_flag
import locale
import utils
from telebot.types import Message
from init import GREETING, init_bot, IS_PREDICTION_GOING

locale.setlocale(locale.LC_ALL)

bot = init_bot()


@bot.message_handler(commands=["start"])
def start_func(message: Message):
    try:
        start_new_thread(utils.playing, (message,))
    except:
        set_flag(message.chat.id, False)


@bot.message_handler(commands=["reg"])
def register_user(message: Message):
    utils.save_user(message.from_user)
    bot.send_message(
        message.chat.id, f"Зарегал тебя {message.from_user.username}")


@bot.message_handler(commands=["cube"])
def throw_cube(message: Message):
    dice_value = bot.send_dice(chat_id=message.chat.id, emoji="🎲").dice.value
    bot.send_message(message.chat.id, str(dice_value))


@bot.message_handler(func=lambda message: message.text in ["1", "2", "3", "4", "5", "6"], content_types=['text'])
def create_prediction(message: Message):
    if IS_PREDICTION_GOING:
        bot.send_message(
            message.chat.id, f"Записал {message.from_user.username} ты поставил на " + message.text)
        utils.save_prediction(message)
    else:
        bot.send_message(
            message.chat.id, "КУДЫ ПАЛЬЦЕМ ТЫЧЕШЬ? Я ЩАС ТЕБЕ ЕГО В ЖОПУ ЗАСУНУ")


@bot.message_handler(commands=["time"])
def create_prediction(message: Message):
    bot.send_message(message.chat.id, f"Сейчас {message.date}")
    bot.send_message(message.chat.id, f"Сейчас {message.chat.id}")


bot.infinity_polling()
