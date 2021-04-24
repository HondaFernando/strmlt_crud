import streamlit as st
import modules

cursor, connection = modules.connect()

st.title('pagina')
task = st.sidebar.selectbox('task', ['create', 'read', 'update', 'delete'])

if task == 'read':
    
    series_filter = st.sidebar.multiselect('filter', ['id', 'nome', 'nascimento', 'classe', 'score'])
    df = modules.get_full_table(connection)

    df[series_filter]

elif task == 'create':
    
    main_wndw = ''
    ret = modules.create_row(cursor, connection)
    if ret == None:
        main_wndw

    else:
        ret

elif task == 'delete':

    main_wndw = ''
    ret = modules.delete_row(cursor, connection)
    if ret == None:
        main_wndw
    else:
        ret

elif task == 'update':

    main_wndw = ''    
    ret = modules.update_row(cursor, connection)
    if ret == None:
        main_wndw
    else:
        ret
 