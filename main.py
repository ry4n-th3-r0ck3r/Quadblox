import sys
import pygame

from board import Board
from block import Block
from piece import *


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
fall_delay = 500      # milliseconds
last_fall = pygame.time.get_ticks()

# Create the game board
board = Board()

#Creates a random piece to start the game.
piece = spawn_piece()

running = True

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    if current_time - last_fall > fall_delay:
        piece.move_down()
        last_fall = current_time
    # Draw
    screen.fill((0, 0, 0))

    board.draw(screen)

    piece.draw(screen)

    # Update display
    pygame.display.flip()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()