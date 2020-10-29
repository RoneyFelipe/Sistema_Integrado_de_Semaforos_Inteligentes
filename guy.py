import os, subprocess, sys, socket, time, struct, random, datetime #Importação das dependências necessárias

import constant, population #Importação dos arquivos constant.py e population.py

class Guy:
    def create_Cromossome(self): 
        num_zeros = 0 #Criação da variável para conter a quantidade de algarismos uns da solução
        num_one = 0 #Criação da variável para conter a quantidade de algarismos zeros da solução
        cromossome = str() #Criação da variável que irá abrigar os indivíduos
        max_green_time = constant.CYCLE_TIME - (constant.YELLOW_TIME * 2) - (constant.MINFASE_TIME) #Determina o tempo máximo da fase verde do semáforo
        total_period_time = constant.CYCLE_TIME - (constant.YELLOW_TIME * 2) #Determina o tempo máximo do ciclo do semáforo

        genes = random.randrange(0, max_green_time) #Gera um número aleátorio entre 0 e o tempo máximo de verde de cada fase do semáforo
        genes_position = [] #Cria um vetor que irá armazenar os valores gerados entre 0 e o tempo total do ciclo semafórico

        for i in range (0, genes): 
            pseudo_gene = random.randrange(0, total_period_time) #Gera um número aleátorio entre 0 e o tempo máximo do ciclo do semáforo

            while pseudo_gene in genes_position:
                pseudo_gene = random.randrange(0, total_period_time) #Gera um número aleátorio entre 0 e o tempo máximo do ciclo do semáforo
            genes_position.append(pseudo_gene) #Adiciona o gene gerado ao vetor de posicionamento de genes

        for i in range(0, total_period_time):
            if i in genes_position:
                cromossome += str('1') #Insere o algarismo 1 no indivíduo
                num_one = num_one + 1 #Aumenta em 1 a quantidade de algarismos zeros
            else:
                cromossome += str('0') #Insere o algarismo 0 no indivíduo
                num_zeros = num_zeros + 1 #Aumenta em 1 a quantidade de algarismos uns
                        
        return cromossome,num_one,num_zeros #Retorna o indivíduo; a quantidade de algarismos um; e a quantidade de algarismos zeros
