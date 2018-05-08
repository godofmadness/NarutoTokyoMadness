import pygame
from .constants.Contstants import *
from .game.GameController import GameController
from .logger.LoggerFactory import LoggerFactory
import timeit
import time
import sys
from .environment.Environment import Environment
from PodSixNet.PodSixNet.Connection import ConnectionListener, connection
from .environment.ConfigService import ConfigService
from .screen.WelcomeScreen import WelcomeScreen



class App(ConnectionListener):


    # Create a function to receive the start game signal
    def Network_startgame(self, data):
        # Get the game ID and player number from the data
        self.roomId = data['roomId']
        self.playerId = data['playerId']
        self.roomMember = data['roomMember']
        self.gameController = GameController(self.roomId, self.playerId, self.roomMember, self)
        self.gameController.setEnv(self.configService.getEnvironment())
        self.log.debug("Player ", self.player, " connected to game ", self.roomId)
        # Set the game to running so that we enter the update loop
        self.running = True


    def Network_move(self, data):
        print("Moving player " + str(data["playerId"]) + " to " + str(data["direction"]))
        self.gameController.moveEnermy(data["playerId"], data["direction"], data["x"], data["y"])

    def Network_stop(self, data):
        print("Stopping player " + str(data["playerId"]) + " to " + str(data["direction"]))
        self.gameController.stopEnermy(data["playerId"], data["direction"], data["x"], data["y"])

    def Network_jump(self, data):
        print("jmp  " + str(data["playerId"]) + " to " + str(data["direction"]))
        self.gameController.jumpEnermy(data["playerId"], data["direction"], data["x"], data["y"])

    def Network_basicAttack(self, data):
        print("basicAttack  " + str(data["playerId"]) + " to " + str(data["direction"]) + " time " + str(data["time"]))
        self.gameController.basicAttackEnermy(data["playerId"], data["direction"], data["x"], data["y"], self.updateTime)

    def Network_specialMove1(self, data):
        print("special move 1  " + str(data["playerId"]) + " to " + str(data["direction"]) + " time " + str(data["time"]))
        self.gameController.specialMove1Enermy(data["playerId"], data["direction"], data["x"], data["y"], self.updateTime)


    def renderLoadingScreen(self, screen, timeCounter):
        screen.fill(BLACK)
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        textsurface = myfont.render('Waiting for other players' + (int(timeCounter / 10) * "."), False,
                                    (255, 255, 255))
        timeCounter += 1

        if timeCounter == 40:
            timeCounter = 0

        screen.blit(textsurface, (SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        return timeCounter

    def renderWelcomeScreen(self, screen):
        ws = WelcomeScreen( screen, [])
        resume = False
        while not resume:
            print("WEG")
            resume = ws.render()


    def __init__(self):
        self.log = LoggerFactory.getStreamLogger(__name__)
        #  default values for debug mode
        self.gameController = GameController( 1, 1, 1, self)
        self.running = False
        self.configService = ConfigService(sys.argv)
        self.log.debug("Currend env: " + self.configService.getEnvironment())
        self.gameController.setEnv(self.configService.getEnvironment())
        self.debug = True
        self.updateTime = 0


    def restart(self):
        app = App()
        app.run()

    def run(self):
        """ Main Program """
        pygame.init()


        self.gameId = None
        self.player = None

        print(self.configService.getEnvironment() == Environment.DEBUG.value[0])
        self.debug = self.configService.getEnvironment() == Environment.DEBUG.value[0]

        # Set the height and width of the screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)


        pygame.display.set_caption("Naruto: Tokyo Madness")

        # While the game isn't running pump the server

        # Set running to false
        self.running = True


        if not self.debug:
            self.Connect()
            self.running = False

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.

        connectingTimeCounter = 0
        # While the game isn't running pump the server
        while not self.running and not self.debug:

            # Check if the user exited the game
            updatedTime = self.renderLoadingScreen(screen, connectingTimeCounter)
            connectingTimeCounter = updatedTime

            # Pump the server
            # While the game isn't running pump the server
            self.Pump()
            connection.Pump()

            time.sleep(0.01)

        #setup game controller
        self.gameController.setup(screen)

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()


        startTime = timeit.default_timer()

        # -------- Main Program Loop -----------
        while not done:
            screen.fill(BLACK)
            self.gameController.draw()

            # Pump the server to check for updates
            if not self.debug:
                connection.Pump()
                self.Pump()

            # updateTime = None
            # updateTime = 0

            updateTime = time.time()

            print("UPDATE TIME " + str(updateTime))
            self.updateTime = updateTime
            for event in pygame.event.get():  # User did something
                self.gameController.handleEvent(event, updateTime)

            self.gameController.udpate(updateTime, event)

            # Limit to 60 frames per second
            clock.tick(30)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        pygame.quit()

        pass


def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()


