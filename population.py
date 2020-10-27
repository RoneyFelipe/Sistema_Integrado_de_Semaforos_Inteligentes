import os, subprocess, sys, socket, time, struct, random, datetime #Importação das dependências necessárias

import constant, guy #Importação dos arquivos guy.py e constant.py

class Population:
    def __init__(self):
        self.create_guy = guy.Guy() #Criação de um objeto da classe Guy do arquivo guy.py

    def Principle(self):
        generation = [[]]*constant.MAXPOPULATION #Criação de uma matriz com o tamanho da constant.MAXPOPULATION (Ou seja, 20)
        for i in range(0, constant.MAXPOPULATION): # Estrutura de repetição que será executada de 0 à constant.MAXPOPULATION (Ou seja, 20) 
           generation[i] = self.create_guy.create_Cromossome() # Irá executar o metodo creat_Cromossome gerando um novo indivíduo que será atribuido a posição I da matriz
        print(generation)
        return generation #Retorna a matriz com todas as posições preenchidas por indivíduos
        