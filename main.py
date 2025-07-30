import math
import pygame

# Constants
SCREEN_HEIGHT: int = 800
SCREEN_WIDTH: int = 800
FPS: int = 30
PIXEL_SIZE: int = 10
K1: float = 15
K2: float = 1
R1: float = 5
R2: float = 10
A_SPACING: float = 0.1
B_SPACING: float = 0.1

# Pygame Init
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variables
running: bool = True
angleA: float = 0
angleB: float = 0
animated: bool = True


def generate_torus(r1: float, r2: float) -> list[list[float]]:
    phi: int = 0
    phi_spacing: float = 0.03
    theta_spacing: float = 0.1
    output: list = []
    while phi <= math.pi * 2:
        theta: int = 0
        while theta <= math.pi * 2:
            output.append([
                (r2 + r1 * math.cos(theta)) * math.cos(phi),
                r1 * math.sin(theta),
                -(r2 + r1 * math.cos(theta)) * math.sin(phi),
                theta,
                phi])
            theta += theta_spacing
        phi += phi_spacing
    return output


def rotate_point(point: list[float], angle_a: float, angle_b: float) -> list[float]:
    x, y, z, theta, phi = point
    sinA = math.sin(angle_a)
    cosA = math.cos(angle_a)
    sinB = math.sin(angle_b)
    cosB = math.cos(angle_b)
    sinPhi = math.sin(phi)
    cosPhi = math.cos(phi)
    sinTheta = math.sin(theta)
    cosTheta = math.cos(theta)
    return [x * cosB - sinB * (y * cosA - z * sinA),
            x * sinB + cosB * (y * cosA - z * sinA),
            y * sinA + z * cosA,
            (cosPhi * cosTheta * sinB) - (cosA * cosTheta * sinPhi) - (sinA * sinTheta) + (
            cosB * (cosA * sinTheta - cosTheta * sinA * sinPhi))]


def rotate_points(points, angle_a, angle_b):
    output = []
    for point in points:
        output.append(rotate_point(point, angle_a, angle_b))
    return output


torus: list[list[float]] = generate_torus(R1, R2)
while running:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animated = not animated

    # WIN FILL
    win.fill((0, 0, 0))

    # ROTATE ANGLE A & B
    if animated:
        angleA += A_SPACING
        angleB += B_SPACING
        if angleA > 2 * math.pi:
            angleA = 0
        if angleB > 2 * math.pi:
            angleB = 0

    rotated_torus = rotate_points(torus, angleA, angleB)
    sorted_torus = sorted(rotated_torus, key=lambda item: item[2], reverse=True)
    for point in sorted_torus:
        x, y, z, luminance = point
        x = K1 * x / K2 + z
        y = K1 * y / K2 + z
        luminance = (luminance + 1.5) * (255 / 3)
        pygame.draw.rect(win, (luminance, luminance, luminance), (x + 400, y + 400, PIXEL_SIZE, PIXEL_SIZE))

    # DISPLAY UPDATE
    pygame.display.update()
