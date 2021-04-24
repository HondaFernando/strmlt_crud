import psycopg2
import pandas as pd

def connect():
    
    connection = psycopg2.connect(database = 'strmlt_crud_db', user = 'postgres', password = '5432',
                              host = 'localhost')
    cursor = connection.cursor()
    
    return cursor, connection

def get_full_table(connection):
    return pd.read_sql('SELECT * FROM people;', connection)