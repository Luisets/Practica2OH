from abc import ABCMeta, abstractmethod


class ReplacementOperator(metaclass = ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def apply(self, poblacionGenomas1, poblacionGenomas2):
        pass

    pass
