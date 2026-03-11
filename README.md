# Exemple — Problème de typage statique avec une librairie externe

Cet exemple illustre un problème courant en Python : **une classe externe** possède la bonne interface (method `dessiner()`), mais **n'hérite pas** de la classe abstraite attendue (`Dessinable`). L'analyseur statique (Pylance/mypy) se plaint, même si le code fonctionne parfaitement à l'exécution grâce au duck typing.

## Structure

```
exemple_duck/
├── main.py          # Point d'entrée, contient Dessinable, Cercle et l'utilisation
└── ui_lib/
    └── __init__.py  # Simule une librairie externe (BoutonWeb)
```

## Le problème

```python
class Dessinable(ABC):
    @abstractmethod
    def dessiner(self) -> None: ...

def afficher_element(element: Dessinable) -> None:
    element.dessiner()

afficher_element(BoutonWeb())  # ⚠️ Pylance se plaint
```

`BoutonWeb` (librairie externe) a bien une méthode `dessiner()`, mais n'hérite pas de `Dessinable`. On ne peut pas modifier son code source.

# duck-typing-typage-statique
