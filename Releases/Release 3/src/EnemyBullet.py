from Bullet import Bullet
import pygame

class EnemyBullet(Bullet):

    def __init__(self, location):

        Bullet.__init__(self, location)
        self.image = pygame.image.load("data/EnemyBullet.png")
        self.rect = self.image.get_rect()
