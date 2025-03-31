'''
st.selectbox
st.selectbox exibe um componente de seleção

O que estamos construindo?
Uma aplicação simples que pergunta ao usuário qual a cor favorita dele.

Fluxo da aplicação:

Usuário seleciona a cor
Aplicação exibe a cor selecionada
Aplicação de demonstração
Depois de feito o deploy a aplicação ficará semelhante a mostrada no link abaixo.
'''

import streamlit as st

st.header('st.selectbox') #Na sequência, vamos adicionar um texto de cabeçalho:

option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde')) #Em seguida, vamos criar uma variável chamada option que vai receber o valor do componente selectbox através do comando st.selectbox().

'''
Como você pode ver no código acima, o comando st.selectbox() aceita 2 argumentos (parâmetetros) de entrada:

1- O texto que vai acima do componente, ex: 'Qual a sua cor favorita?'
2- Os valores possíveis de serem selecionados ('Azul', 'Vermelho', 'Verde')
'''

st.write('Sua cor favorita é: ', option) #Finalmente, vamos imprimir a cor selecionada: