import math
import pygame

# Constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
FPS = 30
PIXEL_SIZE = 1
K1 = 15
K2 = 1
R1 = 5
R2 = 10

# Pygame Init
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variables
running = True


def generate_torus(r1, r2):
    phi = 0
    phi_spacing = 0.03
    theta_spacing = 0.1
    output = []
    while phi < math.pi * 2:
        theta = 0
        while theta < math.pi * 2:
            output.append([(r2 + r1 * math.cos(theta)) * math.cos(phi), r1 * math.sin(theta),
                           -(r2 + r1 * math.cos(theta)) * math.sin(phi)])
            theta += theta_spacing
        phi += phi_spacing
    return output


torus = generate_torus(R1, R2)
while running:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # WIN FILL
    win.fill((0, 0, 0))

    # DRAW TORUS
    for point_index, point in enumerate(torus):
        x, y, z = point
        x = round(K1 * x / K2 + z)
        y = round(K1 * y / K2 + z)
        pygame.draw.rect(win, (255, 255, 255), (x + 400, y + 400, PIXEL_SIZE, PIXEL_SIZE))

    # DISPLAY UPDATE
    pygame.display.update()
