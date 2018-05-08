from ..constants.Contstants import *
import pygame

# ABSTRACT
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.

        # Background image
        self.backgroundImage = None

        self.world_shift = 0
        # How far this world has been scrolled left/right
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        pass

    def draw(self, screen):
        """ Draw everything on this level. """

        screen.blit(self.background, (self.world_shift // 3, 0))

