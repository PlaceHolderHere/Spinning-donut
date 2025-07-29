import math
import pygame

# Constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
FPS = 30

# Pygame Init
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variables
running = True

while running:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # WIN FILL
    win.fill((0, 0, 0))

    # DISPLAY UPDATE
    pygame.display.update()
