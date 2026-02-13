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
st.markdown(f"### <span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Sabendo do seu IRA Geral em um determinado semestre, é possível conhecer sua posição acadêmica em relação aos seus colegas de curso nesse semestre.</span>", unsafe_allow_html=True)

st.markdown(f'### <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Para obter esses dados, faça o login no SIGAA e siga o caminho mostrado abaixo:</span>', unsafe_allow_html=True)

link_imagem='https://i.ibb.co/WNyvJkLQ/obtendo-estat-sticas-do-curso.png'

col1, col2, col3 = st.columns([1, 1000,1])
with col2:
    st.image(link_imagem,use_column_width=True)

st.markdown('### Insira os dados requeridos com todas as casas decimais.')

#INSERÇÃO DOS DADOS

IRAG=st.number_input("Digite o seu IRA Geral (IRA-G):",min_value=0.0,step=0.00000000000000000000000000000000000000000000000000000000001,format="%.4f",key="IRAG")
IRAG=st.session_state.IRAG


#CÁLCULO

def probabilidade_do_zscore(z):

    probabilidade = stats.norm.cdf(z)
    return probabilidade

if st.button('Clique aqui para calcular sua posição'):
    st.write('Calculadora acionada!')
    
    p=(1-probabilidade_do_zscore((IRAG-6)/2))*100



    if not p==0:

        if p<30:

            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Sua posição é tal que apenas {p:.2f}%, aproximadamente dos estudantes do seu curso obtiveram IRA individual maior ou igual ao seu nesse semestre; parabéns!</span>', unsafe_allow_html=True)
        else:

            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Sua posição é tal que aproximadamente {p:.2f}% dos estudantes do seu curso obtiveram IRA individual maior ou igual ao seu nesse semestre.</span>', unsafe_allow_html=True)

