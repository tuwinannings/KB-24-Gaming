import pygame
from threading import Timer

class NewWave(pygame.sprite.Sprite):

    def __init__(self, dir):

        pygame.sprite.Sprite.__init__(self)

        if dir == "right":
            self.image = pygame.image.load("images/new_wave_upper.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.position = (550, 100)
            self.moveSpeed = 5
        elif dir == "left":
            self.image = pygame.image.load("images/new_wave_bottom.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.position = (-150, 100)
            self.moveSpeed = -5
        self.pause = False

    def checkCenter(self):
    
        if self.position[0] == 200:

            self.pause = True
            Timer(2, self.unpause).start()

    def unpause(self):
        
        self.pause = False
        self.moveSpeed *= 2.5

    def checkOutofScreen(self):

        if self.position[0] >= 550 or self.position[0] <= -150:

            self.kill();

    def update(self):

        if self.pause == False:
            self.position = (self.position[0] - self.moveSpeed, self.position[1])
            self.rect.center = self.position
            self.checkCenter()
            self.checkOutofScreen()


