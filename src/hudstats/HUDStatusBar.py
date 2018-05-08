import pygame
from ..constants.Contstants import *

class HUDStatusBar:

    def __init__(self, display, leftSide):
        self.leftSide = leftSide
        self.display = display
        self.icon = None




    def update(self, updateTime, healthSize, icon):

        if self.leftSide:
            self.display.blit(icon, (10, 10))
        else:
            icon = pygame.transform.flip(icon, True, False)
            self.display.blit(icon, (SCREEN_WIDTH - 52, 10))



        if self.leftSide:
            pygame.draw.rect(self.display, GREEN, (44, 25, healthSize, 25))
        else:
            pygame.draw.rect(self.display, RED, (SCREEN_WIDTH - 44, 25, -healthSize, 25))


    def setIcon(self, icon):
        self.icon = icon
