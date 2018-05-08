from ..TimingAnimationService  import TimingAnimationService
class ChidoriAnimation:


    def __init__(self, chidory, frameRate, startTime):
        self.frameRate = frameRate
        self.chidorySprite = chidory

        # self.chidoryAnimationFrames = self.chidorySprite.getFrames()

        self.leftTargetAnimation = None
        self.rightTargetAnimation = None

        self.animationLastUpdateTime = 0
        self.animationStartTime = startTime
        self.moveStartTime = startTime + 2000

        self.chidoryIdleTime = 0.2
        self.chidoryMoveTime = 2.5 - 1

        self.hitTime = 1


        self.hitStartTime = None
        self.runAnimationService = None
        self.hitAnimationService = None


    def animate(self, updateTime, direction, target):
        #animate target and skill here

        # idle chidory state


        if updateTime - self.animationStartTime < self.chidoryIdleTime and target.isOnGround():
            if direction == "R":
                return self.rightTargetAnimation[0]
            else:
                return self.leftTargetAnimation[0]


        # if updateTime - self.animationStartTime < self.chidoryIdleTime and updateTime - self.animationStartTime < self.chidoryMoveTime:
        self.chidorySprite.setInMoveState(True)
        # move chidory state
        print(target)
        if direction == "R":
            target.xVelocity = 30
        else:
            target.xVelocity = -30
        return self.runAnimationService.updateAnimation(updateTime, direction)

        # elif updateTime - self.animationStartTime > self.chidoryMoveTime and updateTime - self.animationStartTime < self.hitTime:
        #     self.chidorySprite.setInMoveState(False)
        #     self.chidorySprite.setInHitState(True)
        #     target.xVelocity = 0
        #
        #     return self.hitAnimationService.updateAnimation(updateTime, direction)

        # elif updateTime - self.animationStartTime > self.hitTime:
        #     print("over")
        #     return None
        #



    def hit(self, target, updateTime, direction):
        print("hit animation")
        if updateTime - self.hitTime < self.hitStartTime:
            self.chidorySprite.setInMoveState(False)
            self.chidorySprite.setInHitState(True)
            target.xVelocity = 0

            return self.hitAnimationService.updateAnimation(updateTime, direction)

    def getAnimationTarget(self):
        return self.chidorySprite

    def setTargetAnimation(self, rta, lta):
        self.leftTargetAnimation = lta
        self.rightTargetAnimation = rta
        self.configAniamtionService()

    def setHitStartTime(self, time):
        self.hitStartTime = time


    def configAniamtionService(self):
        lta = list.copy(self.leftTargetAnimation)
        rta = list.copy(self.rightTargetAnimation)
        self.hitAnimationService = TimingAnimationService([lta.pop(len(lta) - 1)], [rta.pop(len(rta) - 1)], self.frameRate)

        lta.remove(lta[len(lta) - 1])
        lta.remove(lta[0])

        rta.remove(rta[len(rta) - 1])
        rta.remove(rta[0])

        self.runAnimationService = TimingAnimationService(lta, rta, self.frameRate)

