import psycopg2
import pandas as pd
import streamlit as st

# ----------> CONNECT
def connect():
    
    connection = psycopg2.connect(database = 'strmlt_crud_db', user = 'postgres', password = '5432',
                              host = 'localhost')
    cursor = connection.cursor()
    
    return cursor, connection

# ----------> READ
def read_no_constraint(connection):

    series_filter = st.sidebar.multiselect('series', ['id', 'nome', 'nascimento', 'classe', 'score'], ['id', 'nome', 'nascimento', 'classe', 'score'])
    df = pd.read_sql('SELECT * FROM people;', connection)

    if df[series_filter].shape[1] == 0:
        return st.warning('no data')
    else:
        return df[series_filter]

def read_year_constraint(connection):
    
    # hard coded range
    year_range = st.sidebar.slider('year range', min_value = 1920, max_value = 2020, value = (2000, 2010))
    df = pd.read_sql('SELECT * FROM people', connection)

    df['aux'] = df['nascimento'].str.split('/')
    df['aux'] = df['aux'].apply(lambda x: x[2])
    df['aux'] = df['aux'].astype(int)

    df = df.loc[(df['aux'] >= year_range[0]) & (df['aux'] <= year_range[1])]
    df.drop('aux', axis = 1, inplace = True)

    return df

def read_score_constraint(connection):

    # hard coded range
    score_range = st.sidebar.slider('score range', min_value = 0, max_value = 100, value = (50, 75))
    df = pd.read_sql(f'SELECT * FROM people WHERE score >= {score_range[0]} and score <= {score_range[1]}', connection)

    return df

def read_class_constraint(connection):

    classe = st.sidebar.multiselect('classe', ['a', 'b', 'c', 'd', 'e'])

    if len(classe) == 1:
        df = pd.read_sql(f"SELECT * FROM people WHERE classe = '{classe[0]}'", connection)
        
        return df

    elif len(classe) > 1:
        df = pd.read_sql(f"SELECT * FROM people WHERE classe IN {tuple(classe)}", connection)

        return df

    else:
        return 'no data'

# ----------> CREATE
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

            st.success('feito')

        else:
            st.warning('algo deu errado')

# ----------> DELETE
def delete_row(cursor, connection):
    
    id_del_input = st.text_input('id para deletar')
    go_button = st.button('go')    

    if go_button:

        if len(id_del_input) > 0:
            string = f"DELETE FROM people WHERE id = {id_del_input}"
            cursor.execute(string)
            connection.commit()
            st.success('feito')

        else:
            st.warning('nao tem id')

# ----------> UPDATE
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
                st.success('feito')

            else:
                string = f"UPDATE people SET {feature} = {text_update} WHERE id = {target_id}"
                cursor.execute(string)
                connection.commit()
                st.success('feito')

        else:
            st.warning('algo deu errado')