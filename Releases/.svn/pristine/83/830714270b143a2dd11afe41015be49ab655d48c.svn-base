import pygame, random

from threading import Timer

class EnemyShip(pygame.sprite.Sprite):

    def __init__(self, location):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("EnemyShip.png")
        self.rect = self.image.get_rect()
        
        self.receiveScore = 10
        self.health = 1
        self.moveSpeed = 0.2
        self.shootSpeed = 0

        self.moveDir = random.randint(-1, 1)
        self.moveMax = random.randint(50, 200)
        self.moveCount = 0
        self.intervalWait = False

        self.beginLocation = location
        self.position = location
        self.rect.center = location

    def move(self, dir):

        if self.moveCount < self.moveMax:
            self.moveCount += 1
            self.position = (self.position[0] + (dir * self.moveSpeed), self.position[1])
            self.checkOutofScreen()
        elif self.intervalWait == False:
            self.moveInterval = Timer(random.randint(1, 3), self.randomMove)
            self.moveInterval.start()
            self.intervalWait = True

    def randomMove(self):
        self.moveDir = random.randint(-1, 1)
        self.moveMax = random.randint(50, 200)
        self.moveCount = 0
        self.intervalWait = False

    def checkOutofScreen(self):

        if self.position[0] - (self.rect.width / 2) <= 0:
            self.position = (0 + (self.rect.width / 2), self.position[1])

        if self.position[0] + (self.rect.width / 2) >= 400:
            self.position = (400 - (self.rect.width / 2), self.position[1])

    def shootBullet(self):
        
        nothing = 0

    def addDamage(self, dmg, score):

        self.health -= dmg
        self.checkHealth(score)

    def checkHealth(self, score):

        if self.health <= 0:

            score.increaseScore(self.receiveScore)
            self.kill()

    def update(self):

        self.move(self.moveDir)
        self.rect.center = self.position