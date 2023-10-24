import streamlit as st
from PIL import Image
import model



st.sidebar.title("Menu")
page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'Model'])


if page == 'Home Page':
    col1, col2, col3 = st.columns(3)
    img = Image.open('hacktiv8-1.png')
    with col2:
        st.image(img, width=200)
    st.header('Welcome to Risk Detector Credit Card')
    st.subheader('Please Select Menu On Side Bar')
    with st.expander('Explanation'):
            st.markdown('An application that detects a customer having a bad risk or a good risk and groups the customer who belongs to the bad risk to facilitate the handling of the customer')
    img1 = Image.open('Square-1200x1200px.jpg')
    st.image(img1)




else:
    model.run()



