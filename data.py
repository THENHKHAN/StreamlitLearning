import streamlit as st 
import pandas as pd
import numpy as np
import  datetime
from datetime import date
import  time


# lets creat a list and will make it a numpy arry of 2d
arr= [1,2,3,4,5,6,7,8]
nArr = np.array(arr) # making arr as numpy array as nArr 
ndArr = nArr.reshape((2,4)) #makin 2X3 matrix or 2D array 2 row 3 col
st.markdown("""
## Printing 2d list/array(numpy) 
like console:
""")
print(ndArr)
print(type(ndArr))
'''
[[1 2 3 4]
 [5 6 7 8]]
<class 'numpy.ndarray'>
'''
def display2DArrayOnStreamLit(ndArray) :
    st.markdown("""
                ## Dsiplaying 2D numpy array with Streamlit method (write)like df
                """)
    st.write(ndArray)
    st.markdown("""
                ### In Table format with table method
                """)
    st.table(ndArray)

def displayDictOnStreamLit(myDict) :
    st.markdown("### Dict In different form")


    st.markdown("##### 1-Through write method")
    st.write(myDict) #dsiplay in json fomrat but remember type will not json but format will on UI. check verifeid key
  
    st.markdown("##### 2-Through json method")
    st.json(myDict)

    st.markdown("##### 3-Through table method in table form")
    st.table(myDict)
    
def displayCSVOnStreamLit(df):
    st.markdown("## Display CSV data- Using dataframe method-with width&height")
    st.dataframe(df,width=500,height=500) # widht and height by default will be in px

display2DArrayOnStreamLit(ndArr)
# creating dictionary
dct = {
    "name":["harsh","Gupta"],
    "age":[21,32],
    "city":["noida","delhi"],
    "verified":True
}
displayDictOnStreamLit(dct)
# lets read csv and do operation and diplay on streamlit UI
df = pd.read_csv('./data/Salary_Data.csv')
print(pd.options.display.max_rows) #60
# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# print(df.head(8))
# print(df.dtypes)
'''displaying df through streamlit'''
displayCSVOnStreamLit(df)


# lets add checkbox and check, uncheck : checkbox("label") - this function add a checkbox with specified name
# and when click it return True and uncheck then false so this can be used with condional stuff
a = st.checkbox("check") 
st.write(a)
st.checkbox("1")
st.checkbox("2")

def getTodaysDate ():
    if st.checkbox("checkToGetTodaysDate") : 
        today = date.today()     
        st.write(today)

getTodaysDate()