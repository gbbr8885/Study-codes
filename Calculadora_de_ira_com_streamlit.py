import streamlit as st
import pandas as pd


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
""", unsafe_allow_html=True) #estrutura que permite colocar foto de fundo no site


#APRESENTAÇÃO:


st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Simulador de IRA</span>', unsafe_allow_html=True) #extrutura que permite selecionar cor
st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Instruções:</span>', unsafe_allow_html=True)
st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas cursadas</span>',unsafe_allow_html=True)

st.markdown(
        f"#### <div style='text-align: justify;'> <span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>O seu IRA atual depende de TODAS as disciplinas que você cursou até o presente. Para a realização correta do cálculo, prepare um documento txt no formato mostrado a seguir incluindo TODAS as disciplinas cursadas (exceto as trancadas, caso tenha), mais as cadeiras do(s) semestre(s) não finalizado(s) para a(s) qual/quais você tenha sua suposição de nota final, com os dados pedidos (use ponto para separar a parte inteira de um número da parte decimal). Você pode editar o template disponível para download abaixo.</div>", 
        unsafe_allow_html=True
    ) #essa síntaxe permite formatar o texto.

link_imagem1 = 'https://i.ibb.co/WNNyppjr/Exemplo-hist-rico-cadeiras-n-o-trancadas.jpg' #link da imagem no repositório imgBB 

col1, col2, col3 = st.columns([1, 3, 1]) #separa o espaço da tela em 3 colunas (esquerda, centro e direita), definindo a proporção entre elas

with col2:
    st.image(link_imagem1, use_column_width=True,width=400) # põe a imagem na coluna 2. 'use_column_width' faz a imagem ocupar todo o espaço da coluna. Caso use_column_width fosse falso, a imagem teria o tamanho definido por width 

st.download_button(
    label="Baixar template histórico cadeiras não trancadas",
    data='Disciplina,Semestre,Carga horária,Nota',  
    file_name="Histórico_cadeiras_não_trancadas.txt"
) # gera arquivo para download para usuário

#INSERÇÃO DE DADOS:

historico_nt = st.file_uploader('Faça o upload do documento solicitado:',key='k1') #gera janela de realizar upload
historico_nt=st.session_state.k1

semestres_não_consolidados=st.number_input("Quantos desses semestres ainda não estão consolidados?",min_value=0.0,step=0.0000000000000000000000000000000001,format="%.0f",value=None)

há_trancamento=st.selectbox("### Há trancamentos na sua simulação?",['Não','Sim'])

    #CADEIRAS TRANCADAS:

if há_trancamento=='Sim':

    st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas trancadas</span>', unsafe_allow_html=True)

    st.markdown(
            f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Caso tenho trancado cadeira(s) ou queira simular trancamento(s) em semestre(s) não finalizado(s), prepare um documento txt no formato mostrado a seguir com TODAS essas disciplinas. Você pode editar o template disponível para download abaixo. Caso não tenho trancamentos, não realize esse passo.</div>", 
            unsafe_allow_html=True
        )

    link_imagem2='https://i.ibb.co/rKMp0gmZ/Exemplo-hist-rico-cadeiras-trancadas.jpg'

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image(link_imagem2, use_column_width=True,width=400)

    st.download_button(
        label="Baixar template histórico cadeiras trancadas",
        data='Disciplina,Semestre,Carga horária',  
        file_name="Histórico_cadeiras_trancadas.txt"
    )

    historico_t=st.file_uploader('Faça o upload do documento solicitado',key='k2')
    historico_t=st.session_state.k2

else:

    historico_t=None

if semestres_não_consolidados is not None:

    if semestres_não_consolidados==0:

        st.markdown("### Zero semestres não consolidados significa que os IRA's de todos esses semestres já se encontram em seu histórico de IRA no SIGAA, não fazendo sentido calculá-los. Tem certeza que esse número é zero? Se continuar com esse valor, os valores de IRA obtidos serão iguais aos já disponíveis no SIGAA.")

    #ÍNDICES DO CURSO:

    if semestres_não_consolidados==1:

        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA geral</span>', unsafe_allow_html=True)
        st.markdown(
                f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>O seu IRA geral depende do seu IRA individual e do desempenho dos alunos do seu curso no semestre em questão, medido pela média e desvio padrão de IRA perfomados por seus colegas de curso. Se deseja fazer uma estimativa do seu IRA geral, você deve obter essas estatísticas através do SIGAA entrando na página e clicando na opção mostrada abaixo:</div>", 
                unsafe_allow_html=True
            )

        link_imagem3='https://i.ibb.co/WNyvJkLQ/obtendo-estat-sticas-do-curso.png'

        col1, col2, col3 = st.columns([1, 1000,1])
        with col2:
            st.image(link_imagem3,use_column_width=True)


        st.markdown(
                f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Após fazer isso, você chegará em uma página com uma seção chamada 'índices do curso', onde se encontram média e desvio padrão de IRA relativo a cada semestre que você cursou. Com eses dados, monte um documento txt como mostrado abaixo (informe os valores com todas as casas decimais e usando ponto para separar a parte inteira da parte decinal dos números). Você pode editar o template disponível para download abaixo. Com isso, o IRA geral que exibiremos para semestres que você já cursou é o valor real e, para o semestre que você ainda não finalizou exibiremos uma estimativa com base nas estatísticas de todos os semestre que você cursou. Caso não queira estimar IRA geral, pule esse passo.</div>", 
                unsafe_allow_html=True
            )

        link_imagem4='https://i.ibb.co/GQK9PxJm/Exemplo-ndices-do-curso.png'

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st.image(link_imagem4,use_column_width=True)

        st.download_button(
            label="Baixar template índices do curso",
            data='Semestre,Média,Desvio-padrão', 
            file_name="Índices_do_curso.txt"
        )

        indices=st.file_uploader('Faça o upload do documento solicitado:',key='k3')
        indices=st.session_state.k3

        if indices is not None:
            st.markdown(
                    f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Como informação adicional, informe a quantidade de vagas ofertadas por ano para o seu curso e o número de semestres de duração do seu curso.</div>", 
                    unsafe_allow_html=True,
                )
            vagas=st.number_input('Digite o número de vagas:',min_value=0.0,step=0.0000000000000000000000000000000000000001,format="%.0f",key='v')
            vagas=st.session_state.v
            n_semestres=st.number_input('Digite o número de semestres:',min_value=0.0,step=0.00000000000000000000000000000001,format="%.0f",key='n')
            n_semestres=st.session_state.n

#BOTÃO QUE ACIONA CALCULADORA:

if st.button('Clique aqui para calcular o seu IRA'):
    st.write('Simulação acionada!')

#CALCULADORA DE IRA:

    try:
        tranc={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        irasi=[]
        irasg=[]

        if historico_nt is not None:

            if historico_t is not None:

                h_t=pd.read_csv(historico_t)

                T=0

                for i in range(h_t.shape[0]):
                                                            
                    T=T+h_t['Carga horária'][i]

                    if i<h_t.shape[0]-1:

                        if h_t['Semestre'].iloc[i+1]>h_t['Semestre'].iloc[i]:
                            tranc[h_t['Semestre'].iloc[i]]=T
                    else:
                        tranc[h_t['Semestre'].iloc[i]]=T
            h_nt=pd.read_csv(historico_nt)

            num=0
            den=0
            C=0

            for i in range(h_nt.shape[0]):
                p=h_nt['Semestre'][i]
                c=h_nt['Carga horária'][i]
                n=h_nt['Nota'][i]
                C=c+C
                if p>6:
                    p=6
                num=num + p*c*n
                den=den + p*c

                if historico_t is not None:

                    if i<h_nt.shape[0]-1:  

                        if h_nt['Semestre'][i+1]>h_nt['Semestre'][i]:
                            ira_indiv=(1-(0.5*tranc[h_nt['Semestre'][i]]/(C+tranc[h_nt['Semestre'][i]])))*(num/den)
                            irasi.append(ira_indiv)

                    else:
                        ira_indiv=(1-(0.5*tranc[h_nt['Semestre'][i]]/(C+tranc[h_nt['Semestre'][i]])))*(num/den)
                        irai_ultimo_semestre=ira_indiv
                        
                else:

                    if i<h_nt.shape[0]-1:  

                        if h_nt['Semestre'][i+1]>h_nt['Semestre'][i]:
                            ira_indiv=num/den
                            irasi.append(ira_indiv)
                            

                    else:
                        ira_indiv=num/den
                        irai_ultimo_semestre=ira_indiv
                        

            if indices is not None:

                medias=[]
                desvios_padrao=[]

                id=pd.read_csv(indices)

                for i in id['Média']:

                    medias.append(i)

                for i in id['Desvio-padrão']:

                    desvios_padrao.append(i)

                for i in range(id.shape[0]):

                        m=id['Média'][i]
                        dp=id['Desvio-padrão'][i]

                        irasg.append(6+2*((irasi[i]-m)/dp))

                from Estima_IRA_geral import estima_IRA_medio_populacional as eimp

                n=vagas*(n_semestres/2)/3

                media_combinada,desvio_padrao_combinado,limite_inferior_media,limite_superior_media=eimp(medias,desvios_padrao,n)

                irag_estimado_1=6+2*((irai_ultimo_semestre-limite_inferior_media)/desvio_padrao_combinado)
                irag_estimado_2=6+2*((irai_ultimo_semestre-limite_superior_media)/desvio_padrao_combinado)
                irag_estimado_3=6+2*((irai_ultimo_semestre-media_combinada)/desvio_padrao_combinado)

                historico_ira={'Semestre':[],'IRA individual':irasi,'IRA geral':irasg}

                for i in range(len(irasi)):

                    historico_ira['Semestre'].append(i+1)

                historico_ira=pd.DataFrame(historico_ira)
                
            else:

                historico_ira={'Semestre':[],'IRA individual':irasi}

                for i in range(len(irasi)):

                    historico_ira['Semestre'].append(i+1)

                historico_ira=pd.DataFrame(historico_ira)
            historico_ira.index=historico_ira.index+1

            h_nt.index=h_nt.index+1

            if historico_t is not None:

                h_t.index=h_t.index+1


            from Estima_IRA_geral import probabilidade_do_zscore as pzs

            id.insert(1,'IRA individual',irasi)

            lp=[]

            for i in range(id.shape[0]):

                IRA=id["IRA individual"][i]
                IRAm=id["Média"][i]
                IRAdp=id["Desvio-padrão"][i]

                p=(1-pzs((IRA-IRAm)/IRAdp))*100
                lp.append(p)

#EXIBIÇÃO DOS RESULTADOS:


    #IRA ATUAL:


        st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA atual(semestre {len(irasi)+1}):</span>', unsafe_allow_html=True)
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA individual: {irai_ultimo_semestre:.4f}</span>', unsafe_allow_html=True)

        if indices is not None:

            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA geral: com 95% de confiança, seu IRA geral está entre {irag_estimado_1:.4f} e {irag_estimado_2:.4f}. Uma boa estimativa pontual é: {irag_estimado_3:.4f}</span>', unsafe_allow_html=True)
        

    #HISTÓRICO DE IRA:


        st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Histórico IRA por semestre:</span>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2.5, 5, 1])
        with col2:

            st.dataframe(historico_ira)

        if len(irasi)>=3:
            if indices is not None:

                historico_ira['Semestre'] = historico_ira['Semestre'].astype(str) #Trasforma os valores de semestre em string para que no gráfico não seja exibido número de semestre "quebrados"
                st.line_chart(historico_ira,x='Semestre',y=['IRA individual','IRA geral']) 
            else:

                historico_ira['Semestre'] = historico_ira['Semestre'].astype(str) #Trasforma os valores de semestre em string para que no gráfico não seja exibido número de semestre "quebrados"
                st.line_chart(historico_ira,x='Semestre',y='IRA individual')


    #HISTÓRICO:


        st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Histórico: </span>', unsafe_allow_html=True)
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras cursadas: {h_nt.shape[0]}</span>', unsafe_allow_html=True)
        if historico_t is not None:
            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras trancadas: {h_t.shape[0]}</span>', unsafe_allow_html=True)
        else:
            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras trancadas: 0</span>', unsafe_allow_html=True)
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas cursadas:</span>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2, 20, 1])
        with col2:
            st.dataframe(h_nt)
        if historico_t is not None:
            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas trancadas:</span>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns([2.4, 5, 1])
            with col2:
                st.dataframe(h_t)


    #ESTATÍSTICAS:


        st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Estatísticas: </span>', unsafe_allow_html=True)
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Maior IRA: {max(max(irasi),irai_ultimo_semestre):.4f}</span>', unsafe_allow_html=True)
        if max(max(irasi),irai_ultimo_semestre) in irasi:
            for i in range(len(irasi)):
                if irasi[i]==max(max(irasi),irai_ultimo_semestre):
                    semestre_ira_max=i+1
                else:
                    None
        else:
            semestre_ira_max=len(irasi)+1
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Semestre de maior IRA: {semestre_ira_max} </span>', unsafe_allow_html=True)
        if indices is not None:
            st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Índices do curso:</span>', unsafe_allow_html=True)
            id.index=id.index+1
            col1, col2, col3 = st.columns([2.5, 5, 1])
            with col2:
                st.dataframe(id)
        

            for i in range(id.shape[0]):
                st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px"> Semestre {i+1} </span>', unsafe_allow_html=True)
                if lp[i]<30:

                    st.markdown(f'### <span style="font-family:{fonte}, serif; color:{cor}; font-size:px"> Apenas {lp[i]:.2f}% dos estudantes do seu curso obtiveram IRA individual igual ou maior que o seu; parabéns! </span>', unsafe_allow_html=True)

                else:   

                    st.markdown(f'### <span style="font-family:{fonte}, serif; color:{cor}; font-size:px"> {lp[i]:.2f}% dos estudantes do seu curso obtiveram IRA individual igual ou maior que o seu. </span>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown('### Você cometeu erro(s) ao preencher e/ou formatar o(s) documento(s) txt que você forneceu. Certifique-se que estão em conformidade com os modelos fornecidos e com as instruções orientadas')
        st.error(f"Detalhe do erro: {type(e).__name__}: {e}")
