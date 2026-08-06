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

NORMAL_FALL_DELAY = 500
FAST_FALL_DELAY = 50
fall_delay = NORMAL_FALL_DELAY     # milliseconds

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

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                if piece.can_move_left(board):
                    piece.move_left()

            elif event.key == pygame.K_RIGHT:

                if piece.can_move_right(board):
                    piece.move_right()

            elif event.key == pygame.K_UP:
                    piece.try_rotate(board)

            elif event.key == pygame.K_DOWN:
                    fall_delay = FAST_FALL_DELAY

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN:
                fall_delay = NORMAL_FALL_DELAY

    current_time = pygame.time.get_ticks()

    if current_time - last_fall > fall_delay:
        if piece.can_move_down(board):
            piece.move_down()
        else:
            board.lock_piece(piece)
            piece = spawn_piece()

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