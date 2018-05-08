import pygame
from ..animation.TimingAnimationService import TimingAnimationService
from ..skill.SkillSprite import SkillSprite

class RasenganSprite(SkillSprite):

    def __init__(self, target):
        super().__init__()
        # self.frames = []

        self.rect = target.rect
        self.idleAnimationService = None
        self.moveAnimationService = None
        self.direction = None
        self.soundService = None
        self.leftFrames = []
        self.rightFrames = []

        self.inMoveState = False
        self.inHitState = False



    def update(self, updateTime):

        if self.inMoveState:
            self.image = self.moveAnimationService.updateAnimation(updateTime, self.direction)
        elif self.inHitState:
            self.image = self.hitAnimationService.updateAnimation(updateTime, self.direction)
        else:
            self.image = self.idleAnimationService.updateAnimation(updateTime, self.direction)


    def setImage(self, image):
        self.image = image

    def setFrames(self, frames):
        self.frames = frames

    def getFrames(self):
        return self.frames

    def setInMoveState(self, state):
        self.inMoveState = state

    def setInHitState(self, state):
        self.inHitState = state


    def setRect(self, rect):
        self.rect = rect
        self.rect.y += 5

    def setLFrames(self, lf):
        self.leftFrames = lf

    def setRFrames(self, rf):
        self.rightFrames = rf

    def setSkillDirection(self, direction):
        self.direction = direction

    def configAnimationService(self):
        self.idleAnimationService = TimingAnimationService([self.leftFrames[0], self.leftFrames[1], self.leftFrames[2]],
                                                           [self.rightFrames[0], self.rightFrames[1],  self.leftFrames[2]], 0.05)

        self.moveAnimationService = TimingAnimationService([self.leftFrames[3], self.leftFrames[4]],
                                                           [self.rightFrames[3], self.rightFrames[4]], 0.05)


        self.hitAnimationService = TimingAnimationService(
            [self.leftFrames[5]],
            [self.rightFrames[5]], 0.5)
