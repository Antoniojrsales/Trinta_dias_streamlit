'''
st.write
st.write permite exibir textos e argumentos (parâmetros) na aplicação Streamlit

Além de exibir texto, o comando st.write() também pode exibir:

strings; funciona semelhante ao st.markdown()
Exibir dicionários (dict) Python
Exibir Dataframes do pandas como uma tabela
Plotar gráficos e figuras das seguinte bibliotecas: matplotlib, plotly, altair, graphviz, bokeh
e mais (veja st.write na documentação da API)
'''

#importar a biblioteca
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write') #vamos adicionar um texto de cabeçalho:

# Exemplo 1 Caso de uso mais básico, exibir texto e texto no formato Markdown:

st.subheader('Display text')
st.write('Hello, *World!* :sunglasses:')

# Exemplo 2 Como mencionado acima, também podemos exibir outros formatos, como números:

st.subheader('Display number')
st.write(1234)

# Exemplo 3 DataFrames também podem ser exibidos:

st.subheader('Display DataFrame')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Exemplo 4 Você pode passar múltiplos argumentos (parâmetros):

st.subheader('Accept multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Exemplo 5 Finalmente, você também pode exibir dados de gráficos, passando os dados para uma variável da seguinte maneira:

st.subheader('Display charts')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)