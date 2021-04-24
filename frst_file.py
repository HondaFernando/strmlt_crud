# import streamlit as st
import pandas as pd 
import psycopg2

import modules

cursor, connection = modules.connect()

print(modules.get_full_table(connection))