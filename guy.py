import os, subprocess, sys, socket, time, struct, random, datetime

import constante
class Guy: 

    def create_Cromossome(self): 
        cromossome = str()
        max_green_time = constante.CYCLE_TIME - (constante.YELLOW_TIME * 2) - (constante.MINFASE_TIME)
        total_fase_time = constante.CYCLE_TIME - (constante.YELLOW_TIME * 2)

        if constante.CREATEGUY == 1:
            genes = random.randrange(0, max_green_time)
            genes_position = []

            for i in range (0, genes):
                pseudo_gene = random.randrange(0, total_fase_time)

                while pseudo_gene in genes_position:
                    pseudo_gene = random.randrange(0, total_fase_time)
                genes_position.append(pseudo_gene)

                for i in range(0, total_fase_time):
                    if i in genes_position:
                        cromossome += str('1')
                    else:
                        cromossome += str('0')
        print (len(cromossome))
        return cromossome
    
    def Genesis(self):
        generation = [[]]*20
        print(generation)
        for i in range(0, constante.MAXPOPULATION):
            print(i)
            generation[i].append(self.create_Cromossome())
        print(generation)
    
x = Guy()
x.Genesis()
