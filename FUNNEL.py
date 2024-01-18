

import streamlit as st
import pandas as pd

import pip 
#pip.main(["install","matplotlib"])
#pip.main(["install","numpy"])
#pip.main(["install","plotly_express"])
pip.main(['install', 'matplotlib'])
pip.main(['install', 'plotly'])
pip.main(['install', 'plotly_express==0.4.0'])


#import plotly.express as px

#import matplotlib.pyplot as plt
import numpy as np

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
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)




import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)