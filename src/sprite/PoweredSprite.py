from .ControllableSprite import ControllableSprite

class PoweredSprite(ControllableSprite):

    def __init__(self):
        super().__init__()
        self.leftSpecailMove1Frames = []
        self.rightSpecailMove1Frames = []

        self.inSM1 = False
        self.inSM1Hit = False
        self.currentSkillObject = None

        self.skillAnimation = None
        self.skill1AnimationCallback = None


    def animateSpecialMove1(self, skillAnimation):

        self.context.activeSpriteList.add(skillAnimation.getAnimationTarget())

        self.skillAnimation = skillAnimation
        self.skillAnimation.setTargetAnimation(self.rightSpecailMove1Frames, self.leftSpecailMove1Frames)
        self.currentSkillObject = skillAnimation.getAnimationTarget()

        self.inSM1 = True


    def update(self, updateTime):
        super().update(updateTime)

        if self.inSM1:
            self.currentSkillObject.setRect(self.rect)

            self.skill1AnimationCallback(updateTime)

            self.currentSkillObject.setSkillDirection(self.getDirection())
            self.currentSkillObject.update(updateTime)
            image = self.skillAnimation.animate(updateTime, self.getDirection(), self)

            if image == None:
                print("OVER")
                self.setIdle(True)
                self.inSM1 = False
                self.context.activeSpriteList.remove(self.currentSkillObject)

            else:
                self.image = image

        elif self.inSM1Hit:
            print("Hiittt")
            image = self.skillAnimation.hit(self, updateTime, self.getDirection())

            if image == None:
                print("OVER")
                self.setIdle(True)
                self.inSM1Hit = False
                self.context.activeSpriteList.remove(self.currentSkillObject)

            else:
                self.image = image

    def setLeftSpecialMove1Frames(self, lsm1f):
        self.leftSpecailMove1Frames = lsm1f

    def setRightSpecialMove1Frames(self, rsm1f):
        self.rightSpecailMove1Frames = rsm1f

