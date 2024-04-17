import pygame
from pygame.locals import *

from threading import Timer
from FriendlyBullet import FriendlyBullet

class FriendlyShip(pygame.sprite.Sprite):
    image = None

    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)
        if FriendlyShip.image is None:
            FriendlyShip.image = pygame.image.load("images/FriendlyShip.png").convert_alpha()
        self.image = FriendlyShip.image
        
        self.rect = self.image.get_rect()

        self.health = 100
        self.moveSpeed = 3.5
        self.shootSpeed = 0.1
        self.maxBullets = 30
        self.shootAble = True
        self.position = location
        self.shield = False
        self.vertraging = 0

    def move(self, dir):
        self.vertraging = dir * self.moveSpeed
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

        if self.shield == False:
            self.health -= dmg
            self.checkHealth()

    def checkHealth(self):

        if self.health <= 0:
            
            self.kill()

    def checkShield(self, kills):
        
        if (kills+1) % 10 == 0:
            self.showShield()

    def showShield(self):
        if self.shield == False:
            self.shield = True
            self.image = pygame.image.load("images/Shield.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.shieldInterval = Timer(8, self.hideShield)
            self.shieldInterval.start()

    def hideShield(self):
        self.shield = False
        self.image = FriendlyShip.image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.shieldInterval.cancel()

    def handleVertraging(self):
        keystate = pygame.key.get_pressed()

        if not keystate[K_RIGHT] and self.vertraging - 0.1 > 0:
            self.vertraging -= 0.1
            self.position = (self.position[0] + self.vertraging, self.position[1])
        if not keystate[K_LEFT] and self.vertraging + 0.1 < 0:
            self.vertraging += 0.1
            self.position = (self.position[0] + self.vertraging, self.position[1])
        self.checkOutofScreen()

    def update(self):
        self.handleVertraging()
        self.rect.center = self.position

    