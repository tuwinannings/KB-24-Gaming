import pygame

from threading import Timer
from FriendlyBullet import FriendlyBullet

class FriendlyShip(pygame.sprite.Sprite):
    
    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/FriendlyShip.png")
        self.rect = self.image.get_rect()

        self.health = 100
        self.moveSpeed = 0.4
        self.shootSpeed = 0.1
        self.maxBullets = 30
        self.shootAble = True
        self.position = location

    def move(self, dir):

        self.position = (self.position[0] + (dir * self.moveSpeed), self.position[1])
        self.checkOutofScreen()
    
    def shootBullet(self, num_bullets):

        if self.shootAble == True and num_bullets < self.maxBullets:

            self.shootAble = False

            self.shootInterval = Timer(self.shootSpeed, self.resetShootAble)
            self.shootInterval.start()

            bullet = FriendlyBullet((self.position[0], self.position[1] - 12))

            return bullet

    def resetShootAble(self):

        self.shootAble = True

    def checkOutofScreen(self):

        if self.position[0] - (self.rect.width / 2) <= 0:
            self.position = (0 + (self.rect.width / 2), self.position[1])

        if self.position[0] + (self.rect.width / 2) >= 400:
            self.position = (400 - (self.rect.width / 2), self.position[1])

    def addDamage(self, dmg):
 
        self.health -= dmg
        self.checkHealth()

    def checkHealth(self):

        if self.health <= 0:

            self.kill()


    def update(self):

        self.rect.center = self.position

    