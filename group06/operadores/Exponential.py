from numpy import random
from group06.CrossoverOperator import CrossoverOperator
from group06.Genome import Genome
import numpy as np


class Exponential(CrossoverOperator):

    CR = 0.40

    def __init__(self):
        pass

    def apply(self, genomes):
        target = genomes[0]
        mutant = genomes[1]
        trial = np.copy(target.getSolution())
        
        j = np.random.randint(target.getSize())
        cont = 0
        while True:
            rand = random.uniform(0, 1)
            if rand >= Exponential.CR or cont >= target.getSize():
                break
            trial[j] = mutant.getValue(j)
            cont += 1
            j = (j + 1) % target.getSize()
        return Genome(trial)

    pass
