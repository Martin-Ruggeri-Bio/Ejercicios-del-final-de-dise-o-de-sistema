from abstract_product.abstract_product_A import AbstractProductA, AbstractProductB


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
