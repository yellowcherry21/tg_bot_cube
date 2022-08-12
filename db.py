from init import get_db_connection, QUERIES
from contextlib import closing


def set_flag(chat_id: int, flag: bool) -> None:
    con = get_db_connection()
    with closing(con), con, con.cursor() as cursor:
        cursor.execute(QUERIES['set_flag'], (flag, chat_id))


def get_flag_by_id(id: int) -> bool:
    con = get_db_connection()
    with closing(con), con, con.cursor() as cursor:
        cursor.execute(QUERIES['get_flag_by_id'], (id,))
        flag = cursor.fetchone()[0]
    return flag
