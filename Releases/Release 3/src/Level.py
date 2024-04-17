import pygame

from EnemyShip import EnemyShip
from Wave import Wave

class Level:

    def __init__(self, waves):

        self.waves = self.createWaves(waves)
        self.cur_wave = self.waves[0]

    def getIndexOfCurWave(self):

        index = -1

        for x in range(0, len(self.waves), 1):

            if self.cur_wave == self.waves[x]:

                index = x

        return index

    def createWaves(self, waves):

        all_waves = []
        last_wave = ()

        for x in range(len(waves)):

            enemies = []
            
            for i in range(len(waves[x])):

                for j in range(len(waves[x][i])):

                    if waves[x][i][j] == 1:

                        enemies.append(EnemyShip((j * 16, i * 16 + 348)))

            new_wave = Wave(enemies)

            if isinstance(last_wave, Wave):
                last_wave.setNextWave(new_wave)
                
            last_wave = new_wave
            all_waves.append(last_wave)

        return all_waves

    def getCurWave(self):

        return self.cur_wave

