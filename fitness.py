import os, subprocess, sys, socket, time, struct, random, datetime

import constant, guy, smartCities, population, runner

from population import Population 


def fitness ():
    evaluation = []*20
    for i in range(0, 20):
        evaluation[i] = runner.run(i)
    print(evaluation)

fitness()