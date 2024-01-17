import streamlit as st
import pandas as pd
import pip 


pip.main(["install","openpyxl"])

st.title("JAJA CREDITOS ATORADOS EN PROCESO")
#df=pd.read_excel('PROCESOS_PIVOTE.xlsx')
f=pd.read_csv('PROCESOS_PIVOTE.csv')
st.write(df)