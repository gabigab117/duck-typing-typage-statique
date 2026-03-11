from abc import ABC, abstractmethod


class Dessinable(ABC):
    @abstractmethod
    def dessiner(self) -> None: ...


# Ta propre classe : tu peux modifier son code, pas de problème
class Cercle(Dessinable):  # ← héritage obligatoire
    def dessiner(self) -> None:
        print("Patrick dessine un cercle.")


# BoutonWeb vient d'une librairie externe (ui_lib)
# Son code source :
#
#   class BoutonWeb:
#       def dessiner(self) -> None:
#           print("Sébastien affiche un bouton.")
#
# Elle a bien une méthode dessiner(), mais elle n'hérite pas de Dessinable.
# L'analyseur statique se plaint, même si le code fonctionne parfaitement à l'exécution.

from ui_lib import BoutonWeb


def afficher_element(element: Dessinable) -> None:
    element.dessiner()


afficher_element(Cercle())  # OK
afficher_element(BoutonWeb())  # Pylance se plaint : BoutonWeb n'est pas un Dessinable
