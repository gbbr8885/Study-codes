
import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime

st.markdown('# Análise de empresas')

st.text_input('Digite o tickercode da empresa que deseja se informar',key='t',value='GOOG')
ticker = st.session_state.t

data=yf.Ticker(ticker)

st.markdown(f'## Histórico de ações de 2019 até hoje da {st.session_state.t} :')

end_date=datetime.now().strftime('%Y-%m-%d') #end_time pe uma variável que recebe a data configurada aos moldes da necessária para acessar o histórico

h=data.history(period='max',start='2019-06-01',end=end_date,interval='5d')
h=h.reset_index()

h=h[['Date','Open','High','Low','Close','Volume']]

st.dataframe(h)

ey=st.selectbox('Selecione o eixo y: ',['Open','High','Low','Close','Volume']) #Se quisesse todas as colunas poderia colocar h.columns no lugar da lista
ex=st.selectbox('Selecione o eixo x: ',['Open','High','Low','Close','Volume']) 

st.markdown('# Análise gráfica')
st.markdown(f'## {ey} em função de {ex}:')


st.line_chart(h,x=ex,y=ey)

#O código acima funciona da seguinte forma: primeiramente, o text_input() abre uma caixa na web para o usuário digitar. isso é guardado com a chave 't',através
#da qual essa informação poderá ser recuperada para o restante do código; o value é o valor padrão quando o site inicia. O session_state.t resgata a informação 
#de 't' da web para o python, guardando na variável ticker. O dataframe h foi restrito a apenas suas colunas 'High','Volume','Date', etc, através da síntaxe mostrada.
#Além disso, a biblioteca datetime foi utilizada para regular a análise do histórico até o dia atual em que a página for aberta, de acordo com a síntaxe mostrada.
#A função st.select() é usada para abrir uma caixa de seleção para o usuário escolher os eixos do gráfico, que agora estão atrelados às variáveis ex e ey.
#O restante do código é semelhante ao que antes já foi feito.