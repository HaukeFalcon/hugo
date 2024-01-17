import streamlit as st
import pandas as pd
import pip 


pip.main(["install","openpyxl"])

st.title("CREDITOS ATORADOS EN PROCESO")

df=pd.read_excel('PROCESOS_PIVOTE.xlsx')

st.write(df)