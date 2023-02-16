# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff


df = px.data.gapminder()
st.dataframe(df)

listaPaises = df["country"].unique()
st.write(listaPaises.tolist())

pais = "Canada"
with st.sidebar:
    st.write("Esta es una barra lateral")
    pais = st.selectbox('Paises',(listaPaises))
    st.write('Seleccionaste:', pais)

datosPais = df.query("country == '" + pais + "'")
fig = px.bar(datosPais, x='year', y='pop')
st.plotly_chart(fig, use_container_width=True)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.header("HOLA DESDE STREAMLIT")
    st.subheader("Probando...1...2...3")
    st.write("Hola, soy cristopher")
    st.subheader('Hola soy :red[Cristopher] emoji :sunglasses:')
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Cristopher')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
