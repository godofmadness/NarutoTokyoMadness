from .Heroes import Heroes
from .Naruto import Naruto
from .NarutoFactory import NarutoFactory
from .SasukeFactory import SasukeFactory

class AbstractHeroFactory:


    def getHero(self, type):
        if (type == Heroes.NARUTO):
            return NarutoFactory.getInstance()
        if (type == Heroes.SASUKE):
            return SasukeFactory.getInstance()

