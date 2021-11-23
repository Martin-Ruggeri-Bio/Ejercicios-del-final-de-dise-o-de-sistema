from abc import ABC, abstractmethod

class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self):
        pass

class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA):
        pass
