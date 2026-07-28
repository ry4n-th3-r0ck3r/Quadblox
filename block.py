import pygame
from settings import BLOCK_SIZE


class Block:

    def __init__(self, x, y, color):

        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):

        pixel_x = self.x * BLOCK_SIZE
        pixel_y = self.y * BLOCK_SIZE

        rect = pygame.Rect(pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE)

        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (50, 50, 50), rect, 1)