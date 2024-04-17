import pygame
import random

from threading import Timer

class UpperWall(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/UpperWall.png")
        self.rect = self.image.get_rect()
        
        self.bounce = True
        self.bounceStraight = True

        self.position = (200, 0)
        self.show()

    def show(self):

        self.bounce = True
        self.image.set_alpha(255)
        self.changeInterval = Timer(random.randint(5, 20), self.hide)
        self.changeInterval.start()

    def hide(self):

        self.bounce = False
        self.image.set_alpha(120)
        self.changeInterval = Timer(random.randint(5, 20), self.show)
        self.changeInterval.start()