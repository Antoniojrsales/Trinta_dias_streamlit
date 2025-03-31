'''
st.line_chart
st.line_chart permite exibir um gráfico de linhas

Este é um açúcar sintático relacionado ao st.altair_chart. A principal diferença é que este comando usa as colunas e índices dos próprios dados e tenta descobrir a melhora maneira de exibir o gráfico. Ou seja, é mais fácil de usar para os cenários "apenas exiba o gráfico", porém menos customizável.

Se o st.line_chart não acertar a melhor maneira de exibir o gráfico, ou o melhor tipo, tente usar o st.altair_chart e especifique a informação desejada.

O que estamos construindo?
Uma aplicação simples para exibir um gráfico de linhas

Fluxo da aplicação:

Cria um DataFrame pandas com números gerados aleatoriamente pelo NumPy.
Cria e mostra um gráfico de linha usando o comando st.line_chart().
'''

import streamlit as st
import pandas as pd
import numpy as np

st.header('Gráfico de linhas') #Na sequência, vamos adicionar um texto de cabeçalho:

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']) #Agora, nós criamos o Dataframe de 3 colunas com números aleatórios.

st.line_chart(chart_data) #Finalmente, um gráfico de linhas é criado usando st.line_chart() com o DataFrame armazenado na variável chart_data como entrada: