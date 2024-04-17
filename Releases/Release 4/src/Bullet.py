import pygame

class Bullet(pygame.sprite.Sprite):
    image = None

    def __init__(self, location):

        pygame.sprite.Sprite.__init__(self)

        if Bullet.image is None:
            Bullet.image = pygame.image.load("images/Bullet.png").convert_alpha()
        self.image = Bullet.image

        self.rect = self.image.get_rect()

        self.damage = 10
        self.moveSpeed = (0, 4)
        self.lifeSpan = 1

        self.position = location
        self.rect.center = location

    def checkCollisionFriendly(self, friendly):

        if self.rect.colliderect(friendly):

            self.collideFriendly(friendly)

            return True

    def collideFriendly(self, friendly):
        friendly.addDamage(self.damage)
        self.kill()

    def checkCollisionEnemies(self, enemies, score):

        for enemy in enemies:

            if self.rect.colliderect(enemy):

                self.collideEnemy(enemy, score)

                return True

    def collideEnemy(self, enemy, score):

        enemy.addDamage(self.damage, score)
        self.kill()

    def checkCollisionWall(self, wall):
        
        if self.rect.colliderect(wall):

            self.collideWall(wall)

    def collideWall(self, wall):

        if wall.bounce == True:

            if wall.bounceStraight == True:

                self.moveSpeed = (self.moveSpeed[0], self.moveSpeed[1] * -1)

            else:

                nothing = 0
                # Bullet misschien in de toekomst schuin laten afkaatsen
   
    def checkOutofScreen(self):

        if self.position[1] >= 600:
            self.kill()
        
        if self.position[1] <= 0:
            self.position = (self.position[0],  600)
            self.lifeSpan -= 1
            self.checkLifeSpan()

    def checkLifeSpan(self):
        
        if self.lifeSpan < 0:
            self.kill()

    def update(self):
        
        self.position = (self.position[0] - self.moveSpeed[0], self.position[1] - self.moveSpeed[1])
        self.checkOutofScreen()
        self.rect.center = self.position
