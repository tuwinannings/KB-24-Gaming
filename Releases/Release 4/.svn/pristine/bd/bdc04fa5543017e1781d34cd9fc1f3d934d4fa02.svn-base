import pygame
import sys

class Explosion(pygame.sprite.Sprite):
    explosionSound = None

    def __init__(self, bullet, play_sound = True):
        pygame.sprite.Sprite.__init__(self)

        if Explosion.explosionSound is None:
            Explosion.explosionSound = pygame.mixer.Sound("sound/explosion_sound.wav")
        self.explosionSound = Explosion.explosionSound

        self.animcycle = 3
        self.images = []
        self.defaultlife = 12
        #img = pygame.image.load('data/Explosion.png')

        self.images.append(pygame.image.load('images/Explosion1.png').convert_alpha())
        self.images.append(pygame.image.load('images/Explosion2.png').convert_alpha())
        self.images.append(pygame.image.load('images/Explosion3.png').convert_alpha())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bullet.rect.center

        if play_sound == True:
            self.explosionSound.play()

    def update(self):
        
        self.defaultlife = self.defaultlife - 1
        self.image = self.images[self.defaultlife/self.animcycle%3]
        if self.defaultlife <= 0: self.kill()
