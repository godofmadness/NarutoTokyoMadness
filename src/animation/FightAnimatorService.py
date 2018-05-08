from ..constants.Contstants import *
from ..logger.LoggerFactory import LoggerFactory

class FightAnimatorService:

    def __init__(self, rbaseAttackFrames, lbaseAttackFrames, attackIndexes, comboBreakTime):
        self.log = LoggerFactory.getStreamLogger(__name__)

        self.comboBreakTime = comboBreakTime
        self.rbaseAttackFrames = rbaseAttackFrames
        self.lbaseAttackFrames = lbaseAttackFrames
        self.attackIndexes = attackIndexes
        self.currentFrameIndex = 0
        self.currentFrame = None
        self.lastAttackTime = 0
        self.lastFrameUpdateTime = 0
        self.currentBasicAttack = 0


    def attack(self, attackTime):
        # break combo
        # self.log.debug("length" + str(self.attackIndexes))
        if attackTime - self.lastAttackTime > self.comboBreakTime or self.currentBasicAttack >= len(self.attackIndexes) - 1:
            self.currentBasicAttack = 0
            self.currentFrameIndex = 0
        else:
            self.currentBasicAttack += 1

        # self.log.debug("current attack " + str(self.currentBasicAttack))

        self.lastAttackTime = attackTime



    def updateAttack(self, updateTime, direction):
        # # change frame
        if updateTime - self.lastFrameUpdateTime > BASIC_ATTACK_FRAMERATE and self.currentFrameIndex <= self.attackIndexes[self.currentBasicAttack]:
            if direction == "R":
                image = self.rbaseAttackFrames[self.currentFrameIndex]
            else:
                image = self.lbaseAttackFrames[self.currentFrameIndex]
            #
            self.currentFrame = image
            self.lastFrameUpdateTime = updateTime
            self.currentFrameIndex += 1

        elif self.currentFrameIndex > self.attackIndexes[self.currentBasicAttack] and updateTime - self.lastFrameUpdateTime > BASIC_ATTACK_FRAMERATE:
            return None

        return self.currentFrame
