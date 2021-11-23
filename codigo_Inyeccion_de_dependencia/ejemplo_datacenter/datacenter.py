from pc import PC

class DataCenter():
    def __init__(self, servidores = []):
        self.servidores = servidores

    def __str__(self):
        lista_servidores = "Servidores\n"
        for i in range(len(self.servidores)):
            lista_servidores += f"\tservidor --> {i} {self.servidores[i]}\n"
        return lista_servidores

    @property
    def servidores(self):
        return self.__servidores

    @servidores.setter
    def servidores(self, value):
        self.__servidores = value

    def add_servidor(self, pc: PC ):
        self.__servidores.append(pc)
