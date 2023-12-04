import streamlit as st
import pandas as pd
from pandasql import sqldf


st.set_page_config(page_title="NHKHAN_streamLit", layout="wide")
st.header(":red[NHKHAN]: CSV File Upload and Query like SQL ", divider='rainbow')

# Here file name will be the table name (without extension).



def doQueryOnCSVPandasql(df,table): # working good
    queryBoxForQuery = st.text_area("Enter Query: ")
    btn = st.button("Submit")
    env = {table : df} # here making the df dataframe variable to table name(file name).That's how we use 2nd param of sqldf() function.
    if btn:
        result = sqldf(queryBoxForQuery,env)
        st.dataframe(result ,height=768)



def csvUploadAndReturnDf (): # working Good
    # File upload section
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        st.write(f"file name: {(uploaded_file.name.removesuffix('.csv'))}")
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        fileName = uploaded_file.name.removesuffix('.csv')
        # Display the DataFrame
        st.write("Original DataFrame:")
        # st.write(df)
        return True , df , fileName
    else:
        st.warning("file not upoaded yet!")
        return False, pd.DataFrame(), ""

uploaded , df, fileName = csvUploadAndReturnDf()
if uploaded:
    st.write(df)
    doQueryOnCSVPandasql(df,fileName)