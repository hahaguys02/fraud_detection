import joblib
import streamlit as st
import pandas as pd
import numpy as np
import os

model = os.path.join(os.path.dirname(__file__), 'fraud_detection_model.pkl')

st.title("FRAUD DETECTION APP")

st.markdown('please provide the following transaction details:')

st.divider()

Transaction_Type=st.selectbox('Transaction Type',['PAYMENT','TRANSFER','CASH_OUT','DEBIT','CASH_IN'],key='type')
Amount=st.number_input('Transaction Amount',min_value=0.0,key='amount')
Old_Balance_Org=st.number_input('Old Balance of Origin Account',min_value=0.0,key='oldbalanceorg')
New_Balance_Org=st.number_input('New Balance of Origin Account',min_value=0.0,key='newbalanceorg')
Old_Balance_Dest=st.number_input('Old Balance of Destination Account',min_value=0.0,key='oldbalancedest')
New_Balance_Dest=st.number_input('New Balance of Destination Account',min_value=0.0,key='newbalancedest')

if st.button('PREDICT'):
    input_data=pd.DataFrame([[Transaction_Type, Amount, Old_Balance_Org, New_Balance_Org, Old_Balance_Dest, New_Balance_Dest]],
                 columns=['type', 'amount','oldbalanceOrg', 'newbalanceOrig','oldbalanceDest', 'newbalanceDest'])

    Prediction=model.predict(input_data)[0]

    if Prediction == 1:
        st.error("The Transaction is FRAUDULENT")
    else:

        st.success("The Transaction is NOT FRAUDULENT")
