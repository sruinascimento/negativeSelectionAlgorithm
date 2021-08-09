import numpy as np
import pandas as pd

class NSA:
    def __init__(self, sample_r, sample_d, sample_g):
        self.sample_r = sample_r
        self.sample_d = sample_d
        self.sample_g = sample_g
        self.percentual = [41, 49.2, 57.4, 65.6, 73.8, 82]
        self.self = []
        self.nonself = []
        self.calc_pct = lambda pct, total: pct * 100 / total

    def start(self):
        for _ in self.percentual:
            print(f'Teste com o percentual {np.round(self.calc_pct(_, 82))}%')
            count_r = 0
            for i in self.sample_r:
                resultado = np.bitwise_xor(i, self.sample_d)
                #print('Resultado da comparação dos vetores')
                #print(resultado, end='\n')
                resultado_cr = resultado.sum(axis=1)
                resultado_cr = np.array( [82 - i for i in resultado_cr ] )
                if resultado_cr.max() >= _ :
                    #print(f'{i} --> Ransomware')
                    count_r += 1
            print(f'Total de Ransomwares detectados: {count_r}')

            count_g = 0
            for j in self.sample_r:
                resultado = np.bitwise_xor(j, self.sample_g)
                #print('Resultado da comparação dos vetores')
                #print(resultado, end='\n')
                resultado_cg = resultado.sum(axis=1)
                resultado_cg = np.array( [82 - i for i in resultado_cg ] )
                if resultado_cg.max() >= _:
                    #print(f'{i} -->Falso Ransomware')
                    count_g += 1
            print(f'Total de Falso Ransomware Ransomwares detectados: {count_g}')
            self.escreve_txt(np.round(self.calc_pct(_, 82)), count_r, count_g)

    def escreve_txt(self, pct, count_r, count_g):
        with open('/home/rui/Área de Trabalho/projeto/dataset/teste/testestes20.txt', 'a') as arq:
            arq.write('Teste com percentual :'+str(pct)+'\n')
            arq.write('Total de Ransomwares detectados: '+str(count_r)+'\n')
            arq.write(str(self.calc_pct(count_r, 208)) +'% de Verdadeiro Positivo\n')
            arq.write('Total de Falsos Ransomwares detectados: ' + str(count_g) + '\n')
            arq.write(str(self.calc_pct(count_g, 208)) + '% de Falso Positivo\n')
            arq.write('=========================================================\n')


if __name__ == '__main__':
    #sample_ransomwares = pd.read_csv('/home/rui/Área de Trabalho/projeto/dataset/treino_teste/70_30_t1/random_ransomwares408X85.csv')
    #sample_detector    = pd.read_csv('/home/rui/Área de Trabalho/projeto/dataset/treino_teste/70_30_t1/detectores687X82_5499_.csv')
    sample_goodwares   = pd.read_csv('/home/rui/Área de Trabalho/projeto/dataset/teste/dataset_goodware_20_208X85.csv')
    sample_ransomwares = pd.read_csv('/home/rui/Área de Trabalho/projeto/dataset/teste/dataset_ransomware_20_208X85.csv')
    sample_detector    = pd.read_csv('/home/rui/Área de Trabalho/projeto/dataset/teste/detectores687X82_10811_.csv')

    obj = NSA(np.array(sample_ransomwares.drop(columns=['1', '2', '3'])), np.array(sample_detector),
              np.array(sample_goodwares.drop(columns=['1', '2', '3'])))
    obj.start()

