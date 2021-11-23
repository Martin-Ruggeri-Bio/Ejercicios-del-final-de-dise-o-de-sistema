class Mother():
    def __init__(self, marca: str):
        self.marca = marca

    def __str__(self):
        return 'Marca - {}'.format(self.marca)
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value
