import streamlit as st
import pandas as pd

# Title of the web app
st.title('CSV File Upload and Analysis')

# Section for uploading the first type of CSV file
st.header("Upload CSV profile")
uploaded_file1 = st.file_uploader("Choose the first CSV file", type="csv", key="file1")

if uploaded_file1 is not None:
    try:
        df1 = pd.read_csv(uploaded_file1, on_bad_lines='skip')
        st.write("Here is the data from the uploaded CSV file Type 1:")
        st.dataframe(df1)

        # Display basic statistics about the data
        st.write("### Basic Statistics")
        st.write(df1.describe())

        # Show first 5 rows of the data
        st.write("### Data Preview (First 5 Rows)")
        st.write(df1.head())

        # Allow user to download the dataframe as a CSV file
        st.write("### Download Data")
        csv1 = df1.to_csv(index=False)
        st.download_button(
            label="Download File Type 1 as CSV",
            data=csv1,
            file_name='analyzed_data_type_1.csv',
            mime='text/csv',
        )
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV file Type 1: {e}")

# Section for uploading the second type of CSV file
st.header("Upload CSV Messages file")
uploaded_file2 = st.file_uploader("Choose the second CSV file", type="csv", key="file2")

if uploaded_file2 is not None:
    try:
        df2 = pd.read_csv(uploaded_file2, on_bad_lines='skip')
        st.write("Here is the data from the uploaded CSV file Type 2:")
        st.dataframe(df2)

        # Display basic statistics about the data
        st.write("### Basic Statistics")
        st.write(df2.describe())

        # Show first 5 rows of the data
        st.write("### Data Preview (First 5 Rows)")
        st.write(df2.head())

        # Allow user to download the dataframe as a CSV file
        st.write("### Download Data")
        csv2 = df2.to_csv(index=False)
        st.download_button(
            label="Download File Type 2 as CSV",
            data=csv2,
            file_name='analyzed_data_type_2.csv',
            mime='text/csv',
        )
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV file Type 2: {e}")

# Section for uploading the third type of CSV file
st.header("Upload Connection csv")
uploaded_file3 = st.file_uploader("Choose the third CSV file", type="csv", key="file3")

if uploaded_file3 is not None:
    try:
        df3 = pd.read_csv(uploaded_file3, on_bad_lines='skip')
        st.write("Here is the data from the uploaded CSV file Type 3:")
        st.dataframe(df3)

        # Display basic statistics about the data
        st.write("### Basic Statistics")
        st.write(df3.describe())

        # Show first 5 rows of the data
        st.write("### Data Preview (First 5 Rows)")
        st.write(df3.head())

        # Allow user to download the dataframe as a CSV file
        st.write("### Download Data")
        csv3 = df3.to_csv(index=False)
        st.download_button(
            label="Download File Type 3 as CSV",
            data=csv3,
            file_name='analyzed_data_type_3.csv',
            mime='text/csv',
        )
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV file Type 3: {e}")
