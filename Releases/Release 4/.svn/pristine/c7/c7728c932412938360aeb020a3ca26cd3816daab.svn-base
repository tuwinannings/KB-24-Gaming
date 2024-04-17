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
        self.kills = 0
        
        self.highScore = self.loadHighScore()

        self.setUpDisplay()

    def setUpDisplay(self):

        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Neon Blaster - v4.0")

    def printScores(self):

        self.printToScreen("RANK", 40, 65)
        self.printToScreen("NAME", 158, 65)
        self.printToScreen("SCORE", 275, 65)
        for i in range(0, len(self.highScore), 1):
            self.printToScreen(str(i+1), 40, (i*35)+100)
            self.printToScreen("AAA", 158, (i*35)+100)
            self.printToScreen(str(self.highScore[-i - 1]), 275, (i*35)+100)
            if i == 9: break


        pygame.display.flip()

    def increaseScore(self, num):

        self.currentScore += num
        self.kills += 1

    def update(self, wave, level, health):
        
        self.msg = "Score: "+str(self.currentScore)+"  Wave: "+str(wave)+"  Level: "+str(level)+"  Health: "+str(health)
        self.text = self.font.render(self.msg, 1, (0, 255, 0))
        self.screen.blit(self.text, (3, 585))

    def run(self):

        self.running = True

        self.setHighScore()
        self.printScores()

        while self.running == True:
            
            self.checkEvent()            

    def setHighScore(self):
        
        self.highScore.append(self.currentScore)
        self.highScore.sort()
        self.saveHighScore()

    def loadHighScore(self):

        return pickle.load(open("resources/highscore.txt", "rb"))

    def saveHighScore(self):

        pickle.dump(self.highScore, open("resources/highscore.txt", "wb"))

    def checkEvent(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.running = False
                    Main.Main().run()

    def printToScreen(self, msg, x, y):
        text = self.fontHighScore.render(msg, 1, (0, 255, 0))
        self.screen.blit(text, (x, y))