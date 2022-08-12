from telebot import TeleBot
import psycopg2 as pg
import os
from urllib.parse import urlparse

GAME_OVER = "GAME OVER"
QUERIES = {"set_flag": '''UPDATE public."Availability" 
            SET flag = %s 
            WHERE id = %s''',
           "get_flag_by_id": """SELECT flag FROM public."Availability" WHERE id = %s""",
           "reg_chat": """INSERT INTO public."Availability"
                          VALUES (%s, false)"""
           }
GREETING = '''АЛЁ ЕБЛАНЫ ИГРА НАЧАЛАСЬ
ДЕЛАЕМ СТАВКИ
'''
CHOOSE_NUMBER = "ВЫБИРАЙ БЛЯ ЦИФРУ ЕБЛАН"
CUBE_RESULT_ALERT = "ВЫПАЛО"
IS_PREDICTION_GOING = True

DB_URL_PARSE = urlparse(os.environ.get('DATABASE_URL', None))
DB_USERNAME= DB_URL_PARSE.username
DB_PASSWORD= DB_URL_PARSE.password
DB_HOST = DB_URL_PARSE.hostname
DB_NAME = DB_URL_PARSE.path[1:]
DB_PORT = DB_URL_PARSE.port


def init_bot():
    # with open("bot_token.txt", "r") as bot_token_file:
    #bot_token = bot_token_file.read()
    bot_token = os.environ.get('BOT_TOKEN', None)
    return TeleBot(bot_token)


def get_db_connection():
    return pg.connect(
        dbname=DB_NAME,
        user = DB_USERNAME,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT
        )
    #return pg.connect(dbname='learn_db', user='postgres',
    #                 password='admin', host='localhost')
