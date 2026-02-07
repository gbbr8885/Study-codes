from scipy import stats
import numpy as np

def estima_IRA_medio_populacional(medias, desvios_padrao, n,nivel_confianca=0.95): #medias: lista de médias. desvios_padrao: lista de desvios padrão. n: tamanho das amoestras (número de alunos do curso)
    if len(medias)>1:

    #estatísticas combinadas

        #Média combinada

        media_combinada = np.mean(medias)

        #Desvio padrão combinado

        N = len(medias)
        tamanho_total = N*n

        part_1 = (n - 1) * np.sum(np.square(desvios_padrao))

        part_2 = n * np.sum(np.square(np.array(medias) - media_combinada))
        
        soma = part_1 + part_2
        
        variancia_combinada = soma / (tamanho_total - 1)
        desvio_padrao_combinado = np.sqrt(variancia_combinada)
    
    else:
        tamanho_total=n
        media_combinada=medias[0]
        desvio_padrao_combinado=desvios_padrao[0]

    #intervalo de confiança

    gl=n-1
    t_student=stats.t.ppf((1-nivel_confianca)/2,gl)
    erro=t_student*desvio_padrao_combinado/np.sqrt(tamanho_total)
    limite_inferior=media_combinada-erro
    limite_superior=media_combinada+erro

  

    return media_combinada,desvio_padrao_combinado,limite_inferior,limite_superior
