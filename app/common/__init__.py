import os
import logging
import sqlite3
from fastapi import HTTPException

log_format = '%(asctime)s %(filename)-18s %(funcName)-18s:%(lineno)-4s %(levelname)-8s %(message)s'
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger('api_demo')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
db_file = os.getenv('sqlite_file', 'api_demo.db')


async def create_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    with open('database/main.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    # logger.debug(sql_script)
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    logger.info('database is ready')


def abort_with_error(message: str, status_code: int):
    raise HTTPException(status_code, detail={'error': message})