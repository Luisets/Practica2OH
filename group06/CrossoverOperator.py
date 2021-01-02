from abc import ABCMeta, abstractmethod

class CrossoverOperator(metaclass = ABCMeta):

    @abstractmethod
    def apply(self, genomes):
        pass

    pass
