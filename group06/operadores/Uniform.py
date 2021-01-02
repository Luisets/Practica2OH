from group06.SelectionOperator import SelectionOperator
import numpy as np

class Uniform(SelectionOperator):
    
    def apply(self, population, i):
        selection = [population.getGenome(i)]
        while len(selection) < 4:
            rand = np.random.randint(population.getSize())
            if rand != i:
                selection.append(population.getGenome(rand))
            pass
        pass
        return selection
    pass
