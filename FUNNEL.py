import streamlit as st
import pandas as pd
import pip 


pip.main(["install","matplotlib"])

st.title("FUNNEL ACTIVACASH 2.0 :sunglasses:")
#df=pd.read_excel('PROCESOS_PIVOTE.xlsx')

#df_2=pd.read_csv('APROBADOS.csv')
#st.write(df_2)

st.markdown(f':cry: Estos socios estan caidos en el proceso, hay que mandarles wattsapp para que terminen:') 

df=pd.read_csv('PROCESOS_PIVOTE.csv',encoding='latin-1')
st.write(df)

#st.markdown(f'*Resultados Disponibles:{numero_resultados}*') 


st.markdown(f':sweat_smile: Estos socios si terminaron el proceso jajaja:') 


df2=pd.read_csv('APROBADOS.csv',encoding='latin-1')
st.write(df2)


st.markdown(f':neutral_face: Estos socios fueron rechazados:') 


df3=pd.read_csv('RECHAZADOS.csv',encoding='latin-1')
st.write(df3)




import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)




import plotly.express as px
data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(data, x='number', y='stage')
fig.show()