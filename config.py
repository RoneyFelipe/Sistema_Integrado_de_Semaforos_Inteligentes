import os, subprocess, sys, socket, time, struct, random, datetime

class Config: 

    def __init__(self): 
        #Constantes de Tempo
        self.SIMULATION_TIME = 720
        self.CYCLE_TIME = 60
        self.OFFSET = 10
        self.IGNORECYCLES = 2
        self.YELLOW_TIME = 2
        self.MINFASE_TIME = 2

        #Contantes Geneticas
        self.MAXPOPULATION = 20
        self.MAXGENERATIONS = 10
        self.MUTATIONRATE = 0.3
        self.MUTATIONGENERATE = 0.05
        self.CREATEGUY = 1

    def create_Cromossome(self): 
        cromossome = str()
        max_green_time = self.CYCLE_TIME - (self.YELLOW_TIME * 2) - (self.MINFASE_TIME)
        total_fase_time = self.CYCLE_TIME - (self.YELLOW_TIME * 2)

        if self.CREATEGUY == 1:
            genes = random.randrange(0, max_green_time)
            genes_position = []

            for i in range (0 ,genes):
                pseudo_gene = random.randrange(0, total_fase_time)

                while pseudo_gene in genes_position:
                    pseudo_gene= random.randrange(0, total_fase_time)

                genes_position.append(pseudo_gene)
            
                for i in range(0, total_fase_time):
                    if i in genes_position:
                        cromossome += str("1")
                    else:
                        cromossome += str("0")
        print (cromossome)
        return cromossome
        
x = Config()
x.create_Cromossome()
