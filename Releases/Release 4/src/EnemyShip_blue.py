import pygame

from threading import Timer
from EnemyShip import EnemyShip
from EnemyBullet_blue import EnemyBullet_blue

class EnemyShip_blue(EnemyShip):
    image = None

    def __init__(self, location):

        EnemyShip.__init__(self, location)

        if EnemyShip_blue.image is None:
            EnemyShip_blue.image = pygame.image.load("images/EnemyShip_blue.png").convert_alpha()
        self.image = EnemyShip_blue.image

        self.rect = self.image.get_rect()
        
        self.health = 50
        self.moveSpeed = 2
        self.shootSpeed = 2

    def shootBullet(self, num_bullets):

        if self.shootAble == True and num_bullets < self.maxBullets:

            self.shootAble = False

            self.shootInterval = Timer(self.shootSpeed, self.resetShootAble)
            self.shootInterval.start()

            bullet = EnemyBullet_blue((self.position[0], self.position[1] - 12))

            return [bullet]

