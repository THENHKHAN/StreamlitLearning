import streamlit as st

st.title("hello Noor")
st.header("This is header on streamlit UI")
st.text("This is text, you can't modify its format")

st.markdown(""" 
            
# h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:<br>

**bold**
_italics_ <br>
:smiley:<br>
:smile:
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)