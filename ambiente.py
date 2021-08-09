from individuo import Individuo
import numpy as np
import pandas as pd
from random import sample, randint, random


class Ambiente:
    def __init__(self, amostra):
        self.tam_pop = 150
        self.amostra = amostra
        self.melhor_individuo = None
        self.taxa_cruzamento = 0.9
        self.taxa_mutacao = 0.02
        self.geracao_parada = 20
        #self.media_fitness = []
        #self.todos_melhores_fitness = []
        self.detectores = []
        self.total_detectores_por_geracao = []
        #self.fitness_todos_detectores = []

    def inicia(self):
        populacao = self.gera_populacao()
        self.avalia(populacao)
        for _ in range(self.geracao_parada):
        #count = 0
        #while len(self.detectores) < 3:
            #print("\npopulacao  - fitness")
            #print(populacao)
            nova_pop = self.reproducao(populacao)
            self.avalia(nova_pop)
            #count += 1
            # print("\npopulacao  - fitness")
            # print(populacao)
        #print('fitness todos detectores')
        #print(self.fitness_todos_detectores)
        #print(count)
        self.escreve_txt()
        self.escreve_csv()
        #self.escreve_fitnnes_detectores()
        #print("Contagem\n")
        #print(Counter(list(self.detectores)))

        return "Processo finalizado com sucesso."

    def gera_populacao(self):
        populacao = [Individuo() for i in range(self.tam_pop)]
        self.melhor_individuo = populacao[0]
        return populacao

    def avalia(self, populacao):
        for individuo in populacao:
            individuo.fitness = self.calcula_fitness(individuo.cromossomo)
            #print(individuo.fitness)
            self.adiciona_detector(individuo)
            self.e_melhor(individuo)
        #self.media_fitness.append(self.media_todos_fitness(populacao))
        #self.todos_melhores_fitness.append(self.melhor_individuo.fitness)
        self.total_detectores_por_geracao.append(len(self.detectores))

    #def media_todos_fitness(self, populacao):
    #    contador_fitness = [individuo.fitness for individuo in populacao]
    #   return sum(contador_fitness) / len(populacao)
    '''
    def calcula_fitness(self, cromossomo):
        soma_fitness = 0
        #diff_50 = 0

        for individuo in self.amostra:
            # acumulador_diferenca = 0
            #condicao = np.array(cromossomo == individuo)
            #if condicao.all() != True:
            condicao = np.array_equal(cromossomo, individuo)
            if not condicao:
                soma_fitness += 1
            #diferenca = [0 if individuo[i] == cromossomo[i] else 1 for i in range(len(cromossomo))]
            #diferenca = np.sum(individuo != cromossomo)
            #if sum(diferenca) >= (len(individuo) * 0.25):
            #if diferenca >= (len(cromossomo) * 0.5):
            #    diff_50 += 1
            #else:
                #diff_50 -= 1

        #return (soma_fitness, diff_50)
        return soma_fitness
    '''
    def calcula_fitness(self, cromossomo):
        resultado = cromossomo == self.amostra
        if self.amostra.shape[1] in resultado.sum(axis=1):
            return -1
        return 1

    def adiciona_detector(self, individuo):
        if individuo.fitness == 1:
            if len(self.detectores) == 0:
                self.detectores.append(individuo.cromossomo)
            else:
                resultado = individuo.cromossomo == self.detectores
                if not self.amostra.shape[1] in resultado.sum(axis=1):
                    self.detectores.append(individuo.cromossomo)


    '''
    def adiciona_detector(self, individuo):
        if (individuo.fitness == self.amostra.shape[0]):  #  687  and (individuo.fitness[1] == self.amostra.shape[0]): 
            if len(self.detectores) == 0:
                self.detectores.append(individuo.cromossomo)
                #self.fitness_todos_detectores.append(individuo.fitness)
            else:
                i = 0
                for idv in self.detectores:
                    if (individuo.cromossomo != idv).any():
                        i += 1
                if i == len(self.detectores):
                    self.detectores.append(individuo.cromossomo)
                    #self.fitness_todos_detectores.append(individuo.fitness)
    '''

    '''
    def array_exists(self, individuo):
        exist = [True if np.array_equal(individuo, cromossomo) else False for cromossomo in self.detectores]
        return True in exist
    '''
    def e_melhor(self, individuo):
        if (self.melhor_individuo.fitness < individuo.fitness):
            self.melhor_individuo = individuo.copia()

    def quantidade(self):
        return int(self.tam_pop * self.taxa_cruzamento)

    def selecao(self, populacao):
        campeao = []
        for _ in range(self.quantidade()):
            selecionados = sample(populacao, 3)
            selecionados.sort(key=lambda individuo: individuo.fitness, reverse=True)
            campeao.append(selecionados[0])
        return campeao

    def cruzamento(self, selecionados):
        novos_individuos = []
        for _ in range(self.quantidade()):
            indv1, indv2 = sample(selecionados, 2)
            filho1, filho2 = self.um_ponto(indv1, indv2)
            novos_individuos.extend((filho1, filho2))
        return novos_individuos

    def um_ponto(self, indv1, indv2):
        ponto_corte = randint(0, indv1.tamanho)
        filho1 = list(indv1.cromossomo[:ponto_corte]) + list(indv2.cromossomo[ponto_corte:])
        filho2 = list(indv2.cromossomo[:ponto_corte]) + list(indv1.cromossomo[ponto_corte:])
        return (Individuo(np.array(filho1)), Individuo(np.array(filho2)))

    def mutacao(self, populacao):
        for individuo in populacao:
            self.inversao(individuo)

    def inversao(self, individuo):
        ref = individuo.cromossomo
        for i in range(individuo.tamanho):
            if random() <= self.taxa_mutacao:
                if ref[i] == 1:
                    individuo.cromossomo[i] = 0
                    break
                else:
                    individuo.cromossomo[i] = 1
                    break
    '''
    def inversao(self, individuo):
        #ref = individuo
        for valor in individuo.cromossomo:
            if random() <= self.taxa_mutacao:
                if valor == 1:
                    valor = 0
                else:
                    valor = 1
    '''
    def reproducao(self, populacao):
        populacao.sort(key=lambda individuo: individuo.fitness, reverse=True)
        selecionados = self.selecao(populacao)
        pop_temporaria = self.cruzamento(selecionados)
        nova_pop = pop_temporaria + populacao[self.quantidade():]
        self.mutacao(nova_pop)
        return nova_pop

    def escreve_txt(self):
        # with open("detectores150X86.txt", "w") as file:
        with open("/home/rui/PycharmProjects/projectRansomware/dataset_detector/detectores687X82_"+str(len(self.detectores))+"_.txt", "w") as file:
            # with open("teste_funcao.txt", "w") as file:
            # file.write(self.melhor_individuo)
            # file.write(self.melhor_individuo)
            # file.write("\n")
            # file.write("\n")
            # file.write("\n")
            # file.write("\n"+"="*40+ " POPULACAO "+"="*40+"\n")
            # for i in self.amostra:
            # file.write("\n"+str(np.array(i)) + "\n")
            # file.write("\n")
            # file.write("\n")
            # file.write("\n")
            # file.write("Cromossomo: " + str(self.melhor_individuo.cromossomo)+"\n")
            # file.write("Melhor Fitness: " +str(self.melhor_individuo.fitness)+"\n")
            '''
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n"+"="*40+ " DETECTORES "+"="*40+"\n")
            file.write("\n")
            file.write("\n")
            for i in self.detectores:
                file.write("\n" +str(i) + "\n")
            '''
            file.write("Total de detectores: " + "\n" + str(len(self.detectores)))
            file.write("\nTotal de dectores em cada geracao:")
            file.write("\n" + str(self.total_detectores_por_geracao))
            # file.write("Tempo de execução: " +str((fim-ini)))

    def escreve_csv(self):
        # pd.DataFrame(self.detectores).to_csv("detectores150X86.csv")
        pd.DataFrame(self.detectores).to_csv("/home/rui/PycharmProjects/projectRansomware/dataset_detector/detectores687X82_"+str(len(self.detectores))+"_.csv")

    '''
    def escreve_fitnnes_detectores(self):
        # with open("fitness.txt", "w") as file:
        with open("fitness2X6.txt", "w") as file:
            file.write("Fitness: \n" + str(self.fitness_todos_detectores))
    '''