class Micro():
    def __init__(self, nucleo=0, marca='', arquitectura=''):
        self.nucleo = nucleo
        self.marca = marca
        self.arquitectura = arquitectura

    def __str__(self):
        return 'nucleo {} marca {} arquitectura {}'.format(self.nucleo, self.marca, self.arquitectura)

    def is_micro_x86(self):
        if self.arquitectura == 'x86':
            return True
        return False

    @property
    def nucleo(self):
        return self.__nucleo

    @nucleo.setter
    def nucleo(self, value):
        self.__nucleo = value

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

    @property
    def arquitectura(self):
        return self.__arquitectura

    @arquitectura.setter
    def arquitectura(self, value):
        self.__arquitectura = value
