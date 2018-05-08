from .Naruto import Naruto
from ..logger.LoggerFactory import LoggerFactory
from..path.ImagePathResolver import ImagePathResolver
import pygame

class NarutoFactory:

    @staticmethod
    def getInstance():

        log = LoggerFactory.getStreamLogger(__name__)
        naruto = Naruto()
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
        rightGettingStrongDamageFrames = []
        leftGettingStrongDamageFrames = []

        rightKnokedDownFrames = []
        leftKnokedDownFrames = []


        leftSpecial1Move = []
        rightSpecial1Move = []

        rightAirAttackFrame = []
        leftAirAttackFrame = []
        rightBasicAttackFrames = []
        leftBasicAttackFrames = []

        for number in range(1, 7):
            # load right walking frames
            walkingFrame = pygame.image.load(pathResolver.resolve("naruto-sprites/naruto-run" + str(number) + ".png"))
            walkingFrame = pygame.transform.scale(walkingFrame, (90, 94))

            rightWalkingFrames.append(walkingFrame)
            # load left walking frames
            walkingFrame = pygame.transform.flip(walkingFrame, True, False)
            leftWalkingFrames.append(walkingFrame)

        naruto.setRightWalkingFrames(rightWalkingFrames)
        naruto.setLeftWalkingFrames(leftWalkingFrames)

        # load all idle frames
        for number in range(1, 5):
            idleFrame = pygame.image.load(pathResolver.resolve("naruto-sprites/naruto-idle" + str(number) + ".png"))
            idleFrame = pygame.transform.scale(idleFrame, (90, 94))
            rightIdleFrames.append(idleFrame)

            mirroredIdleFrame = pygame.transform.flip(idleFrame, True, False)
            leftIdleFrames.append(mirroredIdleFrame)

        naruto.setRightIdleFrames(rightIdleFrames)
        naruto.setLeftIdleFrames(leftIdleFrames)

        for number in range(1, 3):
            jumpFrame = pygame.image.load(pathResolver.resolve("naruto-sprites/naruto-jump" + str(number) + ".png"))
            jumpFrame = pygame.transform.scale(jumpFrame, (90, 94))
            rightJumpingFrames.append(jumpFrame)

            mirroredJumpFrame = pygame.transform.flip(jumpFrame, True, False)
            leftJumpingFrames.append(mirroredJumpFrame)

        naruto.setRightJumpingFrames(rightJumpingFrames)
        naruto.setLeftJumpingFrames(leftJumpingFrames)

        fallFrame = pygame.image.load(pathResolver.resolve("naruto-sprites/naruto-fall1.png"))
        fallFrame = pygame.transform.scale(fallFrame, (90, 94))
        rightFallingFrames.append(fallFrame)

        mirroredFallFrame = pygame.transform.flip(fallFrame, True, False)
        leftFallingFrames.append(mirroredFallFrame)

        naruto.setRightFallingFrames(rightFallingFrames)
        naruto.setLeftFallingFrames(leftFallingFrames)

        for number in range(1, 15):
            basicAtttackFrame = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-battack_" + str(number) + ".png"))
            basicAtttackFrame = pygame.transform.scale(basicAtttackFrame, (90, 94))
            rightBasicAttackFrames.append(basicAtttackFrame)

            mirroredBasicAttack = pygame.transform.flip(basicAtttackFrame, True, False)
            leftBasicAttackFrames.append(mirroredBasicAttack)

        naruto.setRightBasicAttackFrames(rightBasicAttackFrames)
        naruto.setLeftBasicAttackFrames(leftBasicAttackFrames)

        for number in range(1, 15):
            airAtttackFrame = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-basic-attack_" + str(number) + ".png"))
            airAtttackFrame = pygame.transform.scale(airAtttackFrame, (90, 94))
            rightAirAttackFrame.append(airAtttackFrame)

            mirroredAirAttack = pygame.transform.flip(airAtttackFrame, True, False)
            leftAirAttackFrame.append(mirroredAirAttack)

        naruto.setRightAirAttackFrames(rightAirAttackFrame)
        naruto.setLeftAirAttackFrames(leftAirAttackFrame)


        for number in range(1, 3):
            damageFrame = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-taking-light-damage_" + str(number) + ".png"))
            damageFrame = pygame.transform.scale(damageFrame, (90, 94))
            rightGettingDamageFrames.append(damageFrame)


            mirroredDamageFrame = pygame.transform.flip(damageFrame, True, False)
            leftGettingDamageFrames.append(mirroredDamageFrame)


        #  HEAVY DAMAGE SPRITE LOADING
        for number in range(1, 6):
            strongDamage = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-heavydamage_" + str(number) + ".png"))

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

        for number in range(6, 9):
            strongDamage = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-heavydamage_" + str(number) + ".png"))

            strongDamage = pygame.transform.scale(strongDamage, (90, 94))
            rightGettingStrongDamageFrames.append(strongDamage)

            mirroredStrongDamageFrame = pygame.transform.flip(strongDamage, True, False)
            leftGettingStrongDamageFrames.append(mirroredStrongDamageFrame)

        naruto.setRightGettingDamageFrames(rightGettingDamageFrames)
        naruto.setLeftGettingDamageFrames(leftGettingDamageFrames)
        naruto.setRightGettingStrongDamageFrames(rightGettingStrongDamageFrames)
        naruto.setLeftGettingStrongDamageFrames(leftGettingStrongDamageFrames)

        # !HEAVY DAMAGE SPPRITE LOADING


        for number in range(1, 10):
            skill1Frame = pygame.image.load(
                pathResolver.resolve("naruto-sprites/naruto-skill1_" + str(number) + ".png"))

            skill1Frame = pygame.transform.scale(skill1Frame, (90, 94))
            rightSpecial1Move.append(skill1Frame)

            mirroredSkill1Frame = pygame.transform.flip(skill1Frame, True, False)
            leftSpecial1Move.append(mirroredSkill1Frame)


        naruto.setLeftSpecialMove1Frames(leftSpecial1Move)
        naruto.setRightSpecialMove1Frames(rightSpecial1Move)


        narutoIcon = pygame.image.load(
            pathResolver.resolve("naruto-sprites/naruto-icon_1.png"))

        naruto.setIcon(narutoIcon)

        naruto.setBasicAttackIndexes([2, 5, 10])
        naruto.setAirAttackIndexes([2, 5, 8, 12])

        naruto.initAnimationServices()

        # Set the image the player starts wi th
        naruto.setImage(rightIdleFrames[0])
        print("NARUTO RECT" + str(naruto.rect))
        # Set a reference to the image rect.



        return naruto
