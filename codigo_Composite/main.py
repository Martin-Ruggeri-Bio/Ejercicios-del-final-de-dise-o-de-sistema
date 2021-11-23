from composites.composite import CompositeElement
from leafs.leaf import LeafElement

"""Aquí intentamos hacer una jerarquía organizacional con suborganización,
 que pueden tener suborganizaciones posteriores, tales como:
GeneralManager                      [Composite]
      Manager1                      [Composite]
              Desarrollador1a       [Leaf]
              Desarrollador1b       [Leaf]
      Manager2                      [Composite]
              Desarrollador2a       [Leaf]
              Desarrollador2b       [Leaf]"""

if __name__ == "__main__":
    # defino el nivel superior
    topLevelMenu = CompositeElement("GeneralManager")

    # defino los subniveles superior
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")

    # defino las hojas terminales
    # desarrolladores senior que por sus años de experiencia responden directamente al GeneralManager
    subMenuItema = LeafElement("DeveloperSeniora")
    subMenuItemb = LeafElement("DeveloperSeniorb")
    # desarrolladores juniors que por su falta de experiencia responden a un Manager
    subMenuItem1a = LeafElement("Developer1a")
    subMenuItem1b = LeafElement("Developer1b")
    subMenuItem2a = LeafElement("Developer2a")
    subMenuItem2b = LeafElement("Developer2b")
        
    # agrego los terminales a la rama del subnivel
    subMenuItem1.add(subMenuItem1a)
    subMenuItem1.add(subMenuItem1b)
    subMenuItem2.add(subMenuItem2a)
    subMenuItem2.add(subMenuItem2b)
  
    # agrego los subniveles y dos terminales a la rama master
    topLevelMenu.add(subMenuItema)
    topLevelMenu.add(subMenuItemb)
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    # Muestro la gerarquia
    topLevelMenu.showDetails()

    # asiendo un desarrolladora seniora a manager 3
    subMenuItem3 = CompositeElement("Manager3")
    topLevelMenu.remove(subMenuItema)

    # contrato un desarrollador junior a cargo del gerente 3
    subMenuItem3a = LeafElement("Developer3a")
    subMenuItem3.add(subMenuItem3a)

    # uno a la rama master
    topLevelMenu.add(subMenuItem3)

    print("Muestro la gerarquia modificada")
    topLevelMenu.showDetails()
