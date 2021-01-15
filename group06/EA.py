from group06.Population import Population as Population
from group06.Genome import Genome as Genome
from group06.operadores.Rand1 import Rand1 as Mutation
from group06.operadores.Exponential import Exponential as Crossover
from group06.operadores.Uniform import Uniform as Selection
from group06.operadores.Elitist import Elitist as Replacement
import numpy as np


class EA(object):
    def __init__(self, f_fitnes, bounds, populationSize):
        Genome.set_f_fitnes(f_fitnes)
        self.populationSize = populationSize
        self.nVar = len(bounds)
        self.min = bounds[0][0]
        self.max = bounds[0][1]
        self.f_fitnes = f_fitnes
        pass

    def run(self, iteraciones):
        # conseguimos la poblacion inicial
        self.currentGen = Population(self.f_fitnes, self.populationSize)
        self.initPopulation()
        trialGen = Population(self.f_fitnes, self.populationSize)
        selector = Selection()
        # mutator = Mutation(self.f_fitnes)
        mutator = Mutation()
        replacer = Replacement()
        # crossover = Crossover(self.f_fitnes)
        crossover = Crossover()
        for n_gen in range(0, iteraciones):
            trialGen.clear()
            for n_indiv in range(0, self.populationSize):
                selection = selector.apply(self.currentGen, n_indiv)
                target = selection[0]
                mutation = self.ensureBounds(mutator.apply(selection))
                trial = crossover.apply([target, mutation])
                trialGen.add(trial)
                pass
            self.currentGen = replacer.apply(self.currentGen, trialGen)
            pass
        self.currentGen.ascOrdered()
        pass

    def ensureBounds(self, genome):
        vInBounds = []
        for value in genome.solution:
            if value < self.min:
                vInBounds.append(self.min)
                pass
            elif value > self.max:
                vInBounds.append(self.max)
                pass
            else:
                vInBounds.append(value)
                pass
            pass
        npArray = np.array(vInBounds)
        return Genome(npArray)
        pass

    def initPopulation(self):
        for i in range(0, self.populationSize):
            solution = np.random.uniform(self.min, self.max, self.nVar)
            # self.currentGen.add(Genome(solution, self.f_fitnes(solution)))
            self.currentGen.add(Genome(solution))
            pass
        pass

    def best(self):
        return self.currentGen.getGenome(0)
        pass
