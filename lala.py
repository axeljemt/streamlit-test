import streamlit as st
import pandas as pd
import numpy as np
import sqlalchemy
import psycopg2

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

st.title('Uber pickups in NYC')




# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM table_1 limit 1;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.colument1} has a :{row.column2}:")