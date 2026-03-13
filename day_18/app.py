import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Native Charts")

# Generate some random data
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Display a line chart
st.subheader("Line Chart")
st.line_chart(df)

# Display an area chart
st.subheader("Area Chart")
st.area_chart(df)

# Display a bar chart
st.subheader("Bar Chart")
st.bar_chart(df)