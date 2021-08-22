import streamlit as st
import numpy as np
import pandas as pd

# Add a title
st.title('My first app__')
# Add some text
st.text('Streamlit is great')

st.dataframe(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# lineplot
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# checkbox
if st.checkbox('Show dataframe'):
    st.dataframe(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)

# select box
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

column = st.selectbox(
    'What column to you want to display',
     df.columns)

st.line_chart(df[column])

# multi-select
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

columns = st.multiselect(
    label='What column to you want to display', options=df.columns)

st.line_chart(df[columns])

# slider
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

## slider-range
x = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Range values:', x)

# 