from abc import ABC, abstractmethod

from ui_lib import BoutonWeb


class Dessinable(ABC):
    @abstractmethod
    def dessiner(self) -> None: ...


# Ta propre classe : tu peux modifier son code, pas de problème
class Cercle(Dessinable):  # ← héritage obligatoire
    def dessiner(self) -> None:
        print("Patrick dessine un cercle.")


def afficher_element(element: Dessinable) -> None:
    element.dessiner()


afficher_element(Cercle())  # OK
afficher_element(BoutonWeb())  # Pylance se plaint : BoutonWeb n'est pas un Dessinable
