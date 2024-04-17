import unittest
import pygame

from NeonBlaster import NeonBlaster
from FriendlyShip import FriendlyShip
from EnemyShip import EnemyShip
from Bullet import Bullet
from UpperWall import UpperWall
from Score import Score

class  Test_NeonBlaster(unittest.TestCase):

    def setUp(self):
        self.game = NeonBlaster()
        self.fship = FriendlyShip((100, 100))
        self.eship = EnemyShip((100, 100))
        self.score = Score(pygame.display.set_mode((400, 600)))
        
    def test_ScreenSize(self):
        size = (400,600)
        self.assertEqual(size, self.game.screen.get_size(), "Venster grote = 400X600")

    def text_FriendlyShip_begin(self):
        x = 100
        y = 100
        fship = FriendlyShip((x,y))
        self.assertEqual(fship.position, (x,y), "De coordinaten zouden ("+str(x)+", "+str(y)+") moeten zijn, maar zijn: "+str(fship.position))

    def test_Creation_Levels(self):
        self.assertEqual(len(self.game.levels), 2, "Er zouden 2 levels moeten zijn, maar er zijn er maar: "+str(len(self.game.levels)))

    def test_Creation_Waves(self):
        numberOfWaves = len(self.game.cur_level.waves)
        self.assertNotEqual(numberOfWaves, 0, "Er zouden waves moeten zijn")

    def test_Length_Wave(self):
        wave1 = self.game.levels[1].waves[0].enemies
        wave2 = self.game.levels[1].waves[1].enemies
        wave3 = self.game.levels[1].waves[2].enemies

        self.assertEqual(len(wave1), 12, "De lengte van de wave zou 12 moeten zijn")
        self.assertEqual(len(wave2), 12, "De lengte van de wave zou 12 moeten zijn")
        self.assertEqual(len(wave3), 22, "De lengte van de wave zou 22 moeten zijn")

    def test_Enemies_in_Wave(self):
        wave1 = self.game.cur_level.getCurWave()
        enemies = wave1.getEnemies()

        self.assertEquals(len(enemies), 12, "Er zouden 12 enemies in de eerst wave moeten zitten.")
        
    def test_FriendlyShip_move_right(self):
        x = 100
        y = 100
        fship = FriendlyShip((x,y))
        fship.move(1)
        self.assertGreater(fship.position[0], x, "de x coordinaat zou groter moeten zijn dan "+str(x)+", maar is: "+str(fship.position[0]))

    def test_FriendlyShip_move_left(self):
        x = 100
        y = 100
        fship = FriendlyShip((x,y))
        fship.move(-1)
        self.assertLess(fship.position[0], x, "de x coordinaat zou kleiner moeten zijn dan "+str(x)+", maar is: "+str(fship.position[0]))

    def test_FriendlyShip_checkOutofScreen(self):
        x = 8
        y = 0
        fship = FriendlyShip((x,y))
        fship.position = (-10,0)
        fship.checkOutofScreen()
        self.assertEqual(fship.position, (x,y), "De coordinaten zouden (8, "+str(y)+") moeten zijn, maar zijn: "+str(fship.position))

    def test_FriendlyShip_shootBullet_MaxBullets(self):
        self.fship.maxBullets = 30
        bullet = self.fship.shootBullet(29)
        self.assertIsInstance(bullet, Bullet, "Geeft een bullet obj terug")
        bullet = self.fship.shootBullet(30)
        self.assertNotIsInstance(bullet, Bullet, "Geeft geen bullet obj terug want max = 30")

    def test_Bullet_Collide_Wall_Bounce(self):
        wall = UpperWall()
        wall.bounceStraight = True
        bullet = Bullet((200, 2))
        bullet.moveSpeed = (0, 0.2)
        bullet.collideWall(wall)
        self.assertEqual(bullet.moveSpeed[1], -0.2, "Snelheid kogel moet -0.2 zijn en is: "+str(bullet.moveSpeed[1]))

    def test_Bullet_Collide_Wall_checkOutofScreen(self):
        wall = UpperWall()
        wall.bounceStraight = False
        bullet = Bullet((200, 0))
        bullet.moveSpeed = (0, 0.2)
        bullet.checkOutofScreen()
        self.assertEqual(bullet.position[1], 600, "y coordinaat kogel moet 600 zijn en is: "+str(bullet.position[1]))

    def test_Bullet_checkLifeSpan(self):
        b = Bullet((10,10))
        b.lifeSpan = -1
        allBullets = pygame.sprite.Group(b)
        self.assertIn(b, allBullets, "in allbullets zit b")
        b.checkLifeSpan()
        self.assertNotIn(b, allBullets, "bullet niet in allbullets")
        
    def test_Bullet_Collide_Friendly(self):
        self.fship.health = 100
        bullet = Bullet((200, 0))
        bullet.damage = 25
        bullet.collideFriendly(self.fship)
        self.assertEqual(self.fship.health, 75, "health friendlyship zou 75 moeten zijn en is: "+str(self.fship.health))

    def test_Friendly_Dies(self):
        self.fship.health = 10
        bullet = Bullet((200, 0))
        bullet.damage = 25
        bullet.collideFriendly(self.fship)
        self.assertEqual(self.fship.health, -15, "health friendlyship zou -15 moeten zijn en is: "+str(self.fship.health))
        self.assertEqual(self.fship.alive(), False, "friendlyship zou dood moeten zijn, maar leeft nog")

    def test_Bullet_Collide_Enemy(self):
        self.eship.health = 100
        bullet = Bullet((200, 0))
        bullet.damage = 25
        bullet.collideEnemy(self.eship, self.score)
        self.assertEqual(self.eship.health, 75, "health enemyship zou 75 moeten zijn en is: "+str(self.eship.health))

    def test_Enemy_Dies(self):
        self.eship.health = 10
        bullet = Bullet((200, 0))
        bullet.damage = 25
        bullet.collideEnemy(self.eship, self.score)
        self.assertEqual(self.eship.health, -15, "health enemyship zou -15 moeten zijn en is: "+str(self.eship.health))
        self.assertEqual(self.eship.alive(), False, "enemyship zou dood moeten zijn, maar leeft nog")

    def test_Enemy_Dies_Score_Increase(self):
        self.score.currentScore = 0
        self.eship.receiveScore = 10
        self.eship.health = 10
        bullet = Bullet((200, 0))
        bullet.damage = 25
        bullet.collideEnemy(self.eship, self.score)
        self.assertEqual(self.score.currentScore, 10, "Huidige score zou 10 moeten zijn en is: "+str(self.score.currentScore))

    def test_setHighScore(self):
        self.score.highScore = []
        self.score.currentScore = 10
        self.score.setHighScore()
        self.score.currentScore = 30
        self.score.setHighScore()
        self.score.currentScore = 50
        self.score.setHighScore()
        self.assertEqual(len(self.score.highScore), 3, "In de highScore lijst horen 3 scores in te zitten" )
        self.assertEqual(self.score.highScore[-1], 50, "Testen van de sort functie in setHighScores")

    def test_Shield_FriendlyShip_Off(self):
        self.fship.health = 100
        self.fship.shield = False
        self.fship.addDamage(20)

        self.assertEquals(self.fship.health, 80, "Fship zou nog 80 leven over moeten hebben.")

    def test_Shield_FriendlyShip_On(self):
        self.fship.health = 100
        self.fship.shield = True
        self.fship.addDamage(20)

        self.assertEquals(self.fship.health, 100, "Fship zou nog 100 leven over moeten hebben.")

if __name__ == '__main__':
    unittest.main()
