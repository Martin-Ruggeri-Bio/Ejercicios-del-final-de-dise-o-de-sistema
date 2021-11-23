class SSD():
    def __init__(self, marca: str, memoria: int):
        self.marca = marca
        self.memoria = memoria

    def __str__(self):
        return 'Marca - {} Memoria -{}GB'.format(self.marca, self. memoria)
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

    @property
    def memoria(self):
        return self.__memoria

    @memoria.setter
    def memoria(self, value):
        self.__memoria = value