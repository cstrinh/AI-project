
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as metrics
import pickle
from joblib import dump, load

def Learning():
    st.title('Machine Learning')
    st.markdown('##### Upload your data to see the results of the machine learning model')
    
# Create uploaded_file zone:
    uploaded_file = st.file_uploader(" ")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,index_col=False)
        #st.dataframe(df)

# Show data            
        st.subheader("Data preview")
        with st.expander('Click to View Data'):
            st.table(df.head(10))
         
        features = []
        features = df.columns.values.tolist()
        
        st.subheader("Select features to apply Machine Learning") 
        inputF = st.multiselect("Features to Exclude of the model",features)

       
# Machine learning
        if st.button('Start IA Engine'):
            X1 = df.drop('price_range', axis = 1)
            X = X1.drop(inputF, axis=1)
            y = df['price_range']

            train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=7)
            st.success('_Create corpus of test/training - status : Done_')
            model = RandomForestClassifier(random_state=7, n_estimators=100)
            model.fit(train_X, train_y)
            
# Pickle the system parametres after training
            dump(model, 'bin\SysParam.joblib')
            LP = 'bin\SysParam.joblib'
            st.download_button('Download LEARNING parametres', LP)
            
# Download SysParam.joblib locally
            st.markdown('### Model results:')
            pred_y = model.predict(val_X)

# Show the results:
            accuracy = metrics.accuracy_score(val_y, pred_y)
            st.info("**Accuracy**: %f" %accuracy)

            confusion = metrics.confusion_matrix(val_y, pred_y)
            x= pd.DataFrame(confusion)
            st.info("**Confusion matrix:**")
            st.dataframe(x)

            st.info(f"\n**Normalized confusion matrix:**")
            for row in confusion:
                st.text(row / row.sum())
            
            