from .Level import Level
from ..path.ImagePathResolver import ImagePathResolver
import pygame
from ..constants.Contstants import *

class Level1(Level):


    def __init__(self, player):
        super().__init__(player)
        pathResolver = ImagePathResolver()
        path = pathResolver.resolve("bg.jpg")
        image = pygame.image.load(path).convert()
        self.background = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.set_colorkey(WHITE)
