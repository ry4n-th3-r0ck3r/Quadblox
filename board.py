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

    #Checks to see if rows are full.
    def find_full_rows(self):

        full_rows = []

        # Skip top and bottom border
        for y in range(1, self.height - 1):

            row_full = True

            # Skip left and right border
            for x in range(1, self.width - 1):

                if self.grid[y][x] is None:
                    row_full = False
                    break

            if row_full:
                full_rows.append(y)

        return full_rows

    #Clears full rows
    def clear_rows(self):

        full_rows = self.find_full_rows()

        if not full_rows:
            return 0

        # Clear one row at a time
        y = full_rows[-1]

        for x in range(1, self.width - 1):
            self.grid[y][x] = None

        return 1

#Makes blocks fall if nothing below them.
    def drop_blocks(self):

        blocks_moved = True

        while blocks_moved:

            blocks_moved = False

            # Start at the bottom and work upward
            for y in range(self.height - 2, 0, -1):

                # Only check playable columns
                for x in range(1, self.width - 1):

                    # Is there a block here?
                    if self.grid[y][x] is not None:

                        # Is the space directly below empty?
                        if self.grid[y + 1][x] is None:
                            # Move the block down
                            self.grid[y + 1][x] = self.grid[y][x]
                            self.grid[y][x] = None

                            blocks_moved = True

    #Checks for "game over"
    def is_game_over(self, piece):

        for block in piece.blocks:

            if self.is_occupied(block.x, block.y):
                return True

        return False
