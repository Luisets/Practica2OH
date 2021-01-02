from abc import ABCMeta, abstractmethod

class MutationOperator(metaclass = ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def apply(self, genomes):
        pass

    pass
