from group06.Genome import Genome as Genome
import numpy as np


class Population:
    # crea la poblacion inicial
    def __init__(self, f_fitnes, size):
        self.solPopulation = []
        self.size = size
        self.f_fitnes = f_fitnes

    def getGenome(self, index):
        return self.solPopulation[index]
        pass

    def add(self, genome):
        self.solPopulation.append(genome)
        pass

    def remove(self, index):
        self.solPopulation.pop(index)
        pass

    def clear(self):
        self.solPopulation.clear()
        pass

    def ascOrdered(self):
        self.solPopulation.sort(key = Population.getFitnes)
        pass

    def desOrdered(self):
        self.solPopulation.sort(key = Population.getFitnes, reverse = True)
        pass

    def getSize(self):
        return self.size
        pass

    # Esto se utiliza solo para probar el resultado inicial y final 
    def print(self):
        for gen in self.solPopulation:
            print("\tsolution: {}, fitness: {}".format(gen.getSolution(), gen.getFitnes()))
            pass
        pass

    def getAverage(self):

        return
    def getFitnes(genome):
        return genome.fitnes
        pass