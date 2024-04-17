import pygame

from Bullet import Bullet
from threading import Timer

class FriendlyShip(pygame.sprite.Sprite):
    
    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("FriendlyShip.png")
        self.rect = self.image.get_rect()

        self.health = 100 
        self.moveSpeed = 0.4
        self.shootSpeed = 0.1
        self.maxBullets = 30
        self.shootAble = True

        self.beginLocation = location
        self.position = location
        self.rect.center = location

    def move(self, dir):

        self.position = (self.position[0] + (dir * self.moveSpeed), self.position[1])
        self.checkOutofScreen()

    def checkOutofScreen(self):

        if self.position[0] - (self.rect.width / 2) <= 0:
            self.position = (0 + (self.rect.width / 2), self.position[1])

        if self.position[0] + (self.rect.width / 2) >= 400:
            self.position = (400 - (self.rect.width / 2), self.position[1])

    def shootBullet(self, num_friendly_bullets):
        
        if self.shootAble == True and num_friendly_bullets < self.maxBullets:

            self.shootAble = False

            self.shootInterval = Timer(self.shootSpeed, self.resetShootAble)
            self.shootInterval.start()

            bullet = Bullet((self.position[0], self.position[1] - 12))

            return bullet

    def resetShootAble(self):

        self.shootAble = True

    def addDamage(self, dmg):

        self.health -= dmg
        self.checkHealth()

    def checkHealth(self):

        if self.health <= 0:

            self.kill()

    def update(self):

        self.rect.center = self.position

    