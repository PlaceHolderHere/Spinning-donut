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
COLOR: tuple[int, int, int] = (148, 87, 235)

# Pygame Init
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variables
running: bool = True
angleA: float = 0
angleB: float = 0
animated: bool = False


def generate_torus(r1: float, r2: float, x_offset: int, y_offset: int, z_offset: int, color: tuple[int, int, int]) -> list[list[float]]:
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
                -(r2 + r1 * math.cos(theta)) * math.sin(phi) + z_offset,
                theta, phi, color, x_offset, y_offset])
            theta += theta_spacing
        phi += phi_spacing
    return output


def generate_rect(sizeX: int, sizeY: int, sizeZ: int, spacing: float, x_offset: int, y_offset: int, z_offset: int, color: tuple[int, int, int]) -> list[list[float]]:
    output: list = []
    for x in range(sizeX):
        for y in range(sizeY):
            for z in range(sizeZ):
                output.append([x * spacing, y * spacing, z * spacing + z_offset, 0, 0, color, x_offset, y_offset])

    return output


def rotate_point(point: list[float], angle_a: float, angle_b: float) -> list[float]:
    x, y, z, theta, phi, color, x_offset, y_offset = point
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
            cosB * (cosA * sinTheta - cosTheta * sinA * sinPhi)),
            color, x_offset, y_offset]


def rotate_points(points: list[list[float]], angle_a: [float], angle_b: [float]) -> list[list[float]]:
    output = []
    for point in points:
        output.append(rotate_point(point, angle_a, angle_b))
    return output


def render_shape(shape: list[list[float]]) -> None:
    sorted_shape = sorted(shape, key=lambda item: item[2], reverse=True)
    for point in sorted_shape:
        x, y, z, luminance, color, x_offset, y_offset = point
        x = K1 * x / K2 + z
        y = K1 * y / K2 + z
        luminance += 1.5
        r = luminance * (color[0] / 3)
        g = luminance * (color[1] / 3)
        b = luminance * (color[2] / 3)
        pygame.draw.rect(win, (r, g, b), (x + x_offset, y + y_offset, PIXEL_SIZE, PIXEL_SIZE))


def render_frame(*args):
    frame = []
    for shape in args:
        frame += shape
    sorted_frame = sorted(frame, key=lambda item: item[2], reverse=True)
    for point in sorted_frame:
        x, y, z, luminance, color, x_offset, y_offset = point
        x = K1 * x / K2 + z
        y = K1 * y / K2 + z
        luminance += 1.5
        r = luminance * (color[0] / 3)
        g = luminance * (color[1] / 3)
        b = luminance * (color[2] / 3)
        pygame.draw.rect(win, (r, g, b), (x + x_offset, y + y_offset, PIXEL_SIZE, PIXEL_SIZE))


rect: list[list[float]] = generate_rect(10, 5, 5, 0.5, 300, 300, -20, (255, 255, 255))
torus: list[list[float]] = generate_torus(R1, R2, 400, 400, 5, COLOR)
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
    rotated_rect = rotate_points(rect, angleA, angleB)
    render_frame(rotated_torus, rotated_rect)

    # DISPLAY UPDATE
    pygame.display.update()
