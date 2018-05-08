from pygameMenu.locals import PYGAME_MENU_BACK, PYGAME_MENU_CLOSE, PYGAME_MENU_EXIT, PYGAME_MENU_DISABLE_CLOSE
from ..constants.Contstants import *
import pygame
from pygameMenu.textmenu import TextMenu
import pygameMenu


def bg():
    print("HELLO")


class EndScreen:

    def bg(self):
        print("HELLO")


    def __init__(self, screen, events, context):
        self.font = 'ArcadeClassic Regular'
        self.screen = screen
        self.events = events
        self.context = context






    # Functions
    def mainmenu_background(self):
        """
        Background color of the main menu, on this function user can plot
        images, play sounds, etc.
        """
        self.screen.fill((40, 0, 40))


    def render(self, win):
        # Main menu, pauses execution of the application
        self.menu = pygameMenu.Menu(self.screen,
                                    window_width=SCREEN_WIDTH,
                                    window_height=SCREEN_HEIGHT,
                                    font=pygameMenu.fonts.FONT_NEVIS,
                                    title='You ' + ("WIN" if win else "LOSE"),
                                    title_offsety=5,
                                    menu_alpha=90,
                                    enabled=True,
                                    bgfun=bg,
                                    onclose=PYGAME_MENU_CLOSE)

        self.menu.add_option('Start new game', self.context.restart)
        self.menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function

        self.menu.mainloop([self.events])