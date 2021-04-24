import streamlit as st
import modules

cursor, connection = modules.connect()

st.title('pagina')

df = modules.get_full_table(connection)
df