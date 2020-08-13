import os, subprocess, sys, socket, time, struct, random, datetime

import constant, population

class Guy:
    def create_Cromossome(self): 
        cromossome = str()
        max_green_time = constant.CYCLE_TIME - (constant.YELLOW_TIME * 2) - (constant.MINFASE_TIME)
        total_period_time = constant.CYCLE_TIME - (constant.YELLOW_TIME * 2)

        if constant.CREATEGUY == 1:
            genes = random.randrange(0, max_green_time)
            genes_position = []

            for i in range (0, genes):
                pseudo_gene = random.randrange(0, total_period_time)

                while pseudo_gene in genes_position:
                    pseudo_gene = random.randrange(0, total_period_time)
                genes_position.append(pseudo_gene)

                for i in range(0, total_period_time):
                    if i in genes_position:
                        cromossome += str('1') 
                    else:
                        cromossome += str('0')
        return cromossome
    
