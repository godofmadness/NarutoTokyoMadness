import pygame
from ..path.ImagePathResolver import ImagePathResolver
from .Chidori import Chidori

class ChidoryFactory:

    @staticmethod
    def getInstance(target):

        chidory = Chidori(target)

        # frames = []
        pathResolver = ImagePathResolver()

        leftFrames = []
        rightFrames = []


        for number in range(1, 7):
            # load right walking frames
            frame = pygame.image.load(pathResolver.resolve("sasuke-sprites/skill/chidory_" + str(number) + ".png"))
            if number > 4:
                frame = pygame.transform.scale(frame, (115, 94))
            else:
                frame = pygame.transform.scale(frame, (90, 94))

            # frames.append(frame)

            rightFrames.append(frame)
            # load left walking frames
            mirroredFrames = pygame.transform.flip(frame, True, False)

            leftFrames.append(mirroredFrames)

        chidory.setLFrames(leftFrames)
        chidory.setRFrames(rightFrames)
        # chidory.setSkillDirection("R")
        chidory.configAnimationService()
        return chidory
        # sasuke.setLeftWalkingFrames(leftWalkingFrames)
