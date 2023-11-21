import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy


# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM table_1 limit 1;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.colument1} has a :{row.column2}:")

