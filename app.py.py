import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "BTC": [16000, 16500, 17000],
    "OIL": [70, 72, 75]
}

df = pd.DataFrame(data)

st.write("### Data Table")
st.dataframe(df)

st.write("### Chart")
st.line_chart(df.set_index("Date"))