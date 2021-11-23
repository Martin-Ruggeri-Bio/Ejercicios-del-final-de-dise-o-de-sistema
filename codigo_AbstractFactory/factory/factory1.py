from abstract_factory.abstractFactory import AbstractFactory
from product.products1 import ConcreteProductA1, ConcreteProductB1


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()
