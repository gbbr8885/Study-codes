import streamlit as st
import pandas as pd


#configurador

fonte=st.selectbox('Selecione uma cor',[
    "Arial", "Helvetica", "Verdana", "Tahoma", "Trebuchet MS", "Geneva",
    "Times New Roman", "Georgia", "Palatino", "Garamond", "Bookman",
    "Courier New", "Courier", "Lucida Console", "Monaco", "Consolas",
    "Comic Sans MS", "Brush Script MT", "Lucida Handwriting",
    "Helvetica Neue", "Segoe UI", "Calibri", "Futura", "Optima",
    "Avant Garde", "Century Gothic", "Book Antiqua", "Baskerville",
    "Cambria", "Constantia", "Copperplate", "Didot", "Footlight MT Light",
    "Hoefler Text", "Bodoni MT", "Goudy Old Style", "Lucida Bright",
    "MS Serif", "New York", "Perpetua", "Rockwell", "Times",
    "Monospace", "MS Gothic", "DejaVu Sans Mono", "Bitstream Vera Sans Mono",
    "Andale Mono", "OCR A Extended", "Menlo", "Source Code Pro",
    "Fira Code", "Cascadia Code", "Apple Chancery", "Script MT Bold",
    "Vivaldi", "Zapf Chancery", "Coronetscript", "Florence", "Parkavenue",
    "Rage Italic", "Segoe Script", "Segoe Print", "Kristen ITC",
    "French Script MT", "Monotype Corsiva", "Lucida Calligraphy",
    "Impact", "Charcoal", "Fantasy", "Western", "Jokerman",
    "Old English Text MT", "Parchment", "Plastique", "Arnoldboecklin",
    "Bauhaus 93", "Braggadocio", "Desdemona", "Emblem", "Goudy Stout",
    "Harrington", "Kino MT", "Matura MT Script Capitals", "Playbill",
    "Ravie", "Stencil", "System", "Lucida Sans", "Lucida Grande",
    "MS Sans Serif", "Wingdings", "Webdings", "Symbol"
])

cor=st.text_input('Digite uma cor',key='c')
cor=st.session_state.c


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

st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Calculadora de IRA</span>', unsafe_allow_html=True) #extrutura que permite selecionar cor
st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Instruções:</span>', unsafe_allow_html=True)
st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas cursadas</span>',unsafe_allow_html=True)

st.markdown(
        f"#### <div style='text-align: justify;'> <span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>O seu IRA atual depende de TODAS as disciplinas que você cursou até o presente. Para a realização correta do cálculo, prepare um documento txt no formato mostrado a seguir incluindo TODAS as disciplinas cursadas (exceto as trancadas, caso tenha) com os dados pedidos. Você pode editar o template disponível para download abaixo.</div>", 
        unsafe_allow_html=True
    ) #essa síntaxe permite formatar o texto.

link_imagem1 = 'https://i.ibb.co/QVqpTt5/exemplo-hist-rico-cadeiras-n-o-trancadas.png' #link da imagem no repositório imgBB

col1, col2, col3 = st.columns([1, 3, 1]) #separa o espaço da tela em 3 colunas (esquerda, centro e direita), definindo a proporção entre elas

with col2:
    st.image(link_imagem1, use_column_width=True,width=400) # põe a imagem na coluna 2. 'use_column_width' faz a imagem ocupar todo o espaço da coluna. Caso use_column_width fosse falso, a imagem teria o tamanho definido por width 

st.download_button(
    label="Baixar template histórico cadeiras não trancadas",
    data='Disciplina,Semestre,Carga_Horária,Nota',  
    file_name="histórico cadeiras não trancadas.txt"
) # gera arquivo para download para usuário

historico_nt = st.file_uploader('Faça o upload do arquivo:',key='k1') #gera janela de realizar upload
historico_nt=st.session_state.k1


st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas trancadas</span>', unsafe_allow_html=True)

st.markdown(
        f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Caso tenho trancado cadeira(s), prepare um documento txt no formato mostrado a seguir com TODAS as disciplinas trancadas. Você pode editar o template disponível para download abaixo. Caso não tenho trancamentos, não realize esse passo.</div>", 
        unsafe_allow_html=True
    )

link_imagem2='https://i.ibb.co/mCPh3yGB/exemplo-hist-rico-cadeiras-trancadas.png'

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image(link_imagem2, use_column_width=True,width=400)

st.download_button(
    label="Baixar template histórico cadeiras trancadas",
    data='Disciplina,Semestre,Carga_Horária',  
    file_name="histórico cadeiras trancadas.txt"
)

historico_t=st.file_uploader('Faça o upload do arquivo',key='k2')
historico_t=st.session_state.k2

st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA geral</span>', unsafe_allow_html=True)
st.markdown(
        f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>O seu IRA geral depende do seu ira individual e do desempenho dos alunos do seu curso no semestre em questão, medido pela média e desvio padrão de IRA perfomados por seus colegas de curso. Se deseja fazer uma estimativa do seu IRA geral, você deve obter essas estatísticas através do SIGAA entrando na página e clicando na opção mostrada abaixo:</div>", 
        unsafe_allow_html=True
    )

link_imagem3='https://i.ibb.co/WNyvJkLQ/obtendo-estat-sticas-do-curso.png'

col1, col2, col3 = st.columns([1, 1000,1])
with col2:
    st.image(link_imagem3,use_column_width=True)


st.markdown(
        f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Após fazer isso, você chegará em uma página com uma seção chamada 'índices do curso', onde se encontram média e desvio padrão de IRA relativo a cada semestre que você cursou. Com eses dados, monte um documento txt como mostrado abaixo (informe os valores com todas as casas decimais). Você pode editar o template disponível para download abaixo. Com isso, o IRA geral que exibiremos para semestres que você já cursou é o valor real e, para o semestre que você ainda não finalizou exibiremos uma estimativa com base nas estatísticas de todos os semestre que você cursou.</div>", 
        unsafe_allow_html=True
    )

link_imagem4='https://i.ibb.co/pGLLLdQ/exemplo-ndices-do-curso.png'

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image(link_imagem4,use_column_width=True)

st.download_button(
    label="Baixar template índices do curso",
    data='Semestre,Média,Desvio-padrão', 
    file_name="índices do curso.txt"
)

indices=st.file_uploader('Faça o upload do arquivo:',key='k3')
indices=st.session_state.k3

st.markdown(
        f"#### <div style='text-align: justify;'><span style='font-family:{fonte}, serif; color:{cor}; font-size:px'>Como informação adicional, informe a quantidade de vagas ofertadas por ano para o seu curso e o número de semestres de duração do seu curso.</div>", 
        unsafe_allow_html=True,
    )
vagas=st.number_input('Digite o número de vagas:',min_value=0,step=1,key='v')
vagas=st.session_state.v
n_semestres=st.number_input('Digite o número de semestres:',min_value=0,step=1,key='n')
n_semestres=st.session_state.n

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

    st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Histórico IRA por semestre:</span>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2.5, 5, 1])
    with col2:

        st.dataframe(historico_ira)

    if len(irasi)>=3:
        if indices is not None:

            st.line_chart(historico_ira,x='Semestre',y=['IRA individual','IRA geral'])
        else:

            st.line_chart(historico_ira,x='Semestre',y='IRA individual')

    st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA atual(semestre {len(irasi)+1}):</span>', unsafe_allow_html=True)
    st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA individual: {irai_ultimo_semestre:.4f}</span>', unsafe_allow_html=True)

    if indices is not None:

        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">IRA geral: com 95% de confiança, seu IRA geral está entre {irag_estimado_1:.4f} e {irag_estimado_2:.4f}. Uma boa estimativa pontual é: {irag_estimado_3:.4f}</span>', unsafe_allow_html=True)
    
    st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Histórico: </span>', unsafe_allow_html=True)
    st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras cursadas: {h_nt.shape[0]}</span>', unsafe_allow_html=True)
    if historico_t is not None:
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras trancadas: {h_t.shape[0]}</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Quantidade de cadeiras trancadas: 0</span>', unsafe_allow_html=True)
    st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas cursadas:</span>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4.9, 20, 1])
    with col2:
        st.dataframe(h_nt)
    if historico_t is not None:
        st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Disciplinas trancadas:</span>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2.4, 5, 1])
        with col2:
            st.dataframe(h_t)
    st.markdown(f'# <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Estatísticas: </span>', unsafe_allow_html=True)
    st.markdown(f'## <span style="font-family:{fonte}, serif; color:{cor}; font-size:px">Maior IRA: {max(irasi,irai_ultimo_semestre)[0]:.4f}</span>', unsafe_allow_html=True)
    if max(irasi,irai_ultimo_semestre) in irasi:
        for i in range(len(irasi)):
            if irasi[i]==max(irasi,irai_ultimo_semestre):
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
    

