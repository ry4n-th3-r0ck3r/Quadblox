import sys
import pygame

from board import Board
from block import Block
from piece import *

#Draw function for the game board.
def draw_game(draw_piece=True):

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw board
    board.draw(screen)

    # Draw current piece
    piece.draw(screen)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (350, 1))

    #Draw Instructions
    y = 100

    for line in instructions:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (400, y))
        y += 30

    # Update display
    pygame.display.flip()

# Initialize pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "QuadBlox"

#Instructions settings
instructions = [
    "HOW TO PLAY",
    "",
    "Left, Right   Move",
    "Down  Fast Fall",
    "Up    Rotate",
    "",
    "Complete a row to clear it.",
    "",
    "Rows clear from bottom to top.",
    "Blocks above cleared rows fall.",
    "",
    "Don't reach the top!"
]

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

#Player score
score = 0

#Creates a random piece to start the game.
piece = spawn_piece()

#Sets text font for the display.
font = pygame.font.Font(None, 36)

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

            # Keep clearing until the board is stable
            while True:

                rows_cleared = board.clear_rows()

                # No more completed rows
                if rows_cleared == 0:
                    break

                # Add score
                score += rows_cleared * 100

                # Show that line disappearing
                draw_game(False)

                pygame.time.delay(300)

                # Drop blocks
                board.drop_blocks()

                # Show that line disappearing
                draw_game(False)

                pygame.time.delay(300)

            # Board is now finished updating
            piece = spawn_piece()

            if board.is_game_over(piece):
                running = False

        last_fall = current_time


    # Draw
    draw_game()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()