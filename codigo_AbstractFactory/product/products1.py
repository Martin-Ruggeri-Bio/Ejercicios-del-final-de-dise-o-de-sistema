from abstract_product.abstract_product_A import (AbstractProductA,
                                                 AbstractProductB)


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
