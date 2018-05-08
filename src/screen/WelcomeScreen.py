from pygameMenu.locals import PYGAME_MENU_BACK, PYGAME_MENU_CLOSE, PYGAME_MENU_EXIT, PYGAME_MENU_DISABLE_CLOSE, \
    TEXT_NEWLINE
from ..constants.Contstants import *
import pygame
from pygameMenu.textmenu import TextMenu
import pygameMenu


def bg():
    pass
    # print("HELLO")


def start():
    START_GAME = True

START_GAME = False


class WelcomeScreen:

    def bg(self):
        pass
        # print("HELLO")

    def __init__(self, screen, events):
        self.font = 'ArcadeClassic Regular'
        self.screen = screen
        self.events = events
        self.startGame = False
        # self.context = context

        # Main menu, pauses execution of the application
        self.menu = pygameMenu.Menu(self.screen,
                               window_width=SCREEN_WIDTH,
                               window_height=SCREEN_HEIGHT,
                               font=pygameMenu.fonts.FONT_NEVIS,
                               title='Naruto Tokyo Madness',
                               title_offsety=5,
                               menu_alpha=90,
                               enabled=True,
                               bgfun=bg,
                               onclose=PYGAME_MENU_CLOSE)


        self.menu.add_option("Start online battle", start)
        self.menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function




    # Functions
    def mainmenu_background(self):
        """
        Background color of the main menu, on this function user can plot
        images, play sounds, etc.
        """
        self.screen.fill((40, 0, 40))

    def render(self):

        self.menu.mainloop([self.events])
        print(START_GAME)

        return START_GAME