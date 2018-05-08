from ..constants.Contstants import *
import pygame
from ..logger.LoggerFactory import LoggerFactory
from ..level.Level1 import Level1
from ..hero.AbstractHeroFactory import AbstractHeroFactory
from ..hero.Heroes import Heroes
from ..hudstats.HUDStatsBarFactory import HUDStatsBarFactory
from ..music.SoundEffectService import SoundEffectService
from ..constants.DamageType import *
from ..environment.Environment import Environment

from PodSixNet.PodSixNet.Connection import connection

from ..screen.EndScreen import EndScreen



class GameController:



    def __init__(self, roomId, playerId, roomMember, appContext):
        self.log = LoggerFactory.getStreamLogger(__name__)
        self.soundService = SoundEffectService(pygame.mixer)
        self.playerId = playerId
        self.roomId = roomId
        self.roomMember = roomMember
        self.screen = None
        self.activeSpriteList = pygame.sprite.Group()
        self.env = None
        self.appContext = appContext
        # self.level = None

    def setEnv(self, env):
        self.env = env



    def setup(self, screen):
        self.log.debug("Game controller setup, env: " + str(self.env))
        self.screen = screen
        self.soundService.play("bg/bg1.mp3")

        factory = AbstractHeroFactory()


        self.log.debug("PLAYER MEMEBER OF ROOM : " + str(self.roomMember))
        # Create the player
        if self.roomMember == 1:
            self.player = factory.getHero(Heroes.NARUTO)
            hud = HUDStatsBarFactory.getInstanse(self.screen, True)
            self.player.setHUD(hud)
            self.player.setContext(self)

            self.enermy = factory.getHero(Heroes.SASUKE)

            hud = HUDStatsBarFactory.getInstanse(self.screen, False)
            self.enermy.setHUD(hud)
            self.enermy.setContext(self)
            self.enermy.rect.x += SCREEN_WIDTH - 300

        else:
            self.player = factory.getHero(Heroes.SASUKE)
            hud = HUDStatsBarFactory.getInstanse(self.screen, False)
            self.player.setHUD(hud)
            self.player.setContext(self)

            self.enermy = factory.getHero(Heroes.NARUTO)
            self.enermy.rect.x += SCREEN_WIDTH - 300


            hud = HUDStatsBarFactory.getInstanse(self.screen, True)
            self.enermy.setHUD(hud)
            self.enermy.setContext(self)



            # self.enermy = factory.getHero(Heroes.NARUTO)
            #
            # hud = HUDStatsBarFactory.getInstanse(self.screen, False)
            # self.enermy.setHUD(hud)
            # self.enermy.setContext(self)

        self.activeSpriteList.add(self.player)
        self.activeSpriteList.add(self.enermy)


        # Create all the levels
        self.levels = []
        self.levels.append(Level1(self.player))
        # level_list.append(levels.Level_02(player))

        # Set the current level
        currentLevelIndex = 0
        self.currentLevel = self.levels[currentLevelIndex]


        # player.level = current_level

        # configure player
        # self.player.rect.x = 340
        # self.player.rect.y = SCREEN_HEIGHT - self.player.rect.height


    def draw(self):
        self.currentLevel.draw(self.screen)
        for elemnet in self.activeSpriteList:
            print("eleemnt image " + str(elemnet.image))
            break
        self.activeSpriteList.draw(self.screen)




    def udpate(self, updateTime, events):
        # self.log.debug("controller update")

        # Update items in the level
        self.currentLevel.update()

        # Update the player.
        self.activeSpriteList.update(updateTime)

        # pygame.draw.rect(self.screen, GREEN, (self.player.rect.x, self.player.rect.y, 20, 10))

        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(self.player.getName(), False,
                                    (255, 255, 255))

        self.screen.blit(textsurface, (self.player.rect.x + 25, self.player.rect.y - 15))

        textsurface2 = myfont.render(self.enermy.getName(), False,
                                    (255, 255, 255))

        self.screen.blit(textsurface2, (self.enermy.rect.x + 25, self.enermy.rect.y - 15))

        # check if anyone died
        if self.player.isDead():
            self.log.debug("Your player dead")
            endScreen = EndScreen(self.screen, events, self.appContext)
            endScreen.render(win=False)

        if self.enermy.isDead():
            self.log.debug("Enermy dead")
            endScreen = EndScreen(self.screen, events, self.appContext)
            endScreen.render(win=True)






    def moveEnermy(self, pid, direction, x, y):
        self.enermy.rect.x = x
        self.enermy.rect.y = y
        if direction == "R":
            print("MOVING")
            self.enermy.goRight()
        elif direction == "L":
            self.enermy.goLeft()


    def stopEnermy(self, pid, direction, x, y):
        self.enermy.rect.x = x
        self.enermy.rect.y = y
        print("STOPING")
        self.enermy.stop()


    def jumpEnermy(self, pid, direction, x, y):
        self.enermy.rect.x = x
        self.enermy.rect.y = y
        self.enermy.jump()

    def basicAttackEnermy(self, pid, direction, x, y, time):
        self.enermy.rect.x = x
        self.enermy.rect.y = y
        self.enermy.basicAttack(time)

        collideList = pygame.sprite.spritecollide(self.enermy, self.activeSpriteList, False)
        collideList.remove(self.enermy)
        self.log.debug(collideList)
        for target in list(collideList):
            target.takeDamage(self.enermy.getDamage(), self.enermy.getDirection(), BASIC_ATTACK, time)

    def specialMove1Enermy(self, pid, direction, x, y, time):
        self.enermy.rect.x = x
        self.enermy.rect.y = y

        self.enermy.specialMove1(time)

    def handleEvent(self, event, time):
        # self.log.debug("controller handle event " + str(event))


        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.broadcast("move", "L", time)
                # connection.Send(
                #     {"action": "move", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "L", "time": time})
                self.player.goLeft()


            if event.key == pygame.K_RIGHT:
                self.broadcast("move", "R", time)
                # connection.Send(
                #     {"action": "move", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "R", "time": time})
                self.player.goRight()

            if event.key == pygame.K_SPACE:
                self.broadcast("jump", "R", time)
                # connection.Send(
                #     {"action": "jump", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "R", "time": time})
                self.player.jump()

            if event.key == pygame.K_2:
                self.broadcast("specialMove1", self.player.getDirection(), time)
                self.player.specialMove1(time)
                # self.enermy.specialMove1(time)


            if event.key == pygame.K_1:
                # self.log.debug("a")
                self.broadcast("basicAttack", "R", time)
                # connection.Send(
                #     {"action": "basicAttack", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "R", "time": time})
                self.player.basicAttack(time)

                collideList = pygame.sprite.spritecollide(self.player, [self.enermy], False)
                self.log.debug(collideList)
                for target in list(collideList):
                    target.takeDamage(self.player.getDamage(), self.player.getDirection(), BASIC_ATTACK, time)

            # #temp controls
            # if event.key == pygame.K_a:
            #     print("going left")
            #     self.enermy.goLeft()
            # if event.key == pygame.K_d:
            #     self.enermy.goRight()
            # if event.key == pygame.K_w:
            #     print("going up")
            #     self.enermy.jump()
            # if event.key == pygame.K_s:
            #     # self.log.debug("a")
            #     self.enermy.basicAttack(time)
            #
            #     collideList = pygame.sprite.spritecollide(self.enermy, self.activeSpriteList, False)
            #     collideList.remove(self.enermy)
            #     self.log.debug(collideList)
            #     for target in collideList:
            #         target.takeDamage(self.player.getDamage(), self.enermy.getDirection())

            #temp

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.player.xVelocity < 0:
                self.broadcast("stop", "L", time)
                # connection.Send(
                #     {"action": "stop", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "L", "time": time})
                self.player.stop()

            if event.key == pygame.K_RIGHT and self.player.xVelocity > 0:
                self.broadcast("stop", "R", time)
                # connection.Send(
                #     {"action": "stop", "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                #      "roomId": self.roomId, "direction": "R", "time": time})
                self.player.stop()

            # # temp controls
            # if event.key == pygame.K_a and self.enermy.xVelocity < 0:
            #     self.enermy.stop()
            # if event.key == pygame.K_d and self.enermy.xVelocity > 0:
            #     self.enermy.stop()


    def broadcast(self, action, direction, time):
        self.log.debug("Current env" + str(self.env))
        self.log.debug("Current env var" + str(Environment.PROD.value))

        if self.env == Environment.PROD.value:
            self.log.debug("Broadcasting " + str(action) + ":" + str(direction) + " at time: " + str(time))
            connection.Send(
                {"action": action, "x": self.player.rect.x, "y": self.player.rect.y, "playerId": self.playerId,
                 "roomId": self.roomId, "direction": direction, "time": time})
