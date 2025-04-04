'''
st.slider
st.slider permite exibir um controle deslizante (slider).

Os seguintes tipos do Python são suportados: int, float, date, time, and datetime.

O que estamos construindo?
Uma palicação simples, que mostras as diversas maneiras de como aceitar a entrada do usuários com o controle deslizante (slider).

Fluxo da aplicação:

Usuário seleciona o valor ajustando controle deslizante (slider).
Aplicação imprime o valor selecionado
'''

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Exemplo 1
#Como você pode perceber, o comando st.slider() é usado para pegar a entrada do usuários sobre a idade.
#O primeiro argumento (parâmetro) exibe o texto acima do slider perguntando 'Quantos anos você tem?'.
#Os três números inteiros a seguir 0, 130, 25 representam, respectivamente, o mínimo, máximo e o padrão.

st.subheader('Slider')

age = st.slider('Quantos anos você tem?', 0, 130, 25)
st.write("Eu tenho ", age, ' anos')

# Exemplo 2
#O slider de intervalo permite a seleção de um par de valores.
#O primeiro argumento (parâmetro) exibe o texto acima do slider de intervalo pedindo 'Escolha um intervalo de valores'.
#Os três argumentos (parâmetros) a seguir 0.0, 100.0, (25.0, 75.0) representam o valor mínimo e o máximo, enquanto que a tupla são os valores padrões para o par de números.

st.subheader('Slider de intervalo')

values = st.slider(
     'Escolha um intervalo de valores',
     0.0, 100.0, (25.0, 75.0))
st.write('Valores:', values)

# Exemplo 3
#O slider de intervalo de tempo permite a seleção de um par de valores do tipo datetime.
#O primeiro argumento (parâmetro) exibe o texto acima do Slider de intervalo de tempo pedindo 'Agende um compromisso:.
#O valor padrão para o intervalo é das 11:30 até as 12:45.

st.subheader('Slider de intervalo de tempo')

appointment = st.slider(
     "Agende um compromisso:",
     value=(time(11, 30), time(12, 45)))
st.write("O compromisso foi agendado para:", appointment)

# Exemplo 4
#O slider de data e hora permite a seleção de data e hora, tipo datetime do Python.
#O primeiro argumento (parâmetro) exibe o texto acima do Slider de data e hora perguntando 'Quando você vai começar?'.
#O valor padrão para data e hora (datetime) foi definido usando o valor: 1 de Janeiro de 2020 as 9:30.

st.subheader('Slider de data e hora')

start_time = st.slider(
     "Quando você vai começar?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Início:", start_time)