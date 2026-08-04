import pygame
from settings import *

class Board:

    def __init__(self):

        self.width = VISIBLE_WIDTH
        self.height = VISIBLE_HEIGHT

        # Create an empty grid
        self.grid = []

        for row in range(self.height):
            self.grid.append([])

            for column in range(self.width):
                self.grid[row].append(None)

        # Build the border
        self.create_border()

    def create_border(self):

        for row in range(self.height):

            for column in range(self.width):

                if (
                    row == 0
                    or row == self.height - 1
                    or column == 0
                    or column == self.width - 1
                ):
                    self.grid[row][column] = "B"

    def draw(self, screen):

        for row in range(self.height):

            for column in range(self.width):

                x = column * BLOCK_SIZE
                y = row * BLOCK_SIZE

                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

                if self.grid[row][column] == "B":
                    pygame.draw.rect(screen, BORDER_COLOR, rect)


                elif self.grid[row][column] is not None:
                    pygame.draw.rect(screen, self.grid[row][column], rect)

                else:
                    pygame.draw.rect(screen, BOARD_COLOR, rect)

                pygame.draw.rect(screen, GRID_COLOR, rect, 1)

    #Checks if grid cell is occupied
    def is_occupied(self, x, y):
        return self.grid[y][x] is not None

    #Locks piece into the board.
    def lock_piece(self, piece):

        for block in piece.blocks:
            self.grid[block.y][block.x] = block.color