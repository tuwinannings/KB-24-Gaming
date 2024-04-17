import pygame

from threading import Timer
from EnemyShip import EnemyShip
from EnemyBullet_white import EnemyBullet_white

class EnemyShip_white(EnemyShip):
    image = None

    def __init__(self, location):

        EnemyShip.__init__(self, location)

        if EnemyShip_white.image is None:
            EnemyShip_white.image = pygame.image.load("images/EnemyShip_white.png").convert_alpha()
        self.image = EnemyShip_white.image

        self.rect = self.image.get_rect()

        self.health = 50
        self.moveSpeed = 2
        self.shootSpeed = 1

    def shootBullet(self, num_bullets):

        if self.shootAble == True and num_bullets < self.maxBullets:

            self.shootAble = False

            self.shootInterval = Timer(self.shootSpeed, self.resetShootAble)
            self.shootInterval.start()

            bullets = [EnemyBullet_white((self.position[0] - 8, self.position[1] - 12)), EnemyBullet_white((self.position[0] + 8, self.position[1] - 12))]

            return bullets
