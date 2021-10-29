import pygame

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = {'x': SCREEN_WIDTH / 2, 'y': SCREEN_HEIGHT / 2}

MOUSE_POS = pygame.mouse.get_pos()

POND_DIM = 128