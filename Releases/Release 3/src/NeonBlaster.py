import pygame
from pygame.locals import *

from FriendlyShip import FriendlyShip
from Bullet import Bullet
from EnemyBullet import EnemyBullet
from FriendlyBullet import FriendlyBullet
from UpperWall import UpperWall
from Wave import Wave
from Score import Score
from Level import Level

class NeonBlaster:

    def __init__(self):

        self.levels = self.createLevels();
        self.cur_level = 0

        self.setUpDisplay()
        self.createSpriteGroups()
        self.createSprites()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v3.0")
        self.background = pygame.Surface(self.screen.get_size())
        self.bgcolor = (0, 0, 0)
        self.screen.fill(self.bgcolor)

    def createSpriteGroups(self):

        self.allSprites = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.friendlyBullets = pygame.sprite.Group()
        self.enemyBullets = pygame.sprite.Group()
        self.allEnemies = pygame.sprite.Group()

    def createSprites(self):

        self.player = FriendlyShip((200, 300))
        self.allSprites.add(self.player)

        self.wall = UpperWall()
        self.allSprites.add(self.wall)
        
        self.createEnemySprites()

        #self.enemy1 = EnemyShip((300, 550))
        #self.enemy2 = EnemyShip((100, 550))
        #self.allSprites.add(self.enemy1)
        #self.allEnemies.add(self.enemy1)
        #self.allSprites.add(self.enemy2)
        #self.allEnemies.add(self.enemy2)

        self.score = Score(self.screen)

    def createEnemySprites(self):

        allEnemies = self.levels[self.cur_level].getCurWave().getEnemies()
        for e in allEnemies:
            self.allEnemies.add(e)
            self.allSprites.add(e)


    def run(self):

        self.running = True

        while self.running == True:

            if len(self.allEnemies) <= 0:
                
                if not isinstance(self.levels[self.cur_level].cur_wave.getNextWave(), Wave):
                    self.cur_level += 1
                else:
                    self.levels[self.cur_level].cur_wave = self.levels[self.cur_level].cur_wave.getNextWave()

                self.createEnemySprites()

            self.screen.fill(self.bgcolor)

            self.checkEvent()
            self.checkCollisions()
            self.checkPositions()

            self.allSprites.update()
                
            self.score.update(self.levels[self.cur_level].getIndexOfCurWave() + 1, self.cur_level + 1, self.player.health)
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
        else:
            self.running = False
            self.score.run()

    def addBulletToGroups(self, bullet):

        if isinstance(bullet, Bullet):
            self.allSprites.add(bullet)
            self.allBullets.add(bullet)
            if isinstance(bullet, FriendlyBullet):
                self.friendlyBullets.add(bullet)
            if isinstance(bullet, EnemyBullet):
                self.enemyBullets.add(bullet)

    def checkCollisions(self):

        for bullet in self.allBullets:
            if bullet.position[1]>290:
                bullet.checkCollisionFriendly(self.player)
                bullet.checkCollisionEnemies(self.allEnemies, self.score)
            elif bullet.position[1]<10:
                bullet.checkCollisionWall(self.wall)

    def checkPositions(self):

        for e in self.allEnemies:
            if e.position[0] >= self.player.position[0] - 10 and e.position[0] <= self.player.position[0] + 10:
                new_bullet = e.shootBullet(len(self.enemyBullets))
                if isinstance(new_bullet, Bullet):
                    self.addBulletToGroups(new_bullet)

    def createLevels(self):
        
        waves = []
        bestand = open("data/waves.txt", "r")
        for line in bestand.readlines():
            line = line.strip()
            if line == "<wave>":
                patroon = []
            elif line == "</wave>":
                waves.append(patroon)
            elif len(line) > 0:
                line = line.lstrip('[')
                line = line.rstrip(']\n')
                line_list = [int(x) for x in line.split(',')]
                patroon.append(line_list)

        bestand.close()

        level1 = Level([waves[0], waves[1]])
        level2 = Level([waves[0], waves[0], waves[2]])
        levels = [level1, level2]

        return levels
