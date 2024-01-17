import streamlit as st
import pandas as pd
import pip 


pip.main(["install","openpyxl"])

st.title("FUNNEL ACTIVACASH 2.0 :sunglasses:")
#df=pd.read_excel('PROCESOS_PIVOTE.xlsx')

#df_2=pd.read_csv('APROBADOS.csv')
#st.write(df_2)

st.markdown(f':cry:Estos socios estan caidos en el proceso:') 

df=pd.read_csv('PROCESOS_PIVOTE.csv')
st.write(df)

#st.markdown(f'*Resultados Disponibles:{numero_resultados}*') 


st.markdown(f'Estos socios si terminaron el proceso jajaja:') 


df2=pd.read_csv('APROBADOS.csv')
st.write(df2)