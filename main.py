import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_RES = (512, 288)
WINDOW_TITLE = "My Python Game"
pygame.display.set_caption(WINDOW_TITLE)
GAME_SCREEN = pygame.display.set_mode(SCREEN_RES)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

