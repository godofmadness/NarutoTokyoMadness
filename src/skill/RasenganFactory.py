import pygame
from ..path.ImagePathResolver import ImagePathResolver
from .Rasengan import Rasengan

class RasenganFactory:

    @staticmethod
    def getInstance(target):

        rasengan = Rasengan(target)

        # frames = []
        pathResolver = ImagePathResolver()

        leftFrames = []
        rightFrames = []


        for number in range(1, 7):
            # load right walking frames
            frame = pygame.image.load(pathResolver.resolve("naruto-sprites/skill/rasengan_" + str(number) + ".png"))
            if number > 4:
                frame = pygame.transform.scale(frame, (115, 94))
            else:
                frame = pygame.transform.scale(frame, (90, 94))

            # frames.append(frame)

            rightFrames.append(frame)
            # load left walking frames
            mirroredFrames = pygame.transform.flip(frame, True, False)

            leftFrames.append(mirroredFrames)

        rasengan.setLFrames(leftFrames)
        rasengan.setRFrames(rightFrames)
        # chidory.setSkillDirection("R")
        rasengan.configAnimationService()
        return rasengan
        # sasuke.setLeftWalkingFrames(leftWalkingFrames)
