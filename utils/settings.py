import pygame
pygame.init()
pygame.font.init()

WHITE = (225, 225, 225)
BLACK = (25, 25, 25)
RED = (225, 0, 0)
BLUE = (0, 225, 0)
GREEN = (0, 0, 225)

FPS = 540

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
