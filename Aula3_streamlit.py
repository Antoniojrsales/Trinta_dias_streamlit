'''O que estamos construindo?
Uma aplicação simples que imprime condicionalmente mensages alternadas, dependendo se o botão estão pressionado ou não.

Fluxo da aplicação:

Por padrão, a aplicação imprime Goodbye
Após clicar no botão, a aplicação imprime Why hello there
'''

import streamlit as st

st.header('St.Button') #Na sequência, vamos adicionar um texto de cabeçalho:

#Agora, vamos utilizar condicionais if e else para imprimir as mensagens alternadamente.
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
#Como podemos ver no código acima, o comando st.button() recebe Say hello como argumento de entrada, que é o texto que o botão exibirá.

#O comando st.write é usado para imprimir mensages de texto, no caso Why hello there ou Goodbye, dependendo se o botão foi clicado ou não, que é implementando assim: