import numpy
import random
import benchmarks.functions as functions

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


creator.create("FitnessBenchmark"   , base.Fitness, weights=(-1.0,))
creator.create("IndividualBenchmark", list, fitness=creator.FitnessBenchmark)

def checkBounds(min, max):
    def decorator(func):
        def wrapper(*args, **kargs):
            offspring = func(*args, **kargs)
            for child in offspring:
                for i in range(len(child)):
                    if child[i] > max:
                        child[i] = max
                    elif child[i] < min:
                        child[i] = min
            return offspring
        return wrapper
    return decorator

def runGA(bounds, probsize, popsize, func, iters, reps):
    toolbox = base.Toolbox()

    # Attribute generator 
    toolbox.register("attr_bool", random.uniform, bounds[0], bounds[1])

    # Structure initializers
    toolbox.register("individual", tools.initRepeat, creator.IndividualBenchmark, toolbox.attr_bool, probsize)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", func)
    toolbox.register("select"  , tools.selTournament, tournsize=3)
    toolbox.register("mate"    , tools.cxBlend, alpha=0.5)
    toolbox.register("mutate"  , tools.mutGaussian, mu=0, sigma=2, indpb=0.2)

    toolbox.decorate("mate"  , checkBounds(bounds[0], bounds[1]))
    toolbox.decorate("mutate", checkBounds(bounds[0], bounds[1]))

    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    results = []

    for i in range(reps):
        _, _ = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=iters, 
                                       stats=stats, halloffame=hof, verbose=False)
        results.append(hof[0].fitness.values[0])

    return results

def main():
    resultsGA = runGA((0, 10), 20, 50, functions.sphere, 50, 10)
    print(resultsGA)
    pass

if __name__ == "__main__":
    main()
    pass