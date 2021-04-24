import psycopg2
import pandas as pd
import streamlit as st

def connect():
    
    connection = psycopg2.connect(database = 'strmlt_crud_db', user = 'postgres', password = '5432',
                              host = 'localhost')
    cursor = connection.cursor()
    
    return cursor, connection

def get_full_table(connection):
    return pd.read_sql('SELECT * FROM people;', connection)

def create_row(cursor, connection):

    id_input = st.text_input('id')
    nome_input = st.text_input('nome')
    nascimento_input = st.text_input('nascimento')
    classe_input = st.text_input('classe')
    score_input = st.text_input('score')
    
    go_button = st.button('go')
    
    if go_button:

        if len(id_input) > 0 and len(nome_input) > 0 and len(nascimento_input) > 0 and len(classe_input) > 0 and len(score_input) > 0:
            string = f"INSERT INTO people (id, nome, nascimento, classe, score) VALUES ({id_input}, '{nome_input}', '{nascimento_input}', '{classe_input}', {score_input})"
            
            cursor.execute(string)
            connection.commit()

            return 'criado'

        else:
            string = 'campos nao preenchidos'

            return string

def delete_row(cursor, connection):
    
    id_del_input = st.text_input('id para deletar')
    go_button = st.button('go')    

    if go_button:

        if len(id_del_input) > 0:
            string = f"DELETE FROM people WHERE id = {id_del_input}"
            cursor.execute(string)
            connection.commit()
            return 'deletado'

        else:
            return 'nao tem id'

def update_row(cursor, connection):

    df = pd.read_sql("SELECT id FROM people", connection)
    options = df['id'].tolist()

    target_id = st.sidebar.selectbox('id para atualizar', options)
    feature = st.sidebar.radio('coluna para atualizar', ['nome', 'nascimento', 'classe', 'score'])
    text_update = st.text_input('novo valor')
    go_button = st.button('go')

    if go_button:

        if len(str(target_id)) > 0 and len(text_update) > 0 and len(feature) > 0:
       
            if feature in ['nome', 'nascimento', 'classe']:
                string = f"UPDATE people SET {feature} = '{text_update}' WHERE id = {target_id}"
                cursor.execute(string)
                connection.commit()
                return 'atualizado'

            else:
                string = f"UPDATE people SET {feature} = {text_update} WHERE id = {target_id}"
                cursor.execute(string)
                connection.commit()
                return 'atualizado'

  