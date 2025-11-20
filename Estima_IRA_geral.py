from scipy import stats
import numpy as np

def estima_media_populacao(medias, desvios_padrao, n,nivel_confianca=0.95): #medias: lista de médias. desvios_padrao: lista de desvios padrão. n: tamanho das amoestras (número de alunos do curso)
    if len(medias)>1:

    #estatísticas combinadas

        N = len(medias)
        total_size = N * n

        media_combinada = np.mean(medias)

        SS_within = (n - 1) * np.sum(np.square(desvios_padrao))

        SS_between = n * np.sum(np.square(np.array(medias) - media_combinada))
        
        SST = SS_within + SS_between
        
        variancia_combinada = SST / (total_size - 1)
        desvio_padrao_combinado = np.sqrt(variancia_combinada)
    
    else:

        media_combinada=medias[0]
        desvio_padrao_combinado=desvios_padrao[0]

    #intervalo de confiança

    gl=n-1
    t_student=stats.t.ppf((1-nivel_confianca)/2,gl)
    erro=t_student*desvio_padrao_combinado/np.sqrt(n)
    limite_inferior=media_combinada-erro
    limite_superior=media_combinada+erro

  

    return media_combinada,desvio_padrao_combinado,limite_inferior,limite_superior
