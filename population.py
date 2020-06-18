import os, subprocess, sys, socket, time, struct, random, datetime

import constant, fitness, guy

class Genesis: 
    def Principle(self):
        self.create_guy = guy.Guy()
        generation = [[]]*constant.MAXPOPULATION
        for i in range(1, constant.MAXPOPULATION):
           generation[i].append(self.create_guy.create_Cromossome())
        print(len(generation))
        self.evaluation = fitness.Rating()
        self.evaluation.evaluation(generation)

x = Genesis()
x.Principle()
