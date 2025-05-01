import mysql.connector
import logging
from datetime import datetime

formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def tables_check(host_name: str, user_name: str, password_name: str, database_name: str):
    tables = ['saved_news', 'news_source_api_url']
    cnx = mysql.connector.connect(host=host_name, user=user_name, password=password_name,database=database_name)
    cursor = cnx.cursor()
    cursor.execute(f"SELECT Table_name as TablesName from information_schema.tables where table_schema = '*_news'")
    tables_name_db = cursor.fetchall()
    cursor.close()
    for table in tables:
        print(table, str(tables_name_db))
        if table not in str(tables_name_db):
            table_create(host_name,user_name,password_name,database_name,table)
    cnx.close()

def read_file_sql(path_file):
    read_sql = open(f'{path_file}', 'r')
    sql_file = read_sql.read()
    read_sql.close()
    return sql_file

def table_create(host_name: str, user_name: str, password_name: str, database_name: str,table: str):
    logger.info(host_name, user_name, password_name, database_name, table)
    logger.info("host_name: %s user_name: %s database_name: %s", host_name, user_name, database_name)
    """table_create(host, user, password, database, raise_exception)
    create connection to db using input parametrs
    create cursor
    create str to execute sql 
    insert str to cursor and commit
    close cursor and close connection
    if exception print DB error with error message and time
    """
    try:
        cnx = mysql.connector.connect(host=host_name, user=user_name, password=password_name,
                                      database=database_name)
        cursor = cnx.cursor()
        cursor.execute(read_file_sql(f'sql/create_table_{table}.sql'))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except Exception as e:
        print("DB error", datetime.now(), e)
        return False

tables_check('*.beget.tech','*_news','n3w5_c0ll3ctor','*_news')