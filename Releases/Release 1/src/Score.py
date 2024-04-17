import pygame

class Score:
    
    def __init__(self, screen):
        
        pygame.font.init()
        self.currentScore = 0
        self.totalScore = 0
        self.screen = screen
        self.font = pygame.font.Font(None, 20)

    def increaseScore(self, num):

        self.currentScore += num

    def update(self):
        
        self.msg = "Score: "+str(self.currentScore)
        self.text = self.font.render(self.msg, 1, (0, 255, 0))
        self.screen.blit(self.text, (3, 585))