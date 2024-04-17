import pygame
from pygame.locals import *

from FriendlyShip import FriendlyShip
from Bullet import Bullet
from UpperWall import UpperWall
from EnemyShip import EnemyShip
from Score import Score

class NeonBlaster:

    def __init__(self):

        self.setUpDisplay()
        self.createSpriteGroups()
        self.createSprites()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v1.0")
        self.background = pygame.Surface(self.screen.get_size())
        self.bgcolor = (0, 0, 0)
        self.screen.fill(self.bgcolor)

    def createSpriteGroups(self):

        self.allSprites = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.friendlyBullets = pygame.sprite.Group()
        self.allEnemies = pygame.sprite.Group()

    def createSprites(self):

        self.player = FriendlyShip((200, 300))
        self.allSprites.add(self.player)

        self.wall = UpperWall()
        self.allSprites.add(self.wall)

        self.enemy1 = EnemyShip((300, 550))
        self.enemy2 = EnemyShip((100, 550))
        self.allSprites.add(self.enemy1)
        self.allEnemies.add(self.enemy1)
        self.allSprites.add(self.enemy2)
        self.allEnemies.add(self.enemy2)

        self.score = Score(self.screen)

    def run(self):

        self.running = True

        while self.running == True:

            self.screen.fill(self.bgcolor)

            self.checkEvent()
            self.checkCollisions()

            self.allSprites.update()
            self.score.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()

    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

        keystate = pygame.key.get_pressed()

        if self.player.alive():
            
            if keystate[K_RIGHT]:
                self.player.move(1)
            if keystate[K_LEFT]:
                self.player.move(-1)
            if keystate[K_SPACE]:
                new_bullet = self.player.shootBullet(len(self.friendlyBullets))
                self.addBulletToGroups(new_bullet)
            if keystate[K_w]:
                self.wall.show()
            if keystate[K_d]:
                self.wall.hide()

    def addBulletToGroups(self, bullet):

        if isinstance(bullet, Bullet):
            self.allSprites.add(bullet)
            self.allBullets.add(bullet)
            self.friendlyBullets.add(bullet)

    def checkCollisions(self):

        for bullet in self.allBullets:

            bullet.checkCollisionFriendly(self.player)
            bullet.checkCollisionEnemies(self.allEnemies, self.score)
            bullet.checkCollisionWall(self.wall)

if __name__ == "__main__":
    NeonBlaster().run()
