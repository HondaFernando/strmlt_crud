def connect():
    
    connection = psycopg2.connect(database = 'strmlt_crud_db', user = 'postgres', password = '5432',
                              host = 'localhost')
    cursor = connection.cursor()
    
    return cursor