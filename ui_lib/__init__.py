# Simule une librairie externe dont tu n'as pas accès au code source.
# BoutonWeb a bien une méthode dessiner(), mais n'hérite pas de Dessinable.


class BoutonWeb:
    def dessiner(self) -> None:
        print("Sébastien affiche un bouton.")
