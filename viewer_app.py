## Data View App for Interactive Insight Project

import pandas as pd
import streamlit as st
import plotly.express as px



# Page Setup
st.set_page_config(page_title='📊 Data Viewer App', layout='wide')

# App Title
st.title('📉 CSV Data Viewer with Charts Insight')
st.markdown('Upload a CSV file to explore data and generate interactive Insights.')

# File uploader
uploaded_file = st.file_uploader('Select a CSV file', type='csv')

if uploaded_file is not None:
    # ✅ Correct usage: pass uploaded_file, not a string
    df = pd.read_csv(uploaded_file)
    st.success('✅ File uploaded successfully')

    # Show a preview
    st.subheader('🐼 Data Preview')
    st.dataframe(df.head())

    # Column selection
    all_columns = df.columns.tolist()
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    st.subheader('🐱 Chart Settings')
    chart_type = st.radio('Choose chart type', ['Bar Chart', 'Pie Chart', 'Line Chart'])

    x_axis = st.selectbox('Select x-axis (category or numeric)', all_columns)
    y_axis = st.selectbox('Select y-axis (numeric)', numeric_columns)

    # Chart display
    if chart_type == 'Bar Chart':
        st.subheader('📉 Bar Chart')
        fig = px.bar(df, x=x_axis, y=y_axis, color=x_axis)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'Pie Chart':
        st.subheader('😬 Pie Chart')
        fig = px.pie(df, names=x_axis, values=y_axis, title=f'{y_axis} by {x_axis}')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'Line Chart':
        st.subheader('📈 Line Chart')
        fig = px.line(df, x=x_axis, y=y_axis, title=f'{y_axis} over {x_axis}')
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info('😱 Upload a CSV file to begin')
