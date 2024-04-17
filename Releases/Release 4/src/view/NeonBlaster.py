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
from NewWave import NewWave
from Explosion import Explosion

class NeonBlaster:

    def __init__(self):

        self.setUpDisplay()
        self.levels = self.createLevels();
        self.cur_level = self.levels[0]
        self.pauze = False
        self.createSpriteGroups()
        self.createSprites()

        #pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.mixer.init()
        self.pauseSound = pygame.mixer.Sound("sound/pause.wav")
        self.depthBomb = pygame.mixer.Sound("sound/depth_bomb.wav")
        #self.bulletSound = pygame.mixer.Sound("sound/bullet_sound.wav")
        pygame.mixer.music.load("music/game_sound.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()


    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v4.0")
        self.background = pygame.Surface(self.screen.get_size())
        self.bgcolor = (0, 0, 0)
        self.screen.fill(self.bgcolor)
        self.clock = pygame.time.Clock()
        
        bg1 = [pygame.image.load("images/Background.png").convert_alpha(), (0,0), .5]
        bg2 = [pygame.image.load("images/Background.png").convert_alpha(), (0,-650), .5]
        bg3 = [pygame.image.load("images/Background_2.png").convert_alpha(), (0,0), .9]
        bg4 = [pygame.image.load("images/Background_2.png").convert_alpha(), (0,-650), .9]
        bg5 = [pygame.image.load("images/Background_3.png").convert_alpha(), (0,0), 1.2]
        bg6 = [pygame.image.load("images/Background_3.png").convert_alpha(), (0,-650), 1.2]
        bg7 = [pygame.image.load("images/Background_4.png").convert_alpha(), (0,0), 1.5]
        bg8 = [pygame.image.load("images/Background_4.png").convert_alpha(), (0,-650), 1.5]
        self.background_images = [bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8]

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
        
        self.score = Score(self.screen)

        self.displayNextWaveText()

    def createEnemySprites(self):

        allEnemies = self.cur_level.getCurWave().getEnemies()
        for e in allEnemies:
            self.allEnemies.add(e)
            self.allSprites.add(e)

    def destroyAllBullets(self):

        self.depthBomb.play()

        for bullet in self.allBullets:

            expl = Explosion(bullet, False)
            self.allSprites.add(expl)
            bullet.kill()

    def checkAllEnemiesDied(self):

        if len(self.allEnemies) <= 0:

            if not isinstance(self.cur_level.cur_wave.getNextWave(), Wave):
                self.destroyAllBullets()
                self.cur_level = self.cur_level.getNextLevel()
                self.displayNextWaveText()
            else:
                self.destroyAllBullets()
                self.cur_level.cur_wave = self.cur_level.cur_wave.getNextWave()
                self.displayNextWaveText()

            self.createEnemySprites()

    def handleBackgrounds(self):

        for x in range(0, len(self.background_images)):
            if x % 2 == 0:
                self.screen.blit(self.background_images[x][0], self.background_images[x][1])
            else:
                self.screen.blit(self.background_images[x][0], self.background_images[x][1])

    def run(self):

        self.running = True

        while self.running == True:

            self.clock.tick(60)

            self.screen.fill(self.bgcolor)

            self.handleBackgrounds()

            self.checkAllEnemiesDied()

            self.player.checkShield(self.score.kills)

            self.checkEvent()
            self.checkCollisions()

            self.score.update(self.cur_level.getIndexOfCurWave() + 1, self.getIndexOfCurLevel() + 1, self.player.health)
            self.allSprites.draw(self.screen)

            if self.pauze == False:
                self.backgroundScroll()
                self.checkPositions()
                self.allSprites.update()
            else:
                self.screen.blit(pygame.image.load("images/pausebackground.png"), (0, 0))
                
            pygame.display.flip()

        pygame.quit()            

    def displayNextWaveText(self):
        self.new_wave_right = NewWave("right")
        self.allSprites.add(self.new_wave_right)
        self.new_wave_left = NewWave("left")
        self.allSprites.add(self.new_wave_left)

    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == KEYDOWN:
                if event.key == K_p:
                    self.pauseSound.play()
                    if self.pauze == True:
                        self.pauze = False
                        pygame.mixer.music.unpause()
                    else:
                        self.pauze = True
                        pygame.mixer.music.pause()
                if event.key == K_ESCAPE:
                    self.running = False

        keystate = pygame.key.get_pressed()

        if self.player.alive():

            if self.pauze == False:
                if keystate[K_RIGHT]:
                    self.player.move(1)
                if keystate[K_LEFT]:
                    self.player.move(-1)
                if keystate[K_SPACE]:
                    new_bullet = self.player.shootBullet(len(self.friendlyBullets))
                    self.addBulletToGroups(new_bullet)

        else:
            self.depthBomb.play()
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
            if bullet.position[1] > 290:
                if bullet.checkCollisionFriendly(self.player):
                    expl = Explosion(bullet)
                    self.allSprites.add(expl)
                    
                if bullet.position[1] > 330:
                    if bullet.checkCollisionEnemies(self.allEnemies, self.score):
                        expl = Explosion(bullet)
                        self.allSprites.add(expl)
                        
            elif bullet.position[1] < 10:
                bullet.checkCollisionWall(self.wall)

    def checkPositions(self):

        for e in self.allEnemies:
            if e.position[0] >= self.player.position[0] - 8 and e.position[0] <= self.player.position[0] + 8:
                new_bullets = e.shootBullet(len(self.enemyBullets))
                if new_bullets != None and len(new_bullets) > 0:
                    for i in range(len(new_bullets)):
                       self.addBulletToGroups(new_bullets[i])

    def createLevels(self):
        
        waves = []
        bestand = open("resources/waves.txt", "r")
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

        level1.setNextLevel(level2)
        level2.setNextLevel(level1)
        
        levels = [level1, level2]

        return levels

    def getIndexOfCurLevel(self):

        index = -1

        for x in range(0, len(self.levels), 1):

            if self.cur_level == self.levels[x]:

                index = x

        return index

    def backgroundScroll(self):

        for x in range(0, len(self.background_images)):
            self.background_images[x][1] = (self.background_images[x][1][0], self.background_images[x][1][1] + self.background_images[x][2])

            if x % 2 == 0:
                if  self.background_images[x][1][1] > 650:
                     self.background_images[x][1] = (self.background_images[x][1][0], -650)
                if  self.background_images[x][1][1] > 650:
                     self.background_images[x][1] = (self.background_images[x][1][0], -650)
            else:
                if  self.background_images[x][1][1] > 650:
                     self.background_images[x][1] = (self.background_images[x][1][0], -650)
                if  self.background_images[x][1][1] > 650:
                     self.background_images[x][1] = (self.background_images[x][1][0], -650)


