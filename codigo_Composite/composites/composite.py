from components.component import Component


class CompositeElement(Component):
    '''Clase que representa objetos en cualquier nivel de la jerarquía
     árbol a excepción de la parte inferior o el nivel de la hoja. Mantiene al niño
      objetos agregándolos y eliminándolos de la estructura de árbol.'''
  
    def __init__(self, *args):
        '''Toma el primer argumento posicional y lo asigna a miembro
         variable "posición". Inicializa una lista de elementos secundarios.'''
        self.position = args[0]
        self.children = []

    def is_composite(self):
        return True

    def add(self, child):
        '''Agrega el elemento secundario proporcionado a la lista de elementos secundarios
         elementos "niños"..'''
        self.children.append(child)

    def remove(self, child):
        '''Elimina el elemento secundario proporcionado de la lista de
        elementos de los niños "niños".'''
        self.children.remove(child)
  
    def showDetails(self):
        '''Imprime primero los detalles del elemento componente. Luego,
        itera sobre cada uno de sus hijos, imprime sus detalles por
        llamando a su método showDetails ()'''
        print(self.position)
        for child in self.children:
            print("\t", end ="")
            child.showDetails()
