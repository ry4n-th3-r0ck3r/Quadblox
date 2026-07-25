import sys
import pygame

from board import Board

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "QuadBlox"

# Colors
BACKGROUND_COLOR = (30, 30, 30)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Control frame rate
clock = pygame.time.Clock()
FPS = 60

# Create the game board
board = Board()

running = True

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    screen.fill((0, 0, 0))

    board.draw(screen)

    pygame.display.flip()

    # Update display
    pygame.display.flip()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()