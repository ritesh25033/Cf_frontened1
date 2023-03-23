import streamlit as st

st.title('CF Recommender System')

st.checkbox('Graph')
st.checkbox('Greedy')
st.checkbox('Dynamic Programming')
st.checkbox('Array')
st.checkbox('String')

st.text_input('Rating')

st.button('Submit')




# option = st.selectbox(
# 'How would you like to be contacted?',
# ('Email','Home phone', 'Mobile phone'))