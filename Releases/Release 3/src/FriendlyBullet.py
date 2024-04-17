from Bullet import Bullet
import pygame

class FriendlyBullet(Bullet):

    def __init__(self, location):

        Bullet.__init__(self, location)
        self.image = pygame.image.load("data/FriendlyBullet.png")
        self.rect = self.image.get_rect()
