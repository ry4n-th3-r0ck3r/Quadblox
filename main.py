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

    title = font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (300, 40))

    score_text = instruction_font.render(
        f"Score: {score}   Level: {level}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (300, 90))

    heading = font.render(
        "HIGH SCORES",
        True,
        (255, 255, 255)
    )

    screen.blit(heading, (280, 140))

    y = 190

    for position, (name, saved_score) in enumerate(high_scores, start=1):

        line = instruction_font.render(
            f"{position:2}. {name:3}   {saved_score}",
            True,
            (255, 255, 255)
        )

        screen.blit(line, (280, y))

        y += 28

    exit_text = instruction_font.render(
        "Press SPACE to exit",
        True,
        (255, 255, 255)
    )

    screen.blit(exit_text, (300, 520))

    pygame.display.flip()

#Reads in high scores
def load_high_scores():

    scores = []

    try:
        with open("highscores.txt", "r") as file:

            for line in file:

                name, score = line.strip().split(",")

                scores.append((name, int(score)))

    except FileNotFoundError:
        pass

    return scores

#Saves high scores
def save_high_scores():

    with open("highscores.txt", "w") as file:

        for name, saved_score in high_scores:

            file.write(f"{name},{saved_score}\n")

#Checks if score makes the high score list
def is_high_score(score):

    if len(high_scores) < 10:
        return True

    return score > high_scores[-1][1]
# Initialize pygame
pygame.init()

#Draws high score board
def draw_name_entry():

    screen.fill((0, 0, 0))

    title = font.render(
        "NEW HIGH SCORE!",
        True,
        (255, 255, 255)
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    name_text = font.render(
        f"Name: {player_name}",
        True,
        (255, 255, 255)
    )

    instruction = instruction_font.render(
        "Enter up to 3 letters - ENTER to save",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (250, 180))
    screen.blit(score_text, (300, 240))
    screen.blit(name_text, (300, 300))
    screen.blit(instruction, (220, 360))

    pygame.display.flip()

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

#For high scores
high_scores = load_high_scores()
name_entry = False
player_name = ""

#Game logic
running = True
game_over = False
paused = False


while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # High Score entry
        elif name_entry:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    if len(player_name) > 0:
                        high_scores.append((player_name, score))

                        high_scores.sort(
                            key=lambda entry: entry[1],
                            reverse=True
                        )

                        high_scores = high_scores[:10]

                        save_high_scores()

                        name_entry = False

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                elif len(player_name) < 3:

                    letter = event.unicode.upper()

                    if letter.isalpha():
                        player_name += letter
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

            # Count lines cleared by this piece
            lines_cleared = 0

            # Keep clearing until the board is stable
            while True:

                rows_cleared = board.clear_rows()

                # Keep track of every row that actually cleared
                lines_cleared += rows_cleared
                modifier = lines_cleared

                # No more completed rows
                if rows_cleared == 0:
                    break

                # Add score/modify level
                score += lines_cleared * 100 * modifier * level
                # Adjust difficulty
                if score >= 30000:
                    level = 5
                    NORMAL_FALL_DELAY = 100

                elif score >= 20000:
                    level = 4
                    NORMAL_FALL_DELAY = 200

                elif score >= 10000:
                    level = 3
                    NORMAL_FALL_DELAY = 300

                elif score >= 5000:
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
                # Stop the music during game over.
                pygame.mixer.music.stop()

                if is_high_score(score):
                    name_entry = True


        last_fall = current_time


    # Draw
    if name_entry:
        draw_name_entry()

    elif game_over:
        draw_game_over()

    else:
        draw_game()

    # Maintain FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()