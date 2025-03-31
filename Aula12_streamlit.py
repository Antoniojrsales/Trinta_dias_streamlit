'''st.checkbox
st.checkbox exibe um componente de caixa de seleção.'''

import streamlit as st

st.header('st.checkbox') #Na sequência, vamos adicionar um texto de cabeçalho:

st.write ('O que você gostaria de pedir?') #Agora, nós vamos perguntar ao usuário usando o st.write:

icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante') #Em seguida vamos mostrar algumas opções do menu que podem ser selecionadas:

if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")

if coffee: 
     st.write("Ok, aqui está o seu café ☕")

if cola:
     st.write("E lá vamos nós 🥤") #Finalmente, nós vamos imprimir uma mensagem customizada, dependendo das caixas de seleções que foram marcadas: