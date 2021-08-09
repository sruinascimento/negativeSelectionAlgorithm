import numpy as np
from individuo import Individuo


def gera_populacao():
    populacao = [Individuo() for _ in range(6)]
    return populacao

def calcula_fitness(amostra ,cromossomo):
    soma_fitness = 0

    for individuo in amostra:
        acumulador_diferenca = 0
        condicao = np.array(cromossomo == individuo)
        if condicao.all() != True:
            soma_fitness += 1
        diferenca = [0 if individuo[i] == cromossomo[i] else 1 for i in range(len(cromossomo)) ]
        acumulador_diferenca += sum(diferenca)
        print("Diferenca")
        print(diferenca)
    return (soma_fitness, acumulador_diferenca)

if __name__ == "__main__":
    #pop = gera_populacao()
    #print(pop)
    amostra = np.array([[1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0]])
                       # [1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0]

    cromossomo = np.array([1,	0,	0,	0,	0,	1])
    '''
    [0,	0,	0,	0,	1,	1],
    [1,	1,	0,	1,	0,	1],
    [0,	1,	0,	1,	0,	0],
    [1,	1,	1,	0,	0,	1],
    [1,	0,	0,	0,	0,	0],
    [0,	1,	0,	1,	0,	1],
    [1,	1,	0,	0,	0,	1],
    [0,	0,	0,	0,	0,	1],
    [1,	0,	0,	0,	1,	1],
    [0,	0,	0,	1,	0,	0],
    [0,	0,	0,	1,	0,	1],
    [1,	1,	0,	0,	1,	1],
    [1,	0,	0,	0,	0,	1]

    '''
    print(f'Cromossomo: {cromossomo}')
    #x, y = calcula_fitness(amostra, cromossomo)
    soma_fitness = 0
    diff_50 = 0
    for individuo in amostra:
        acumulador_diferenca = 0
        condicao = np.array(cromossomo == individuo)

        if condicao.all() != True:
            soma_fitness += 1
        diferenca = [0 if individuo[i] == cromossomo[i] else 1 for i in range(len(cromossomo))]
        #acumulador_diferenca += sum(diferenca)
        if sum(diferenca) >= (len(individuo) * 0.5):
            print("Difere em 50% ou mais")
            diff_50 += 1
            print(f'Valor do dif: {diff_50}')
        else:
            print("Não difere em 50% ou mais")
            diff_50 -= 1
        print(f"Diferenca: {diferenca}")
        print(f"Fitness: {soma_fitness}")
        print(f"Diff: {diff_50}")
    #print(x, y)

