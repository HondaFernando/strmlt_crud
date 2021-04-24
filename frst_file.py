import streamlit as st
import modules

# should cache data

cursor, connection = modules.connect()

st.title('CRUD SQL')
task = st.sidebar.selectbox('task', ['create', 'read', 'update', 'delete'])

if task == 'read':
    
    quant_constraint = st.sidebar.selectbox('filter', ['series', 'ano', 'score', 'classe'], index = 0)

    if quant_constraint == 'series':
        ret = modules.read_no_constraint(connection)
        ret

    elif quant_constraint == 'ano':

        ret = modules.read_year_constraint(connection)        
        ret 

    elif quant_constraint == 'score':
        ret = modules.read_score_constraint(connection)
        ret
    
    elif quant_constraint == 'classe':
        ret = modules.read_class_constraint(connection)
        ret

elif task == 'create':
    
     modules.create_row(cursor, connection)
    
elif task == 'delete':

    modules.delete_row(cursor, connection)

elif task == 'update':
   
    modules.update_row(cursor, connection)