'''st.multiselect
st.multiselect exibe um componente de seleção múltipla'''

import streamlit as st

st.header('st.multiselect') #Na sequência, vamos adicionar um texto de cabeçalho:

options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho']) #Agora, nós vamos usar o componente st.multiselect para receber a entrada dos usuários, que escolherão uma ou mais cores.

st.write('Você selecionou:', options) #Finalmente vamos imprimir as cores selecionadas:

