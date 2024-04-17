import pygame

class UpperWall(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("UpperWall.png")
        self.rect = self.image.get_rect()
        
        self.health = 0
        self.bounce = True
        self.bounceStraight = True

        self.position = (200, 0)
        self.show()

    def show(self):

        self.bounce = True
        self.image.set_alpha(255)

    def hide(self):

        self.bounce = False
        self.image.set_alpha(120)
