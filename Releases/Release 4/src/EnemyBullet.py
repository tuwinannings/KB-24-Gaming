from Bullet import Bullet
import pygame

class EnemyBullet(Bullet):
    image = None

    def __init__(self, location):

        Bullet.__init__(self, location)
        if EnemyBullet.image is None:
            EnemyBullet.image = pygame.image.load("images/EnemyBullet.png").convert_alpha()
        self.image = EnemyBullet.image
        self.rect = self.image.get_rect()
