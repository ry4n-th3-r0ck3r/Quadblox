import sys
import pygame

#Clarifies mixer is being used. Using it for background music.
pygame.init()
pygame.mixer.init()

#Sets music to play and loop for the background song.
pygame.mixer.music.load("Assets/Music/Dance of the Sugar Plum Fairy.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

from board import Board
from block import Block
from piece import *

#Draw the preview piece
def draw_next_piece():

    preview_x = 500
    preview_y = 110

    for block in next_piece.blocks:

        relative_x = block.x - next_piece.x
        relative_y = block.y - next_piece.y

        x = preview_x + relative_x * BLOCK_SIZE
        y = preview_y + relative_y * BLOCK_SIZE

        rect = pygame.Rect(
            x,
            y,
            BLOCK_SIZE,
            BLOCK_SIZE
        )

        pygame.draw.rect(screen, block.color, rect)
        pygame.draw.rect(screen, GRID_COLOR, rect, 1)

#Draw function for the game board.
def draw_game(draw_piece=True):

    screen.fill((0, 0, 0))

    board.draw(screen)

    if draw_piece:
        piece.draw(screen)

    # Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (350, 1))

    # Draw level
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (550, 1))

    # Next piece
    next_text = font.render("Next:", True, (255, 255, 255))
    screen.blit(next_text, (400, 50))

    draw_next_piece()

    # Instructions
    y = 300

    for line in instructions:
        text = instruction_font.render(line, True, (255, 255, 255))
        screen.blit(text, (400, y))
        y += 25

    # Pause overlay
    if paused:
        pause_text = font.render("PAUSED", True, (255, 255, 255))
        screen.blit(pause_text, (100, 250))
        continue_text = instruction_font.render(
            "Press SPACE to continue",
            True,
            (255, 255, 255)
        )

        screen.blit(continue_text, (65, 290))

    # Update screen ONCE after everything is drawn
    pygame.display.flip()

#Game Over Screen
def draw_game_over():

    screen.fill((0, 0, 0))

    game_over_text = font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    score_text = font.render(
        f"Final Score: {score}",
        True,
        (255, 255, 255)
    )

    level_text = font.render(
        f"Level: {level}",
        True,
        (255, 255, 255)
    )

    exit_text = instruction_font.render(
        "Press SPACE to exit",
        True,
        (255, 255, 255)
    )

    screen.blit(game_over_text, (300, 180))
    screen.blit(score_text, (300, 240))
    screen.blit(level_text, (300, 290))
    screen.blit(exit_text, (300, 360))

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
    "Left/Right - Move",
    "Down - Fast Fall",
    "Up - Rotate",
    "Space Bar - Pause.",
    "",
    "Complete a row to clear it.",
    "",
    "Rows clear from bottom to top.",
    "Blocks above cleared rows collapse.",
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

#Base level and score
level = 1
score = 0

last_fall = pygame.time.get_ticks()

# Create the game board
board = Board()

# Create a current piece and a preview piece
piece = spawn_piece()
next_piece = spawn_piece()

#Sets text font for the display.
font = pygame.font.Font(None, 36)
#Smaller font for game instructions
instruction_font = pygame.font.Font(None, 24)

running = True
game_over = False
paused = False

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Game over controls
        elif game_over:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                paused = not paused

                if paused:
                    pygame.mixer.music.pause()

                else:
                    pygame.mixer.music.unpause()
                    last_fall = pygame.time.get_ticks()

            elif not paused:
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

    if not game_over and not paused and current_time - last_fall > fall_delay:
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

                # Add score/modify level
                score += rows_cleared * (level * 100)
                # Adjust difficulty
                if score >= 20000:
                    level = 5
                    NORMAL_FALL_DELAY = 100

                elif score >= 12000:
                    level = 4
                    NORMAL_FALL_DELAY = 200

                elif score >= 6000:
                    level = 3
                    NORMAL_FALL_DELAY = 300

                elif score >= 3000:
                    level = 2
                    NORMAL_FALL_DELAY = 400

                else:
                    level = 1
                    NORMAL_FALL_DELAY = 500

                # Show that line disappearing
                draw_game(False)

                pygame.time.delay(300)

                # Drop blocks
                board.drop_blocks()

                # Show that line disappearing
                draw_game(False)

                pygame.time.delay(300)

            # Board is now finished updating
            piece = next_piece
            next_piece = spawn_piece()

            if board.is_game_over(piece):
                game_over = True


        last_fall = current_time


    # Draw
    if game_over:
        pygame.mixer.music.stop()
        draw_game_over()
    else:
        draw_game()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()