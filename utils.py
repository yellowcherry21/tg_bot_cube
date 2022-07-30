from telebot import types, TeleBot
import telebot
import time


with open("bot_token.txt","r") as bot_token_file:
    bot_token = bot_token_file.read()

bot = TeleBot(bot_token)


def playing(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    btn6 = types.KeyboardButton("6")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="ВЫБИРАЙ БЛЯ ЦИФРУ ЕБЛАН", reply_markup=markup)

    time.sleep(30)

    while True:
        result = throw_cube(message)
        bot.send_message(message.chat.id, str(result))
        time.sleep(15)


def save_user(user: types.User):
    with open("users.txt", "a", encoding="UTF-8") as users_file:
        users_file.write(str(user.id) + "," +
                         str(user.first_name)+"," + str(user.username)+"\n")


def throw_cube(message: types.Message) -> int:
    return bot.send_dice(chat_id=message.chat.id, emoji="🎲").dice.value
