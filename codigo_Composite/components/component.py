from abc import ABC, abstractmethod

class Component(ABC):    
    @abstractmethod
    def is_composite(self):
        return False

    @abstractmethod
    def showDetails(self):
        pass
