import os, subprocess, sys, socket, time, struct, random, datetime

import constant, guy, fitness


class Genesis:
    def __init__(self):
        self.create_guy = guy.Guy()
        self.test = fitness.test()

    def Principle(self):
        generation = [[]]*constant.MAXPOPULATION
        for i in range(1, constant.MAXPOPULATION):
           generation[i].append(self.create_guy.create_Cromossome())
        print(len(generation))
        self.test.evaluation(generation)

x = Genesis()
x.Principle()
