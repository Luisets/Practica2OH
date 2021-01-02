from warnings import simplefilter


class Genome:
    # def __init__(self, solution, fitnes):
    def __init__(self, solution):
        self.solution = solution
        # self.fitnes = fitnes
        self.fitnes = Genome.f_fitnes(solution)
        pass

    def getSize(self):
        return len(self.solution)

    def getValue(self, i):
        return self.solution[i]

    def getSolution(self):
        return self.solution
        pass

    def getFitnes(self):
        return self.fitnes
        pass

    def set_f_fitnes(fun):
        Genome.f_fitnes = fun
    pass
