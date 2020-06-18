import os, subprocess, sys, socket, time, struct, random, datetime

import constant, population, guy

class Rating:
    def evaluation(self,generation):
        generation = population.Genesis()
        individuals = generation
        couple = []
        selector = 0
        for x in [0,1]:
            roullete = float(0)
            for i in range (1,(len(individuals))):
                roullete = i*2
            rand = random.randrange(1, roullete)
            
            # for i in range(1, len(individuals)):
            #     selector += i*2
            #     if (rand > selector):
            #         continue
            #     couple.append(individuals.pop(i))
            #     break
