import unittest
from arv import Fisk
from arv import Grädda
from arv import Aborre


enfisk = Fisk()
engrädda = Grädda()
enaborre = Aborre()


assert(type(enfisk)==Fisk)
assert(isinstance(enaborre, Fisk))