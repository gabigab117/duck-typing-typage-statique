from typing import Protocol
from ui_lib import BoutonWeb  # toujours la même lib externe, rien n'a changé de son côté

# Le contrat : "avoir une méthode dessiner()"
class Dessinable(Protocol):
    def dessiner(self) -> None:
        ...

# Ta propre classe, sans héritage forcé
class Cercle:
    def dessiner(self) -> None:
        print("Patrick dessine un joli cercle.")

# La fonction attend un Dessinable
def afficher_element(element: Dessinable) -> None:
    element.dessiner()

afficher_element(Cercle())     # L'analyseur statique est content
afficher_element(BoutonWeb())  # L'analyseur statique est content aussi et pourtant on n'a rien changé dans ui_lib