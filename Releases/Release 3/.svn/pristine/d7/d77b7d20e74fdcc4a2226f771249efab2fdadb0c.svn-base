import pygame
import pickle

from pygame.locals import *

import Main


class Score:
    
    def __init__(self, screen):
        
        pygame.font.init()
        self.currentScore = 0
        self.totalScore = 0
        self.screen = screen
        self.font = pygame.font.Font(None, 20)
        self.fontHighScore = pygame.font.Font(None, 35)
        self.highScore = []

        self.setUpDisplay()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v3.0")
        self.background = pygame.image.load("data/highscorebackground.png")
        self.screen.blit(self.background, (0,0))

    def increaseScore(self, num):

        self.currentScore += num

    def update(self, wave, level, health):
        
        self.msg = "Score: "+str(self.currentScore)+"  Wave: "+str(wave)+"  Level: "+str(level)+"  Health: "+str(health)
        self.text = self.font.render(self.msg, 1, (0, 255, 0))
        self.screen.blit(self.text, (3, 585))

    def run(self):

        self.running = True

        self.highScore = self.loadHighScore()
        self.setHighScore(self.currentScore)
        self.currentScore = 0
        self.screen.blit(self.background, (0,0))

        self.printToScreen("RANK    NAME    SCORE", 55, 65)
        for i in range(len(self.highScore)):
                self.printToScreen(str(i+1)+"            AAA       "+str(self.highScore[-i+-1]), 55, (i*35)+100)
                if i == 9: break
                

        pygame.display.flip()

        while self.running == True:
            
            self.checkEvent()            

    def setHighScore(self, newScore):
        
        self.highScore.append(newScore)
        self.highScore.sort()
        self.saveHighScore(self.highScore)

    def loadHighScore(self):

        return pickle.load( open("data/highscore.txt", "rb"))

    def saveHighScore(self, highScore):

        pickle.dump(highScore, open("data/highscore.txt", "wb"))

    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.running = False
                    Main.Main().run()

    def printToScreen(self, msg, x, y):
        text = self.fontHighScore.render(msg, 1, (0, 255, 0))
        self.screen.blit(text, (x, y))