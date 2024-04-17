import pygame

from Bullet import Bullet

class EnemyBullet_blue(Bullet):
    image = None

    def __init__(self, location):

        Bullet.__init__(self, location)

        if EnemyBullet_blue.image is None:
            EnemyBullet_blue.image = pygame.image.load("images/EnemyBullet_blue.png").convert_alpha()
        self.image = EnemyBullet_blue.image
        self.rect = self.image.get_rect()

        self.damage = 20
