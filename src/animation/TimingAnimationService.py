class TimingAnimationService:

    def __init__(self, leftf, rightf, frameRate):
        self.leftf = leftf
        self.rightf = rightf
        self.frameRate = frameRate
        self.lastUpdatetime = 0
        self.currentActiveFrameIndex = -1
        self.curretFrame = None

    def clear(self):
        self.lastUpdatetime = 0
        self.currentActiveFrameIndex = -1
        self.curretFrame = None

    def updateAnimation(self, updateTime, direction):


        if direction == "R" and updateTime - self.lastUpdatetime > self.frameRate:


            if self.currentActiveFrameIndex == len(self.leftf) - 1:
                self.currentActiveFrameIndex = 0
            else:
                self.currentActiveFrameIndex += 1

            self.lastUpdatetime = updateTime
            self.curretFrame = self.rightf[self.currentActiveFrameIndex]

        elif direction == "L" and updateTime - self.lastUpdatetime > self.frameRate:

            if self.currentActiveFrameIndex == len(self.leftf) - 1:
                self.currentActiveFrameIndex = 0
            else:
                self.currentActiveFrameIndex += 1
            self.lastUpdatetime = updateTime
            self.curretFrame = self.leftf[self.currentActiveFrameIndex]


        return self.curretFrame

    def lastFrame(self):
        return self.currentActiveFrameIndex == len(self.leftf) + 1