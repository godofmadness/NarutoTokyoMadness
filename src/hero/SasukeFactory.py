from .Sasuke import Sasuke
from ..logger.LoggerFactory import LoggerFactory
from..path.ImagePathResolver import ImagePathResolver
import pygame


class SasukeFactory:


    @staticmethod
    def getInstance():
        log = LoggerFactory.getStreamLogger(__name__)
        sasuke = Sasuke()
        pathResolver = ImagePathResolver()
        # load all walking frames
        leftWalkingFrames = []
        rightWalkingFrames = []
        leftJumpingFrames = []
        rightJumpingFrames = []
        rightIdleFrames = []
        rightFallingFrames = []
        leftFallingFrames = []
        leftIdleFrames = []

        rightGettingDamageFrames = []
        leftGettingDamageFrames = []

        leftGettingStrongDamageFrames = []
        rightGettingStrongDamageFrames = []

        rightAirAttackFrame = []
        leftAirAttackFrame = []
        rightBasicAttackFrames = []
        leftBasicAttackFrames = []

        leftSpecailMove1Frames = []
        rightSpecialMove1Frames = []

        for number in range(1, 7):
            # load right walking frames
            walkingFrame = pygame.image.load(pathResolver.resolve("sasuke-sprites/sasuke-run" + str(number) + ".png"))
            walkingFrame = pygame.transform.scale(walkingFrame, (90, 94))

            rightWalkingFrames.append(walkingFrame)
            # load left walking frames
            walkingFrame = pygame.transform.flip(walkingFrame, True, False)
            leftWalkingFrames.append(walkingFrame)

        sasuke.setRightWalkingFrames(rightWalkingFrames)
        sasuke.setLeftWalkingFrames(leftWalkingFrames)

        # load all idle frames
        for number in range(1, 7):
            idleFrame = pygame.image.load(pathResolver.resolve("sasuke-sprites/sasuke-idle" + str(number) + ".png"))
            idleFrame = pygame.transform.scale(idleFrame, (90, 94))
            rightIdleFrames.append(idleFrame)

            mirroredIdleFrame = pygame.transform.flip(idleFrame, True, False)
            leftIdleFrames.append(mirroredIdleFrame)

            sasuke.setRightIdleFrames(rightIdleFrames)
            sasuke.setLeftIdleFrames(leftIdleFrames)

        for number in range(1, 3):
            jumpFrame = pygame.image.load(pathResolver.resolve("sasuke-sprites/sasuke-jump" + str(number) + ".png"))
            jumpFrame = pygame.transform.scale(jumpFrame, (90, 94))
            rightJumpingFrames.append(jumpFrame)

            mirroredJumpFrame = pygame.transform.flip(jumpFrame, True, False)
            leftJumpingFrames.append(mirroredJumpFrame)

            sasuke.setRightJumpingFrames(rightJumpingFrames)
        sasuke.setLeftJumpingFrames(leftJumpingFrames)

        fallFrame = pygame.image.load(pathResolver.resolve("sasuke-sprites/sasuke-fall1.png"))
        fallFrame = pygame.transform.scale(fallFrame, (90, 94))
        rightFallingFrames.append(fallFrame)

        mirroredFallFrame = pygame.transform.flip(fallFrame, True, False)
        leftFallingFrames.append(mirroredFallFrame)

        sasuke.setRightFallingFrames(rightFallingFrames)
        sasuke.setLeftFallingFrames(leftFallingFrames)

        for number in range(1, 11):
            basicAtttackFrame = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-battack_" + str(number) + ".png"))
            basicAtttackFrame = pygame.transform.scale(basicAtttackFrame, (90, 94))
            rightBasicAttackFrames.append(basicAtttackFrame)

            mirroredBasicAttack = pygame.transform.flip(basicAtttackFrame, True, False)
            leftBasicAttackFrames.append(mirroredBasicAttack)

            sasuke.setRightBasicAttackFrames(rightBasicAttackFrames)
            sasuke.setLeftBasicAttackFrames(leftBasicAttackFrames)

        for number in range(1, 7):
            airAtttackFrame = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-basic-attack_" + str(number) + ".png"))
            airAtttackFrame = pygame.transform.scale(airAtttackFrame, (90, 94))
            rightAirAttackFrame.append(airAtttackFrame)

            mirroredAirAttack = pygame.transform.flip(airAtttackFrame, True, False)
            leftAirAttackFrame.append(mirroredAirAttack)

            sasuke.setRightAirAttackFrames(rightAirAttackFrame)
            sasuke.setLeftAirAttackFrames(leftAirAttackFrame)

        for number in range(1, 4):
            damageFrame = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-taking-light-damage_" + str(number) + ".png"))
            damageFrame = pygame.transform.scale(damageFrame, (90, 94))
            rightGettingDamageFrames.append(damageFrame)

            mirroredDamageFrame = pygame.transform.flip(damageFrame, True, False)
            leftGettingDamageFrames.append(mirroredDamageFrame)

        for number in range(1, 3):
            smove1 = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-special-move-f_" + str(number) + ".png"))
            if number == 2:
                smove1 = pygame.transform.scale(smove1, (115, 94))
            else:
                smove1 = pygame.transform.scale(smove1, (90, 94))
            rightSpecialMove1Frames.append(smove1)

            mirroredSMove1 = pygame.transform.flip(smove1, True, False)
            leftSpecailMove1Frames.append(mirroredSMove1)


        sasuke.setLeftSpecialMove1Frames([leftSpecailMove1Frames[0]] + leftWalkingFrames + [leftSpecailMove1Frames[1]])
        sasuke.setRightSpecialMove1Frames([rightSpecialMove1Frames[0]] + rightWalkingFrames + [rightSpecialMove1Frames[1]])

        #  TAKIGN STRONG DAMAGE

        for number in range(1, 8):
            strongDamage = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-heavydamage" + str(number) + ".png"))

            strongDamage = pygame.transform.scale(strongDamage, (90, 94))
            rightGettingStrongDamageFrames.append(strongDamage)

            mirroredStrongDamageFrame = pygame.transform.flip(strongDamage, True, False)
            leftGettingStrongDamageFrames.append(mirroredStrongDamageFrame)

        rlayingFrame = rightGettingStrongDamageFrames[len(rightGettingStrongDamageFrames) - 1]
        llayingFrame = leftGettingStrongDamageFrames[len(leftGettingStrongDamageFrames) - 1]

        rightGettingStrongDamageFrames.append(rlayingFrame)
        rightGettingStrongDamageFrames.append(rlayingFrame)
        rightGettingStrongDamageFrames.append(rlayingFrame)

        leftGettingStrongDamageFrames.append(llayingFrame)
        leftGettingStrongDamageFrames.append(llayingFrame)
        leftGettingStrongDamageFrames.append(llayingFrame)

        for number in range(8, 11):
            strongDamage = pygame.image.load(
                pathResolver.resolve("sasuke-sprites/sasuke-heavydamage" + str(number) + ".png"))

            strongDamage = pygame.transform.scale(strongDamage, (90, 94))
            rightGettingStrongDamageFrames.append(strongDamage)

            mirroredStrongDamageFrame = pygame.transform.flip(strongDamage, True, False)
            leftGettingStrongDamageFrames.append(mirroredStrongDamageFrame)

        sasuke.setRightGettingDamageFrames(rightGettingDamageFrames)
        sasuke.setLeftGettingDamageFrames(leftGettingDamageFrames)
        sasuke.setRightGettingStrongDamageFrames(rightGettingStrongDamageFrames)
        sasuke.setLeftGettingStrongDamageFrames(leftGettingStrongDamageFrames)

        # ! TAKIGN STRONG DAMAGE

        sasukeIcon = pygame.image.load(
            pathResolver.resolve("sasuke-sprites/sasuke-icon_1.png"))

        sasuke.setIcon(sasukeIcon)
        sasuke.setRightGettingDamageFrames(rightGettingDamageFrames)
        sasuke.setLeftGettingDamageFrames(leftGettingDamageFrames)

        sasuke.setBasicAttackIndexes([1, 3, 7])
        sasuke.setAirAttackIndexes([2, 5])

        sasuke.initAnimationServices()

        # Set the image the player starts wi th
        sasuke.setImage(rightIdleFrames[0])
        # Set a reference to the image rect.
        return sasuke

