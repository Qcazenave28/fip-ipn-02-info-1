from argparse import ArgumentTypeError
from enum import Enum

class Classification(Enum):
    POISSON = 0
    INSECTE = 1
    OISEAU = 2
    MAMIFERE = 3
    AMPHIBIEN = 4
    REPTILE = 5
    INVERTEBRE = 6

class Animal():
    _classification = None
    _name = ""

    def __init__(self, name, classification):
        self._name = name
        self._classification = classification

    @property
    def classification(self):
        return self._classification

    @property
    def name(self):
        return self._name

class Chat(Animal):
    _isCute = True

    def __init__(self, name):
        if not isinstance(name, str):
            raise ArgumentTypeError("must be a string!")

        super().__init__(name, Classification.MAMIFERE)