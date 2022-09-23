
import streamlit as st
from PIL import Image


def About():

    st.title('Mobile Price Prediction')
    st.markdown("Cette application consiste à déterminer le prix d'un cellulaire à partir des caractéristiques choisis, ainsi à lancer un apprentissage IA sur le sujet.")
    st.markdown('Ce travail est réalisé par **Cong Son Trinh** dans le cours de **Programmation 2** de la Formation continue **"Big Data en Finance"** au **Collège de Rosemont.**')

    st.info('#### **Référence du travail:**')
    st.markdown('_**Source de données :** https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification_')
    st.markdown('_**Documentaire sur le téléphone :** https://en.wikipedia.org/wiki/Mobile_phone, https://www.phonandroid.com/smartphones-ados-top-bienfaits.html_')

    st.success('### **Mes remerciements au Prof. Alaidine pour ce cours!**')
   
    image = Image.open('img/merci.jpg')
    st.image(image)
