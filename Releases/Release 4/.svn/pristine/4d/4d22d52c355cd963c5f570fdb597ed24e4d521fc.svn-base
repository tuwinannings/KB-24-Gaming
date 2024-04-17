import pygame
import random

from threading import Timer
from EnemyBullet import EnemyBullet

class EnemyShip(pygame.sprite.Sprite):
    image = None


    def __init__(self, location):
        
        pygame.sprite.Sprite.__init__(self)
        if EnemyShip.image is None:
            EnemyShip.image = pygame.image.load("images/EnemyShip.png").convert_alpha()

        self.image = EnemyShip.image
        self.rect = self.image.get_rect()

        self.health = 20
        self.moveSpeed = 2
        self.shootSpeed = 2
        self.maxBullets = 10
        self.shootAble = True

        self.receiveScore = 10
        self.moveDir = random.randint(-1, 1)
        self.moveMax = random.randint(20, 50)
        self.moveCount = 0
        self.intervalWait = False
        self.position = location
        self.beginlocation = location
        self.vertraging = 0

    def move(self, dir):

        if self.moveCount < self.moveMax:
            self.moveCount += 1
            self.position = (self.position[0] + (dir * self.moveSpeed), self.position[1])
            self.checkOutofScreen()
        elif self.intervalWait == False:
            self.vertraging = dir * self.moveSpeed
            self.moveInterval = Timer(random.randint(1, 3), self.randomMove)
            self.moveInterval.start()
            self.intervalWait = True

    def randomMove(self):

        self.moveDir = random.randint(-1, 1)
        self.moveMax = random.randint(20, 50)
        self.moveCount = 0
        self.intervalWait = False

    def checkOutofScreen(self):

        if self.position[0] - (self.rect.width / 2) <= 0:
            self.position = (0 + (self.rect.width / 2), self.position[1])

        if self.position[0] + (self.rect.width / 2) >= 400:
            self.position = (400 - (self.rect.width / 2), self.position[1])
            
    def shootBullet(self, num_bullets):

        if self.shootAble == True and num_bullets < self.maxBullets:

            self.shootAble = False

            self.shootInterval = Timer(self.shootSpeed, self.resetShootAble)
            self.shootInterval.start()

            bullet = EnemyBullet((self.position[0], self.position[1] - 12))

            return [bullet]

    def resetShootAble(self):

        self.shootAble = True

    def addDamage(self, dmg, score):

        self.health -= dmg
        self.checkHealth(score)

    def checkHealth(self, score):

        if self.health <= 0:

            score.increaseScore(self.receiveScore)
            self.kill()

    def checkYPosition(self):

        ingevlogen = False

        if self.position[1] > self.beginlocation[1] - 500:

            self.position = (self.position[0], self.position[1] - (self.moveSpeed / 2))
        
        else:
            ingevlogen = True

        return ingevlogen

    def handleVertraging(self):

        if self.intervalWait and self.vertraging - 0.1 > 0:
            self.vertraging -= 0.1
            self.position = (self.position[0] + self.vertraging, self.position[1])
        if self.intervalWait and self.vertraging + 0.1 < 0:
            self.vertraging += 0.1
            self.position = (self.position[0] + self.vertraging, self.position[1])
        self.checkOutofScreen()
    
    def update(self):

        self.handleVertraging()
        if self.checkYPosition() == True:
            self.move(self.moveDir)
        self.rect.center = self.position