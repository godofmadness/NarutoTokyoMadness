from .ChidoriSprite import ChidoriSprite

class Chidori(ChidoriSprite):

    def __init__(self, target):
        super().__init__(target)
        print("CHIDORY INITIALIZATION, RECT: " + str(self.rect))
        self.damage = 20
        self.hitted = False


    def getDamage(self):
        return self.damage



    def isHitted(self):
        return self.hitted

    def setHitted(self, hitted):
        self.hitted = hitted

