from Bullet import Bullet
import pygame

class FriendlyBullet(Bullet):
    image = None

    def __init__(self, location):

        Bullet.__init__(self, location)

        if FriendlyBullet.image is None:
            FriendlyBullet.image = pygame.image.load("images/FriendlyBullet.png").convert_alpha()
            
        self.image = FriendlyBullet.image
        self.rect = self.image.get_rect()
