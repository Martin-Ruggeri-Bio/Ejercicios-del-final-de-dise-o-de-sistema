from abstract_factory.abstractFactory import AbstractFactory
from product.products2 import ConcreteProductA2, ConcreteProductB2


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()
