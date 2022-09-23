import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Data():
    st.title('Descriptive Statistics & Visualization')
    st.markdown('#### Upload your data to explore')
    uploaded_file = st.file_uploader(" ")
    if uploaded_file:
        df = pd.read_csv(uploaded_file,index_col=False)
            
        st.header("View General of All Data")
        with st.expander('View Data'):
            st.table(df.head(10))

### Descriptive statistics with PANDAS
        with st.expander('View Descriptive statistics for all features'):
            st.dataframe(df.describe())

### Choose features to explore:
        st.header("Choose features to explore in details")
        features = []
        features = df.columns.values.tolist()
        var = st.selectbox(' ', features)
        st.subheader("_• Descriptive Statistics for : %s_" %var)

### Descriptive statistics with NUMPY    
        medianv =  np.median(np.array(df[var]))
        maxv =  np.max(np.array(df[var]))
        minv =  np.min(np.array(df[var]))
        meanv =  np.mean(np.array(df[var]))
        stdv = np.std(np.array(df[var]))
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(pd.DataFrame({'Max':[maxv], 'Min':[minv], 'Mean':[meanv], 'Median':[medianv], 'Standard Deviation':[stdv] }))
        

### First visualization: Distribution
        st.subheader("_• Distribution for : %s_" %var)   
        x = dict(df[var].value_counts())
        data = dict(x)
        values = list(data.keys())
        count = list(data.values())

        fig = plt.figure(figsize = (12, 6))

        plt.bar(values, count)
        plt.xlabel("%s" %var)
        plt.ylabel("Count")    
        #plt.hist(count)
        plt.title("Number of occurence by feature : %s" %var)
        st.pyplot(fig)


        var2 = st.selectbox('Choose another feature to see their correlation', features)
        
### Second visualization: Correlation
        st.subheader('_• Correlation between %s & %s in scatter plot_' %(var,var2))

        y = np.array(df[var])
        z = np.array(df[var2])   
        
        fig = plt.figure(figsize=(10, 4))
        plt.xlabel("%s" %var)
        plt.ylabel("%s" %var2) 
        plt.scatter(y, z)
        st.pyplot(fig)
     