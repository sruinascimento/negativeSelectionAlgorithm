import numpy as np

class Individuo:
    def __init__(self, cromossomo=np.array([-1])):
        self.tamanho = 82
        self.cromossomo = self.gera_cromossomo() if cromossomo[0] == -1 else cromossomo
        self.fitness = None

    def gera_cromossomo(self):
        cromossomo = np.random.randint(0, 2, size=self.tamanho)
        return cromossomo

    def __repr__(self):
        return f'Cromossomo: {self.cromossomo}\nFitness: {self.fitness}'

    def copia(self):
        indv_temp = Individuo(self.cromossomo)
        indv_temp.fitness = self.fitness
        return indv_temp

