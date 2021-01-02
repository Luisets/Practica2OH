from ..MutationOperator import MutationOperator
from ..Genome import Genome as Genome

class Rand1(MutationOperator):
    F = 0.80
    # def __init__(self, f_fitnes):
    def __init__(self):
        # self.f_fitnes = f_fitnes
        pass
    
    def apply(self, genomes):
        v_1 = genomes[1].getSolution()
        v_2 = genomes[2].getSolution()
        v_3 = genomes[3].getSolution()
        mutant = v_1 + Rand1.F * (v_2 - v_3)
        return Genome(mutant)
        pass

    pass
