# Exemple — Du typage nominal au typage structurel avec `Protocol`

Cet exemple illustre un problème courant en Python et sa solution.

**Le problème :** une classe externe possède la bonne interface (méthode `dessiner()`), mais **n'hérite pas** de la classe abstraite attendue (`ABC`). L'analyseur statique (Pylance/mypy) se plaint, même si le code fonctionne parfaitement à l'exécution grâce au duck typing.

**La solution :** remplacer `ABC` par `typing.Protocol` pour passer du **typage nominal** au **typage structurel**.

## Structure

```
exemple_duck/
├── main.py          # Point d'entrée : définit Dessinable (Protocol), Cercle, et l'utilisation
└── ui_lib/
    └── __init__.py  # Simule une librairie externe (BoutonWeb) — code non modifiable
```

## Le problème (avec ABC)

```python
from abc import ABC, abstractmethod

class Dessinable(ABC):
    @abstractmethod
    def dessiner(self) -> None: ...

def afficher_element(element: Dessinable) -> None:
    element.dessiner()

afficher_element(BoutonWeb())  # ⚠️ Pylance se plaint
```

`BoutonWeb` (librairie externe) a bien une méthode `dessiner()`, mais n'hérite pas de `Dessinable`. On ne peut pas modifier son code source.

## La solution (avec Protocol)

```python
from typing import Protocol

class Dessinable(Protocol):
    def dessiner(self) -> None: ...

def afficher_element(element: Dessinable) -> None:
    element.dessiner()

afficher_element(Cercle())     # ✅ OK
afficher_element(BoutonWeb())  # ✅ OK — sans rien changer dans ui_lib !
```

Avec `Protocol`, Python vérifie la **forme** (les méthodes présentes) plutôt que la **généalogie** (l'héritage). C'est le duck typing formalisé : *"Si ça marche comme un canard, c'est un canard."*

## Concepts clés

| | `ABC` | `Protocol` |
|---|---|---|
| Type de vérification | Nominale (héritage explicite) | Structurelle (forme de l'interface) |
| Modifiable tiers ? | Non requis | Non requis ✅ |
| Compatibilité statique | Héritage obligatoire | Méthodes suffisantes ✅ |