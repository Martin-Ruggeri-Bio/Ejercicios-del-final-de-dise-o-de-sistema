from datacenter import DataCenter
from mother import Mother
from pc import PC
from micro import Micro
from ssd import SSD
from ram import RAM

if __name__ == '__main__':
    datacenter = DataCenter()

    datacenter.add_servidor(PC(Micro(2, 'Intel', 'x86'),Mother("LG"),SSD("Kingston", 500), RAM("ADATA", 8)))
    datacenter.add_servidor(PC(Micro(4, 'AMD', 'x64'),Mother("SAMSUNG"),SSD("Kingston", 1000), RAM("ADATA", 4)))

    print(datacenter)
