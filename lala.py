import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy

st.title('Uber pickups in NYC')

# Initialize connection.
conn = st.connection("postgresql", type="sql")

st.title('Uber pickups in NYC2')
# Perform query.
#df = conn.query('SELECT * FROM table_1 limit 1;', ttl="10m")

st.title('Uber pickups in NYC3')

# Print results.
#for row in df.itertuples():
    #st.write(f"{row.colument1} has a :{row.column2}:")
    
st.title('Uber pickups in NYC4')

