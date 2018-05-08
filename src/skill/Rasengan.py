from .RasenganSprite import RasenganSprite

class Rasengan(RasenganSprite):

    def __init__(self, target):
        super().__init__(target)
        self.damage = 20
        self.hitted = False


    def getDamage(self):
        return self.damage



    def isHitted(self):
        return self.hitted

    def setHitted(self, hitted):
        self.hitted = hitted

