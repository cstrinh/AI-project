# https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031
# https://discuss.streamlit.io/t/pay-wall-for-streamlit-content/19156/6
# https://medium.com/artificialis/how-to-add-user-authentication-on-your-streamlit-app-c7f50c085b9f
import streamlit as st
from streamlit_option_menu import option_menu

from Home import Home
from Learning import Learning
from Data import Data
from About import About


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 300px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 300px;
                margin-left: -300px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


with st.sidebar:

    page = option_menu("Main menu",
                       ['Home','Machine Learning', 'Data Exploration','About'],
                       icons=['house','book','graph-up','info-circle'],
                       styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "20px"}, 
                            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#0ba4e6"},
                            },
                        menu_icon="cast", default_index=1,
    )
    
    with st.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')
    st.markdown("### What's Inside a Smartphone?")
    st.video("https://www.youtube.com/watch?v=fCS8jGc3log")


if page == 'Home':
    Home()
    
if page == 'Machine Learning':
    Learning()

if page == 'Data Exploration':
    Data()

if page == 'About':
    About()
    
