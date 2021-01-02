from abc import ABCMeta, abstractmethod


class SelectionOperator(metaclass = ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def apply(self, genomes, i):
        pass

    pass
