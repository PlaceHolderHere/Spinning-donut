import math
import pygame

# Constants
SCREEN_HEIGHT: int = 800
SCREEN_WIDTH: int = 800
FPS: int = 60
PIXEL_SIZE: int = 10
K1: float = 15
K2: float = 1
R1: float = 5
R2: float = 10
ANGLE_X_SPACING: float = 0.05
ANGLE_Y_SPACING: float = 0.05
ANGLE_Z_SPACING: float = 0.05
COLOR: tuple[int, int, int] = (110, 134, 73)

# Pygame Init
pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Experimental, assuming I choose to use this for performance and to round off x' and y'
# z_buffer: {(int, int): bool} = {}


# Classes
class Point:
    def __init__(self, x, y, z, theta, phi, luminance, color):
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta
        self.phi = phi
        self.luminance = luminance
        self.color = color


# Functions
def generate_torus() -> list[Point]:
    phi: float = 0
    phi_increment: float = 0.03
    theta_increment: float = 0.1
    output: list[Point] = []

    while phi <= math.pi * 2:
        theta: float = 0
        cos_phi: float = math.cos(phi)
        sin_phi: float = math.sin(phi)
        while theta <= math.pi * 2:
            cos_theta: float = math.cos(theta)

            x = (R2 + R1 * cos_theta) * cos_phi
            y = R1 * math.sin(theta)
            z = -((R2 + R1 * cos_theta) * sin_phi)

            output.append(Point(x, y, z, theta, phi, 0, COLOR))
            theta += theta_increment
        phi += phi_increment
    return output


def generate_donut() -> list[Point]:
    phi: float = 0
    phi_increment: float = 0.03
    theta_increment: float = 0.1
    output: list[Point] = []
    max_y = R1 // 1.2

    while phi <= math.pi * 2:
        theta: float = 0
        cos_phi: float = math.cos(phi)
        sin_phi: float = math.sin(phi)
        while theta <= math.pi * 2:
            cos_theta: float = math.cos(theta)

            x = (R2 + R1 * cos_theta) * cos_phi
            y = R1 * math.sin(theta)
            z = -((R2 + R1 * cos_theta) * sin_phi)

            color = (245, 222, 179) if y > -0.5 else (230, 172, 195)
            output.append(Point(x, max(-max_y, min(max_y, y)), z, theta, phi, 0, color))
            theta += theta_increment
        phi += phi_increment
    return output


def rotate_point(point: Point, angle_x: float, angle_y: float, angle_z: float) -> Point:
    # Rotating the Point
    sinx: float = math.sin(angle_x)
    siny: float = math.sin(angle_y)
    sinz: float = math.sin(angle_z)
    cosx: float = math.cos(angle_x)
    cosy: float = math.cos(angle_y)
    cosz: float = math.cos(angle_z)

    x: float = point.x * cosz - (point.y * cosx - point.z * sinx) * sinz
    y: float = cosz * (point.y * cosx - point.z * sinx) + point.x * sinz
    z: float = point.z * cosx + point.y * sinx

    # Updating the luminance
    sin_theta: float = math.sin(point.theta)
    sin_phi: float = math.sin(point.phi)
    cos_theta: float = math.cos(point.theta)
    cos_phi: float = math.cos(point.phi)

    luminance: float = (cos_phi * cos_theta * sinz) - (cosx * cos_theta * sin_phi) - (sinx * sin_theta) + (
                cosz * (cosx * sin_theta - cos_theta * sinx * sin_phi))

    return Point(x, y, z, point.theta, point.phi, luminance, point.color)


def rotate_points(points: list[Point], angle_x: float, angle_y: float, angle_z: float) -> list[Point]:
    output = []
    for point in points:
        output.append(rotate_point(point, angle_x, angle_y, angle_z))
    return output


def render_shape(shape: list[Point], x_offset: int, y_offset: int) -> None:
    sorted_shape = sorted(shape, key=lambda x: x.z, reverse=True)
    for point in sorted_shape:
        x = point.x * K1 / K2 + point.z
        y = point.y * K1 / K2 + point.z
        luminance = point.luminance + 1.5
        r = luminance * (point.color[0] / 3)
        # r = max(40, min(200, luminance * (point.color[0] / 3)))
        g = luminance * (point.color[1] / 3)
        # g = max(40, min(200, luminance * (point.color[1] / 3)))
        b = luminance * (point.color[2] / 3)
        # b = max(40, min(200, luminance * (point.color[2] / 3)))
        pygame.draw.rect(win, (r, g, b), (x + x_offset, y + y_offset, PIXEL_SIZE, PIXEL_SIZE))


# Main
def main():
    # Variables
    running: bool = True
    angle_x: float = 0
    angle_y: float = 0
    angle_z: float = 0
    animated: bool = False

    torus: list[Point] = generate_donut()
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
            angle_x += ANGLE_X_SPACING
            angle_y += ANGLE_Y_SPACING
            angle_z += ANGLE_Z_SPACING

            angle_x = angle_x if angle_x <= 360 else 0
            angle_y = angle_y if angle_y <= 360 else 0
            angle_z = angle_z if angle_z <= 360 else 0

        rotated_torus = rotate_points(torus, angle_x, angle_y, angle_z)
        render_shape(rotated_torus, 400, 400)

        # DISPLAY UPDATE
        pygame.display.update()


if __name__ == "__main__":
    main()
