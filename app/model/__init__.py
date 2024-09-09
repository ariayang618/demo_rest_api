import sqlite3

from common import logger, db_file

class BaseModel:

    @classmethod
    def fetch(cls, sql):
        try:
            with sqlite3.connect(db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows, ''
        except Exception as e:
            logger.error(e_ := f'fail to query sqlite: {e}')
            return [], e_

    @classmethod
    def sql_insert(cls, sql):
        try:
            with sqlite3.connect(db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return cursor.lastrowid, ''
        except Exception as e:
            logger.error(e_ := f'fail to execute sql: {e}')
            return 0, e_