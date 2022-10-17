import unittest
from klass import Animal
from klass import Human


animal = Animal("Hunter")
human = Human("Hasan")

assert(animal.name == "Hunter")
assert(human.name == "Hasan")
