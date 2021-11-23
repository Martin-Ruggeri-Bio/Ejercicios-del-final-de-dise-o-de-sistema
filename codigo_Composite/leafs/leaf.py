from components.component import Component

class LeafElement(Component):
    '''Clase que representa objetos en la parte inferior o Hoja del árbol de jerarquía.'''
    
    def __init__(self, *args):
        ''''Toma el primer argumento posicional y lo asigna a la variable miembro "posición".'''
        self.position = args[0]
    
    def is_composite(self):
        return False

    def showDetails(self):
        '''Imprime la posición del elemento hijo.'''
        print("\t", end ="")
        print(self.position)