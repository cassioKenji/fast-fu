from sys import exit

import pygame
from pygame.locals import *

from core.game_settings import screen_settings

defaults = dict(screen_settings)

pygame.init()

class Game():
    def __init__(self):
        self.ScreenSetup(dict(screen_settings))
        
        while True:
            self.MainGameLoop()

    def MainGameLoop(self):
        self.GetEvents()
        self.Tick()
        self.Draw()

    def Tick(self):
        pass

    def Draw(self):
        pygame.display.update()

    def GetEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    def ScreenSetup(self, screen_settings):
        self.WINDOW_CAPTION = pygame.display.set_caption(screen_settings['WINDOW_TITLE'])
        self.GAME_SCREEN    = pygame.display.set_mode(screen_settings['SCREEN_RES'])

Game()
