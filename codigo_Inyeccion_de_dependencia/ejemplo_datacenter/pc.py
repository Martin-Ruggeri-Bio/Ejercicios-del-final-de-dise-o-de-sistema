from micro import Micro
from mother import Mother
from ssd import SSD
from ram import RAM


class PC():
    def __init__(self, micro: Micro, mother: Mother, ssd: SSD, ram: RAM):
        self.micro = micro
        self.mother = mother
        self.ssd = ssd
        self.ram = ram

    def __str__(self):
        return 'MICRO - {} - MOTHER {} ssd {} ram {}'.format(self.micro, self.mother, self.ssd, self.ram)

    @property
    def micro(self):
        return self.__micro

    @micro.setter
    def micro(self, value):
        self.__micro = value

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        self.__mother = value

    @property
    def ssd(self):
        return self.__ssd

    @ssd.setter
    def ssd(self, value):
        self.__ssd = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        self.__ram = value
