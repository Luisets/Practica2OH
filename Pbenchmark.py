from group06.EA import EA
import benchmarks.functions as benchmark

def f(x):
    return sum(x)
    pass

# 
def main():
    mybounds = [(0, 1)] * 20
    myea = EA(benchmark.sphere, mybounds, 50)
    for x in range(0, 10):
        myea.run(500)
        bestSol = myea.best()
        print("Best Genoma:")
        print("\tSolution {}: {}, Fitness: {}".format(x + 1, bestSol.solution, bestSol.fitnes))
    pass

if __name__ == "__main__":
    main()
    pass

benchmark.schaffer