from ..TimingAnimationService  import TimingAnimationService
class RasenganAnimation:


    def __init__(self, rasengan, frameRate, startTime):
        self.frameRate = frameRate
        self.rasenganSprite = rasengan

        # self.chidoryAnimationFrames = self.chidorySprite.getFrames()

        self.leftTargetAnimation = None
        self.rightTargetAnimation = None

        print("SETTING ANIMATION START TIME " + str(startTime))
        self.animationLastUpdateTime = 0
        self.animationStartTime = startTime
        self.moveStartTime = startTime + 2000


        self.rasenganIdleTime = 3
        self.hitTime = 1


        self.hitStartTime = None
        self.runAnimationService = None
        self.hitAnimationService = None


    def animate(self, updateTime, direction, target):
        #animate target and skill here

        # idle chidory state
        # todo remove
        # print("IS GROUND = " + str(target.isOnGround()))
        print("UPDATE TIME RASENGAN ANIATMIATN" + str(updateTime))
        print("START TIME " + str(self.animationStartTime))
        if updateTime - self.animationStartTime < self.rasenganIdleTime and target.isOnGround():
            print("IDLE ANIMATION OF RASENGAN")
            return self.idleAnimationService.updateAnimation(updateTime, direction)
        # /todo remove


        # if updateTime - self.animationStartTime < self.chidoryIdleTime and updateTime - self.animationStartTime < self.chidoryMoveTime:
        self.rasenganSprite.setInMoveState(True)
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
            self.rasenganSprite.setInMoveState(False)
            self.rasenganSprite.setInHitState(True)
            target.xVelocity = 0


            return self.hitAnimationService.updateAnimation(updateTime, direction)

    def getAnimationTarget(self):
        return self.rasenganSprite

    def setTargetAnimation(self, rta, lta):
        self.leftTargetAnimation = lta
        self.rightTargetAnimation = rta
        self.configAniamtionService()

    def setHitStartTime(self, time):
        self.hitStartTime = time


    def configAniamtionService(self):
        lta = list.copy(self.leftTargetAnimation)
        rta = list.copy(self.rightTargetAnimation)
        self.idleAnimationService = TimingAnimationService(lta[1:4], rta[1:4], self.frameRate)
        self.hitAnimationService = TimingAnimationService([lta[len(rta) - 1]], [rta[len(rta) - 1]], self.frameRate)

        self.runAnimationService = TimingAnimationService([lta[4]], [rta[4]], self.frameRate)

