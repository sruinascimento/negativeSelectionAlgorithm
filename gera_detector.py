from ambiente import Ambiente
import pandas as pd
import numpy as np
import time


def inicializa(arg0, arg1):
    sample = pd.read_csv(arg0)
    # print(f'Dim do DataFrame: {sample.shape}')
    # sample_reduced = (sample.sample(n=arg2)) , arg2=None
    # sample_final = np.array(sample_reduced.drop(columns=arg1))
    sample_final = np.array(sample.drop(columns=arg1))
    # print(sample_final)
    # print(f'dim do array: {sample_final.shape}')
    ga = Ambiente(sample_final)
    ponto_inicial = time.time()
    ga.inicia()
    ponto_final = time.time()
    print(f'Tempo total de execução: {(ponto_final - ponto_inicial)} segundos')


if __name__ == '__main__':
    inicializa('/home/rui/PycharmProjects/projectRansomware/dataset_detector/random_goodwares687X85.csv', ['1', '2', '3'])

    '''

    inicializa('/home/rui/Documentos/2X9.CSV',
               ['0', '1', '2'])


      #dataset com 942 linhas x 86 colunas
    ponto_inicial = time.time()
    inicializa('/home/rui/PycharmProjects/pythonProject/venv/scripts/99_RF_s00025_ordenado_goodwares.csv',
               ['1', '2', '3'], 687)
    ponto_final = time.time()
    print(f'Tempo total de execução: {(ponto_final - ponto_inicial) / 60} minutos')



    ponto_inicial = time.time()
    #inicializa('/home/rui/PycharmProjects/pythonProject/venv/scripts/99_RF_s00025_ordenado_goodwares.csv', ['1', '2', '3'])
    inicializa('/home/rui/PycharmProjects/pythonProject/venv/scripts/99_RF_s00025_ordenado_goodwares.csv',
               ['1', '2', '3'])
    ponto_final = time.time()
    print(f'Tempo total de execução: {(ponto_final - ponto_inicial) / 60} minutos')
    '''