import pygame
from ..constants.Contstants import *
from ..logger.LoggerFactory import LoggerFactory
from ..animation.FightAnimatorService import FightAnimatorService
from ..animation.TimingAnimationService import TimingAnimationService
import platform
# from ..hero.Naruto import Naruto/


isDarwin = True if platform.system() == "Darwin" else False
OS_PRECISION = 1
# if not isDarwin:
#     OS_PRECISION = 2

""" Class represents controllable sprite that can be manipulated by user"""
class ControllableSprite(pygame.sprite.Sprite):

        def __init__(self):
            """ Constructor function """
            self.log = LoggerFactory.getStreamLogger(__name__)
            # Call the parent's constructor
            super().__init__()

            self.log.debug("Current System is Darwin? " + str(isDarwin))


            self.context = None

            # -- Attributes
            # Set speed vector of player
            self.xVelocity = 0
            self.yVelocity = 0

            #state
            self.__idle = True
            self.__onGround = False
            self.__falling = True
            self.basicAttacking = False
            self.jumpAttacking = False
            self.gettingDamage = False
            self.stunned = False
            self.gettingStrongDamage = False

            self.lastAttackTime = 0

            # This holds all the frames
            # of animation of player
            self.leftWalkingFrames = []
            self.rightWalkingFrames = []
            self.leftJumpingFrames = []
            self.rightJumpingFrames = []
            self.rightIdleFrames = []
            self.rightFallingFrames = []
            self.leftFallingFrames = []
            self.leftIdleFrames = []


            self.rightAirAttackFrame = []
            self.leftAirAttackFrame = []
            self.rightBasicAttackFrames = []
            self.leftBasicAttackFrames = []

            self.rightGettingDamageFrames = []
            self.leftGettingDamageFrames = []
            self.rightGettingStrongDamageFrames = []
            self.leftGettingStrongDamageFrames = []

            self.rightKnokedDownFrames = []
            self.leftKnokedDownFrames = []

            self.airAttackIndexes = None
            self.basicAttackIndexes = None

            self.takeStrongDamageStartTime = 0
            self.takeStrongDamageDuration = 2

            self.idleFramesLastUpdateTime = 0
            self.currentActiveIdleFrameIndex = 0
            self.gettingDamageFramesUpdateTime = 0

            self.currentActiveJumpFrame = 0
            self.jumpFramesLastUpdateTime = 0

            # What direction is the player facing?
            self.direction = "R"
            self.damageSite = None

            self.basicFightAnimatorService = None
            self.airFightAnimatorService = None
            self.takingDamageAnimation = None
            self.takingStrongDamageAnimation = None


        def update(self, updateTime):
            """ Move the player. """
            # Gravity
            self.calculateGravity()

            if self.rect.x >= SCREEN_WIDTH - 90:
                self.rect.x = SCREEN_WIDTH - 90

            if self.rect.x <= 0:
                self.rect.x = 0

            # Move left/right
            self.rect.x += self.xVelocity
            pos = self.rect.x
            # if not self.stunned:
            if not self.basicAttacking:
                    # self.log.debug("not stunned")
                    if not self.isIdle():

                        if self.direction == "R":
                            frame = (pos // 30) % len(self.rightWalkingFrames)
                            self.image = self.rightWalkingFrames[frame]
                        else:
                            frame = (pos // 30) % len(self.leftWalkingFrames)
                            self.image = self.leftWalkingFrames[frame]

                    # if hero do nothing
                    # idle animation
                    if self.isIdle():

                        if self.direction == "R" and updateTime - self.idleFramesLastUpdateTime > IDLE_FRAMERATE:

                            if self.currentActiveIdleFrameIndex == len(self.rightIdleFrames) - 1:
                                self.currentActiveIdleFrameIndex = 0
                            else:
                                self.currentActiveIdleFrameIndex += 1

                            self.image = self.rightIdleFrames[self.currentActiveIdleFrameIndex]
                            self.idleFramesLastUpdateTime = updateTime

                        elif updateTime - self.idleFramesLastUpdateTime > IDLE_FRAMERATE and self.direction == "L":

                            if self.currentActiveIdleFrameIndex == len(self.rightIdleFrames) - 1:
                                self.currentActiveIdleFrameIndex = 0
                            else:
                                self.currentActiveIdleFrameIndex += 1

                            self.image = self.leftIdleFrames[self.currentActiveIdleFrameIndex]
                            self.idleFramesLastUpdateTime = updateTime


                    if not self.__onGround:
                        if self.direction == "R":
                            self.image = self.rightJumpingFrames[0]
                        else:
                            self.image = self.leftJumpingFrames[0]

                        if self.direction == "R" and updateTime - self.idleFramesLastUpdateTime > JUMP_FRAMERATE:

                            self.image = self.rightJumpingFrames[1]

                        elif self.direction == "L" and updateTime - self.idleFramesLastUpdateTime > JUMP_FRAMERATE:
                            self.image = self.leftJumpingFrames[1]




                    if self.__falling:
                        if self.direction == "R":
                            self.image = self.rightFallingFrames[0]
                        else:
                            self.image = self.leftFallingFrames[0]

                    if not self.isOnGround() and self.jumpAttacking:
                        # self.log.debug("jump attacking")
                        image = self.airFightAnimatorService.updateAttack(updateTime, self.getDirection())
                        if image == None:
                            # self.__falling = True
                            self.jumpAttacking = False
                        else:
                            # self.xVelocity = 3
                            self.image = image


                    if self.gettingDamage:
                        print("TAKING DAMAGE")
                        self.image = self.takingDamageAnimation.updateAnimation(updateTime, self.getDirection())

                        # self.log.debug("ge
                        # tting damage")
                        if self.xVelocity != 0:
                            if self.damageSite == "R":
                                self.xVelocity -= 1 / OS_PRECISION
                            else:
                                self.xVelocity += 1 / OS_PRECISION

                            # self.__idle = True
                        else:
                            self.gettingDamage = False
                            self.__idle = True

                    if self.gettingStrongDamage or updateTime <= self.takeStrongDamageStartTime + self.takeStrongDamageDuration:
                        self.image = self.takingStrongDamageAnimation.updateAnimation(updateTime, self.getDirection())
                        self.log.debug("IMAGE " + str(self.image))

                        if self.xVelocity != 0:
                            if self.damageSite == "R":
                                self.log.debug("SKILLL DAMAGE SIDE: R")
                                self.xVelocity -= 1 / OS_PRECISION
                                self.yVelocity += 1 / OS_PRECISION
                            else:
                                self.log.debug("SKILLL DAMAGE SIDE: L")
                                self.xVelocity += 1 / OS_PRECISION
                                self.yVelocity += 1 / OS_PRECISION
                        else:
                            # if updateTime > self.takeStrongDamageStartTime + self.takeStrongDamageDuration:


                            self.gettingStrongDamage = False
                            self.__idle = True

                    # if self.stunned:
                    #     self.image = self.takingDamageAnimation.updateAnimation(updateTime, self.getDirection())


                    # See if we hit anything
                    # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
                    # for block in block_hit_list:
                    #     # If we are moving right,
                    #     # set our right side to the left side of the item we hit
                    #     if self.xVelocity > 0:
                    #         self.rect.right = block.rect.left
                    #     elif self.xVelocity < 0:
                    #         # Otherwise if we are moving left, do the opposite.
                    #         self.rect.left = block.rect.right

                    # Move up/down
                    self.rect.y += self.yVelocity
                    #
                    # # Check and see if we hit anything
                    # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
                    # for block in block_hit_list:
                    #
                    #     # Reset our position based on the top/bottom of the object.
                    #     if self.yVelocity > 0:
                    #         self.rect.bottom = block.rect.top
                    #     elif self.yVelocity < 0:
                    #         self.rect.top = block.rect.bottom
                    #
                    #     # Stop our vertical movement
                    #     self.yVelocity = 0
                    #
                    #     if isinstance(block, MovingPlatform):
                    #         self.rect.x += block.change_x
            else :
                image = self.basicFightAnimatorService.updateAttack(updateTime, self.getDirection())
                if image == None:
                    self.__idle = True
                    self.basicAttacking = False
                    self.xVelocity = 0
                else:
                    # self.xVelocity = 3
                    self.image = image

                    # self.image = self.basicAttackFrames[1]

                 #if stunned

        def calculateGravity(self):
            """ Calculate effect of gravity. """
            if self.yVelocity == 0:
                self.yVelocity = 1 / OS_PRECISION
            else:
                self.yVelocity += .35 * 2


            self.__falling = False
            # falling

            if self.yVelocity > 1 / OS_PRECISION:
                self.log.debug("fal")
                self.__falling = True


            # See if we are on the ground
            if self.rect.y >= SCREEN_HEIGHT - 100 - self.rect.height and self.yVelocity >= 0:

                # landing event
                if not self.__onGround:
                    if self.xVelocity == 0:
                        self.log.debug("landed without x movement")
                        self.__idle = True
                    self.__falling = False


                self.yVelocity = 0
                self.rect.y = SCREEN_HEIGHT - 100 - self.rect.height
                self.__onGround = True



            # event when landed


        def jump(self):
            """ Called when user hits 'jump' button. """

            # move down a bit and see if there is a platform below us.
            # Move down 2 pixels because it doesn't work well if we only move down 1
            # when working with a platform moving down.
            self.__idle = False
            self.__onGround = False
            self.jumpAttacking = False
            # self.rect.y += 2
            # platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            # self.rect.y -= 2
            #
            # if self.direction == "R":
            #     self.image = self.rightJumpingFrames[0]
            # else:
            #     self.image = self.leftJumpingFrames[0]

            # If it is ok to jump, set our speed upwards
            # if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.yVelocity = -12 / OS_PRECISION

        # Player-controlled movement:
        def goLeft(self):
            """ Called when the user hits the left arrow. """
            self.__idle = False
            self.xVelocity = -8 / OS_PRECISION
            self.direction = "L"

        def goRight(self):
            """ Called when the user hits the right arrow. """
            self.__idle = False
            self.xVelocity = 8 / OS_PRECISION
            self.direction = "R"

        def stop(self):
            """ Called when the user lets off the keyboard. """
            self.__idle = True
            self.xVelocity = 0




        def animateBasicDamage(self, damage, damageSide):
            self.damageSite = damageSide
            if self.damageSite == "R":
                self.xVelocity += 4 / OS_PRECISION
            else:
                self.xVelocity -= 4 / OS_PRECISION

            self.gettingDamage = True
            self.stunned = True

        def animateStrongDamage(self, damage, damageSide, time):

            self.log.debug("ANIMATE STRONG DAMAGE METHDO DAMAGE SIDE: " + damageSide)

            self.damageSite = damageSide

            if self.damageSite == "R":
                self.xVelocity += 20 / OS_PRECISION
                self.yVelocity -= 15 / OS_PRECISION
            else:
                self.xVelocity -= 20 / OS_PRECISION
                self.yVelocity -= 15 / OS_PRECISION

            self.takingStrongDamageAnimation.clear()
            self.takeStrongDamageStartTime = time
            self.gettingStrongDamage = True




        def basicAttack(self, time):
            if time - self.lastAttackTime > KEY_A_HOLD:

                if not self.isOnGround():

                    self.log.debug("Air attack")
                    self.jumpAttacking = True
                    self.airFightAnimatorService.attack(time)
                else:
                    if self.getDirection() == "R":
                        self.xVelocity = 3 / OS_PRECISION
                    else:
                        self.xVelocity = -3 / OS_PRECISION
                    self.log.debug("Basic attack")
                    self.basicAttacking = True
                    self.basicFightAnimatorService.attack(time)
                self.lastAttackTime = time


        def stun(self, duration):
            self.stunned = True


            # self.log.debug("atticjing")


        def getDirection(self):
            return self.direction

        def isIdle(self):
            return self.__idle

        def setIdle(self, state):
            self.__idle = state

        def isOnGround(self):
            return self.__onGround

        def isFalling(self):
            return self.__falling

        def setLeftWalkingFrames(self, lwf):
            self.leftWalkingFrames = lwf

        def setRightWalkingFrames(self, rwf):
            self.rightWalkingFrames = rwf

        def setLeftJumpingFrames(self, ljf):
            self.leftJumpingFrames = ljf

        def setRightJumpingFrames(self, rjf):
            self.rightJumpingFrames = rjf

        def setLeftIdleFrames(self, lif):
            self.leftIdleFrames = lif

        def setRightIdleFrames(self, rif):
            self.rightIdleFrames = rif

        def setLeftFallingFrames(self, lff):
            self.leftFallingFrames = lff

        def setRightFallingFrames(self, rff):
            self.rightFallingFrames = rff

        def setRightBasicAttackFrames(self, rbaf):
            self.log.debug("setted " + str(rbaf))
            self.rightBasicAttackFrames = rbaf

        def setLeftBasicAttackFrames(self, lbaf):
            self.log.debug("setted " + str(lbaf))
            self.leftBasicAttackFrames = lbaf

        def setRightAirAttackFrames(self, raaf):
            self.rightAirAttackFrame = raaf

        def setLeftAirAttackFrames(self, laaf):
            self.leftAirAttackFrame = laaf

        def setImage(self, image):
            self.image = image
            self.rect = self.image.get_rect()

        def setAirAttackIndexes(self, aai):
            self.airAttackIndexes = aai

        def setBasicAttackIndexes(self, bai):
            self.basicAttackIndexes = bai

        def setRightGettingDamageFrames(self, gdf):
            self.rightGettingDamageFrames = gdf

        def setRightGettingStrongDamageFrames(self, rgsdf):
            self.rightGettingStrongDamageFrames = rgsdf

        def setLeftGettingStrongDamageFrames(self, lgsdf):
            self.leftGettingStrongDamageFrames = lgsdf

        def setLeftGettingDamageFrames(self, ldf):
            self.leftGettingDamageFrames = ldf

        def setLeftKnokedDownFrames(self, lkdf):
            self.leftKnokedDownFrames = lkdf

        def setRightKnokedDownFrames(self, lkdf):
            self.rightKnokedDownFrames = lkdf

        def setContext(self, context):
            self.context = context

        def initAnimationServices(self):
            if len(self.leftBasicAttackFrames) == 0 or len(self.rightBasicAttackFrames) == 0 or len(self.leftAirAttackFrame) == 0 or len(self.rightAirAttackFrame) == 0:
                raise AttributeError("Attack animations not initialized")
            else:

                self.basicFightAnimatorService = FightAnimatorService(self.rightBasicAttackFrames,
                                                                      self.leftBasicAttackFrames,
                                                                      self.basicAttackIndexes, COMBO_BREAK_TIME)

                self.airFightAnimatorService = FightAnimatorService(self.rightAirAttackFrame,
                                                                      self.leftAirAttackFrame,
                                                                      self.airAttackIndexes, COMBO_BREAK_TIME)

                self.takingDamageAnimation = TimingAnimationService(self.leftGettingDamageFrames, self.rightGettingDamageFrames, TAKING_DAMAGE_FRAMERATE)

                self.takingStrongDamageAnimation = TimingAnimationService(self.leftGettingStrongDamageFrames,
                                                                    self.rightGettingStrongDamageFrames,
                                                                    0.16)


