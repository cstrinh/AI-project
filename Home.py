
import streamlit as st
from PIL import Image
from joblib import dump, load
import numpy as np
import pandas as pd


def Home():
    
    st.title('MOBILE PRICE PREDICTION')
    image = Image.open('img/phone.jpg')
    st.image(image,width = 700)
    
    st.markdown('### Please choose your mobile features:')

# Form with columns of features    
    with st.form('myform'):
        col1, col2, col3 = st.columns(3)

        with col1:
            # TODO make values dynamic
            battery_power = st.slider('Battery Power mAh', 500, 2000)
            clock_speed = st.slider('CPU Speed', 0.5, 3.0)
            fc = st.slider('Front Camera mega pixels', 0, 19)
            int_memory = st.slider('Internal Memory (GB)', 2, 64)
            m_dep = st.slider('Mobile Depth in cm', 0.1, 1.0)
            mobile_wt = st.slider('Mobile Weight in gram', 80, 200)        
            n_cores = st.slider('Number of cores', 1, 8)  

        with col2:
            pc = st.slider('Primary Camera mega pixels', 0, 20)
            px_height = st.slider('Pixel Resolution Height', 0, 2000)
            px_width = st.slider('Pixel Resolution Width', 500, 2000)       
            ram = st.slider('RAM(MB)', 256, 4000)
            sc_h = st.slider('Screen Height cm', 5, 19)
            sc_w = st.slider('Screen Width cm', 0, 18)
            talk_time = st.slider('Talk time (hour)', 2, 20)        
        
        with col3:
            three_g = st.radio('3G', ['Yes','No'])
            four_g = st.radio('4G', ['Yes','No'])
            dual_sim = st.radio('Dual Sim', ['Yes','No'])
            touch_screen = st.radio('Touch Screen', ['Yes','No'])
            wifi = st.radio('Wifi', ['Yes','No'])
            blue = st.radio('Bluetooth', ['Yes','No'])       
        submit_button = st.form_submit_button("Submit")

    if submit_button:

# Prediction in offline mode
        model2 = load('bin\SysParam.joblib')

# Append values        
        mobile  = []
        mobile.append(battery_power)

        if blue == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0) 
        
        mobile.append(clock_speed)
        
        if dual_sim == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0) 
        
        mobile.append(fc)
        
        if four_g == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0)        
        
        mobile.append(int_memory)
        mobile.append(m_dep)
        mobile.append(mobile_wt)
        mobile.append(n_cores)
        mobile.append(pc)
        mobile.append(px_height)
        mobile.append(px_width)
        mobile.append(ram)
        mobile.append(sc_h)
        mobile.append(sc_w)
        mobile.append(talk_time)
        
        if three_g == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0)
        
        if touch_screen == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0)
        
        if wifi == 'Yes':
            mobile.append(1)
        else:
            mobile.append(0)
            
# Prediction for the chosen features
        prediction = model2.predict([mobile])
        price = prediction[0]

# Show the results:
        st.subheader(' →  The mobile PRICE RANGE for your chosen features is :   %d' %price)
 
# Show the note: 
        st.warning('⚠️  **Price Range Note**:')
        
        note = pd.DataFrame({   '0': ['Low Cost'],                    
                                '1': ['Medium Cost'],
                                '2': ['High Cost'],
                                '3': ['Very High Cost']                    
                                })

        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        
        st.table(note)
        
        