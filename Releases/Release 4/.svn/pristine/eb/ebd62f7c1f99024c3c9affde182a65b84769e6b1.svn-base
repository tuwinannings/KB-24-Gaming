import pygame
from pygame.locals import *

import NeonBlaster

class Main:

    def __init__(self):
        
        pygame.mixer.init()
        self.setUpDisplay()
 
        pygame.mixer.music.load("music/menu_sound.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v4.0")
        self.background1 = pygame.image.load("images/neonblasterbackground.png").convert_alpha()
        self.background2 = pygame.image.load("images/neonblastercontrols.png").convert_alpha()
        self.showbackground = self.background1
        self.cur_screen = "main"
        self.screen.blit(self.showbackground, (0,0))

        self.images = [pygame.image.load("images/start.png"), pygame.image.load("images/instructions.png").convert_alpha(), pygame.image.load("images/quit.png").convert_alpha()]
        self.posities = ((161, 351), (142, 407), (162, 466))
        self.huidigepos = 0
        
    def run(self):

        self.running = True

        while self.running == True:

            self.screen.blit(self.showbackground, (0,0))

            self.screen.blit(self.images[self.huidigepos], self.posities[self.huidigepos])

            self.checkEvent()

            pygame.display.flip()

            self.checkMusicStopped()

    def checkMusicStopped(self):

         if pygame.mixer.music.get_busy() == False:
            self.running = False
            NeonBlaster.NeonBlaster().run()

    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            if event.type == KEYDOWN:

                if self.cur_screen == "main":
                
                    self.checkMainEvents(event)

                elif self.cur_screen == "instructions":

                    self.checkInstructionsEvents(event)

    def checkMainEvents(self, event):

        if event.key == K_DOWN:
            
            self.huidigepos += 1

            if self.huidigepos > 2:
                self.huidigepos = 0
                
        if event.key == K_UP:
            
            self.huidigepos -= 1

            if self.huidigepos < 0:
                self.huidigepos = len(self.posities) - 1

        if event.key == K_RETURN:

            if self.huidigepos == 0:
                pygame.mixer.music.fadeout(800)

            if self.huidigepos == 1:
                self.cur_screen = "instructions"
                self.showbackground = self.background2
                self.images = [pygame.image.load("images/back.png").convert_alpha()]
                self.posities = [(-5, 552)]
                self.huidigepos = 0

            if self.huidigepos == 2:
                self.running = False

    def checkInstructionsEvents(self, event):

        if event.key == K_RETURN:

            self.cur_screen = "main"
            self.showbackground = self.background1
            self.images = [pygame.image.load("images/start.png").convert_alpha(), pygame.image.load("images/instructions.png").convert_alpha(), pygame.image.load("images/quit.png").convert_alpha()]
            self.posities = ((161, 351), (142, 407), (162, 466))
            self.huidigepos = 0

        
if __name__ == "__main__":
    Main().run()