import streamlit as st
import pandas as pd
import numpy as np


# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM table1 limit 10;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.colument1} has a :{row.column2}:")

