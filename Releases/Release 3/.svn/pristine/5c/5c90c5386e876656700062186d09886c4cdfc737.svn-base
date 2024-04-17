import pygame
from pygame.locals import *

import NeonBlaster

class Main:

    def __init__(self):
         self.setUpDisplay()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v3.0")
        self.background1 = pygame.image.load("data/neonblasterbackground.png")
        self.background2 = pygame.image.load("data/neonblastercontrols.png")
        self.showbackground = self.background1
        self.cur_screen = "main"
        self.screen.blit(self.showbackground, (0,0))

        self.images = [pygame.image.load("data/start.png"), pygame.image.load("data/instructions.png"), pygame.image.load("data/quit.png")]
        self.posities = ((161, 351), (142, 407), (162, 466))
        self.huidigepos = 0
        
    def run(self):

        self.running = True

        while self.running == True:

            self.screen.blit(self.showbackground, (0,0))

            self.screen.blit(self.images[self.huidigepos], self.posities[self.huidigepos])

            self.checkEvent()

            pygame.display.flip()


    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            if event.type == KEYDOWN:

                if self.cur_screen == "main":
                
                    if event.key == K_DOWN:
                        self.huidigepos += 1

                        if self.huidigepos > 2:
                            self.huidigepos = 0
                    if event.key == K_UP:
                        self.huidigepos -= 1

                        if self.huidigepos < 0:
                            self.huidigepos = len(self.posities) - 1

                    if event.key == K_SPACE:

                        if self.huidigepos == 0:
                            self.running = False
                            NeonBlaster.NeonBlaster().run()

                        if self.huidigepos == 1:
                            self.cur_screen = "instructions"
                            self.showbackground = self.background2
                            self.images = [pygame.image.load("data/back.png")]
                            self.posities = [(-5, 552)]
                            self.huidigepos = 0

                        if self.huidigepos == 2:
                            self.running = False

                elif self.cur_screen == "instructions":

                    if event.key == K_SPACE:

                        self.cur_screen = "main"
                        self.showbackground = self.background1
                        self.images = [pygame.image.load("data/start.png"), pygame.image.load("data/instructions.png"), pygame.image.load("data/quit.png")]
                        self.posities = ((161, 351), (142, 407), (162, 466))
                        self.huidigepos = 0

if __name__ == "__main__":
    Main().run()