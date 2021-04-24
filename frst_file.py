# import streamlit as st
import modules

cursor, connection = modules.connect()

print(modules.get_full_table(connection))