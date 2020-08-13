import os, subprocess, sys, socket, time, struct, random, datetime

import constant, guy

class Population:
    def __init__(self):
        self.create_guy = guy.Guy()

    def Principle(self):
        generation = [[]]*constant.MAXPOPULATION
        for i in range(1, constant.MAXPOPULATION):
           generation[i].append(self.create_guy.create_Cromossome())
        print(generation)

