import pygame

from Bullet import Bullet

class EnemyBullet_white(Bullet):
    image = None

    def __init__(self, location):

        Bullet.__init__(self, location)

        if EnemyBullet_white.image is None:
            EnemyBullet_white.image = pygame.image.load("images/EnemyBullet_white.png").convert_alpha()
        self.image = EnemyBullet_white.image
        self.rect = self.image.get_rect()

        self.damage = 30
        self.moveSpeed = (0, 6)
