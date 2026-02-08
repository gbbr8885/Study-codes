import streamlit as st
import pandas as pd
from scipy import stats

#configurador



fonte="Arial"
cor="white"

st.markdown("""
<style>
    .stApp {
        background-image: url('https://i.ibb.co/fdQ8RFCc/imagem-fundo-site.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
</style>
""", unsafe_allow_html=True)

#INTRODUÇÃO

st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Calculadora de posição em relação ao curso</span>', unsafe_allow_html=True)
st.markdown(f"### <span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Sabendo do seu IRA individual, IRA individual médio do curso e desvio padrão do conjunto de IRA's individuais do curso, em um determinado semestre, é possível conhecer sua posição acadêmica em relação aos seus colegas de curso nesse semestre.</span>", unsafe_allow_html=True)

st.markdown(f'### <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Para obter esses dados, faça o login no SIGAA e siga o caminho mostrado abaixo:</span>', unsafe_allow_html=True)

link_imagem='https://i.ibb.co/WNyvJkLQ/obtendo-estat-sticas-do-curso.png'

col1, col2, col3 = st.columns([1, 1000,1])
with col2:
    st.image(link_imagem,use_column_width=True)

#INSERÇÃO DOS DADOS

IRA=st.number_input("Digite o seu IRA individual (IRA-I):",min_value=0.0,step=0.00000000000000000000000000000000000000000000000000000000001,format="%.3f",key="IRA")
IRA=st.session_state.IRA


IRAm=st.number_input("Digite a média:",min_value=0.0,step=0.0000000000000000000000000000000000000000000011,format="%.8f",key="IRAm")
IRAm=st.session_state.IRAm


IRAdp=st.number_input("Digite o desvio-padrão:",min_value=0.0,step=0.0000000000000000000000000000000000000011,format="%.8f",key="IRAdp")
IRAdp=st.session_state.IRAdp



#CÁLCULO

def probabilidade_do_zscore(z):

    probabilidade = stats.norm.cdf(z)
    return probabilidade

if st.button('Clique aqui para calcular o seu IRA'):
    st.write('Calculadora acionada!')
    
    try:
        p=(1-probabilidade_do_zscore((IRA-IRAm)/IRAdp))*100

    except(ZeroDivisionError):
        p=0
        st.markdown(f'### <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">As entradas não podem ser zeros!</span>', unsafe_allow_html=True)

    if not p==0:

        if p<30:

            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Sua posição é tal que apenas {p:.2f}% dos estudantes do seu curso obtiveram IRA individual maior ou igual ao seu nesse semestre; parabéns!</span>', unsafe_allow_html=True)
        else:

            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Sua posição é tal que {p:.2f}% dos estudantes do seu curso obtiveram IRA individual maior ou igual ao seu nesse semestre.</span>', unsafe_allow_html=True)

