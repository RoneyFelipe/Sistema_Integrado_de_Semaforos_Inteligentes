import os, subprocess, sys, socket, time, struct, random, datetime

import constant, guy

class Population:
    def __init__(self):
        self.create_guy = guy.Guy()

    def Principle(self):
        generation = [[]]*constant.MAXPOPULATION
        print(generation)
        for i in range(0, constant.MAXPOPULATION):
           generation[i] = self.create_guy.create_Cromossome()
           print(i)
        print(generation)
        

