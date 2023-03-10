import pygame
from settings import *


def bound(screen, color: tuple):

    pygame.draw.rect(screen, color, (0, 55, Settings.SCREEN_WIDTH, 20))
    pygame.draw.rect(screen, color, (0, 55, 20, (Settings.SCREEN_HEIGHT - 55)))
    pygame.draw.rect(
        screen, color, ((Settings.SCREEN_WIDTH - 20), 55, 20, (Settings.SCREEN_HEIGHT - 55))
    )
    pygame.draw.rect(
        screen, color, (20, (Settings.SCREEN_HEIGHT - 20), (Settings.SCREEN_WIDTH - 40), 20)
    )
