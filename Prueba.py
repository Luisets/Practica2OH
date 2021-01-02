from group06.EA import EA
import numpy as np
import pyade
from scipy.optimize import rosen, differential_evolution
import benchmarks.functions as function
from deap import algorithms
import pyade.sade as sade
def f(x):
    return -sum(x)
    pass

import pyade.sade as sade

def runSADE(bounds, probsize, popsize, func, iters, reps):
    params = sade.get_default_params(dim=probsize)
    params['bounds'         ] = np.array([[bounds[0], bounds[1]]] * probsize)
    params['max_evals'      ] = popsize*iters
    params['population_size'] = popsize
    params['func'           ] = func
    results = []

    for i in range(reps):
        _, fitness = sade.apply(**params)
        results.append(fitness)

    return results


def main():
    # mybounds = [(0, 100)] * 20
    # myea = EA(f, mybounds, 100)
    # myea.run(200)
    # bestSol = myea.best()
    # print("ultima pob")
    # myea.currentGen.print()
    # print("Best Genoma:")
    # print("\tSolution: {}, Fitness: {}".format(bestSol.solution, bestSol.fitnes))
    # bounds = [(0, 10)]*20
    # res = differential_evolution(function.sphere, bounds, strategy="rand1exp", popsize=50, polish=False, maxiter=50)
    # print(res.fun)
    res = runSADE((0, 10), 20, 50, function.sphere, 50, 10)
    print(res)
    pass

if __name__ == "__main__":
    main()
    pass

