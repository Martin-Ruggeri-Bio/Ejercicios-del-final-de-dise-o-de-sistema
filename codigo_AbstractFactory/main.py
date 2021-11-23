from factory.factory1 import ConcreteFactory1
from factory.factory2 import ConcreteFactory2
from client.cliente_code import client_code


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
