import pygame
from ..constants.Contstants import BLACK

class SpriteSheet():


    def __init__(self, filename):
        self.spriteSheet = pygame.image.load(filename)

    def getImage(self, x, y, w, h):

        # Create a new blank image
        image = pygame.Surface([w, h])

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.spriteSheet, (0, 0), (x, y, w, h))

        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)

        # Return the image
        return image
