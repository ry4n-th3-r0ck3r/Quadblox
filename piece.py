from block import Block
from settings import *
import random


class Piece:

    def __init__(self, shape):

        self.x = SPAWN_X
        self.y = SPAWN_Y

        self.name = shape
        self.blocks = []

        self.rotation = 0

        if shape == "square":
            self.max_rotation = 0
            self.square()

        elif shape == "line":
            self.max_rotation = 1
            self.line()

        elif shape == "l":
            self.max_rotation = 3
            self.l_piece()

        elif shape == "j":
            self.max_rotation = 3
            self.j_piece()

        elif shape == "t":
            self.max_rotation = 3
            self.t_piece()

        elif shape == "s":
            self.max_rotation = 1
            self.s_piece()

        elif shape == "z":
            self.max_rotation = 1
            self.z_piece()

#Draws the new shape with the requested change.

    def rebuild(self):

        if self.name == "square":
            self.square()

        elif self.name == "line":
            self.line()

        elif self.name == "l":
            self.l_piece()

        elif self.name == "j":
            self.j_piece()

        elif self.name == "t":
            self.t_piece()

        elif self.name == "s":
            self.s_piece()

        elif self.name == "z":
            self.z_piece()

    def get_rotated_blocks(self):

        old_rotation = self.rotation
        old_blocks = self.blocks

        self.rotation += 1

        if self.rotation > self.max_rotation:
            self.rotation = 0

        self.rebuild()

        rotated_blocks = self.blocks

        # Restore the current piece
        self.rotation = old_rotation
        self.blocks = old_blocks

        return rotated_blocks

    def try_rotate(self, board):

        if self.max_rotation == 0:
            return

        rotated_blocks = self.get_rotated_blocks()

        # Try rotation normally first
        if self.rotation_is_valid(board, rotated_blocks):
            self.apply_rotation()
            return

        # Try pushing one square right
        if self.rotation_is_valid(board, rotated_blocks, offset_x=1):
            self.x += 1
            self.apply_rotation()
            return

        # Try pushing one square left
        if self.rotation_is_valid(board, rotated_blocks, offset_x=-1):
            self.x -= 1
            self.apply_rotation()

    def rotation_is_valid(self, board, rotated_blocks, offset_x=0):

        for block in rotated_blocks:

            test_x = block.x + offset_x
            test_y = block.y

            # Prevent any out-of-range board access
            if test_x < 0 or test_x >= board.width:
                return False

            if test_y < 0 or test_y >= board.height:
                return False

            if board.is_occupied(test_x, test_y):
                return False

        return True

    def apply_rotation(self):

        self.rotation += 1

        if self.rotation > self.max_rotation:
            self.rotation = 0

        self.rebuild()

#Lets the piece move downward. Simply increases y value to create downward movement.
    def move_down(self):

        for block in self.blocks:
            block.y += 1

#Tests if piece CAN move downard.
    def can_move_down(self, board):

        self.y += 1

        for block in self.blocks:
            next_y = block.y + 1

            if board.is_occupied(block.x, next_y):
                return False

        return True

#Moves piece to the left.
    def move_left(self):

        self.x -= 1

        for block in self.blocks:
            block.x -= 1

#Checks to make sure piece CAN move to the left
    def can_move_left(self, board):

        for block in self.blocks:

            next_x = block.x - 1

            if board.is_occupied(next_x, block.y):
                return False

        return True

#Moves piece to the right.
    def move_right(self):

        self.x += 1

        for block in self.blocks:
            block.x += 1
#Checks to make sure piece CAN move to the right
    def can_move_right(self, board):

        for block in self.blocks:

            next_x = block.x + 1

            if board.is_occupied(next_x, block.y):
                return False

        return True

#Allows piece rotation.
    def rotate(self):

        self.rotation += 1

        if self.rotation > self.max_rotation:
            self.rotation = 0

        self.rebuild()


### Shape definitions
    def square(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x, y, RED),
            Block(x + 1, y, RED),
            Block(x, y + 1, RED),
            Block(x + 1, y + 1, RED)
        ]


    def line(self):

    # This lets you specify starting location of the piece.
        x = self.x
        y = self.y

        if self.rotation == 0:
            self.blocks = [
                Block(x, y, BLUE),
                Block(x + 1, y, BLUE),
                Block(x + 2, y, BLUE),
                Block(x + 3, y, BLUE)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x, y, BLUE),
                Block(x, y + 1, BLUE),
                Block(x, y + 2, BLUE),
                Block(x, y + 3, BLUE)
            ]

    def l_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:

            self.blocks = [
                Block(x, y, GREEN),
                Block(x, y + 1, GREEN),
                Block(x, y + 2, GREEN),
                Block(x + 1, y + 2, GREEN)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x, y, GREEN),
                Block(x + 1, y, GREEN),
                Block(x + 2, y, GREEN),
                Block(x, y + 1, GREEN)
            ]

        elif self.rotation == 2:

            self.blocks = [
                Block(x, y, GREEN),
                Block(x + 1, y, GREEN),
                Block(x + 1, y + 1, GREEN),
                Block(x + 1, y + 2, GREEN)
            ]

        elif self.rotation == 3:

            self.blocks = [
                Block(x + 2, y, GREEN),
                Block(x, y + 1, GREEN),
                Block(x + 1, y + 1, GREEN),
                Block(x + 2, y + 1, GREEN)
            ]

    def j_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:
            self.blocks = [
                Block(x + 1, y, INDIGO),
                Block(x + 1, y + 1, INDIGO),
                Block(x + 1, y + 2, INDIGO),
                Block(x, y + 2, INDIGO)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x, y, INDIGO),
                Block(x, y + 1, INDIGO),
                Block(x + 1, y + 1, INDIGO),
                Block(x + 2, y + 1, INDIGO)
            ]

        elif self.rotation == 2:

            self.blocks = [
                Block(x, y, INDIGO),
                Block(x + 1, y, INDIGO),
                Block(x, y + 1, INDIGO),
                Block(x, y + 2, INDIGO)
            ]

        elif self.rotation == 3:

            self.blocks = [
                Block(x, y, INDIGO),
                Block(x + 1, y, INDIGO),
                Block(x + 2, y, INDIGO),
                Block(x + 2, y + 1, INDIGO)
            ]

    def t_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:

            self.blocks = [
                Block(x, y, YELLOW),
                Block(x + 1, y, YELLOW),
                Block(x + 2, y, YELLOW),
                Block(x + 1, y + 1, YELLOW)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x, y, YELLOW),
                Block(x, y + 1, YELLOW),
                Block(x, y + 2, YELLOW),
                Block(x + 1, y + 1, YELLOW)
            ]

        elif self.rotation == 2:

            self.blocks = [
                Block(x + 1, y, YELLOW),
                Block(x, y + 1, YELLOW),
                Block(x + 1, y + 1, YELLOW),
                Block(x + 2, y + 1, YELLOW)
            ]

        elif self.rotation == 3:

            self.blocks = [
                Block(x + 1, y, YELLOW),
                Block(x, y + 1, YELLOW),
                Block(x + 1, y + 1, YELLOW),
                Block(x + 1, y + 2, YELLOW)
            ]

    def s_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:

            self.blocks = [
                Block(x + 1, y, ORANGE),
                Block(x + 2, y, ORANGE),
                Block(x, y + 1, ORANGE),
                Block(x + 1, y + 1, ORANGE)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x, y, ORANGE),
                Block(x, y + 1, ORANGE),
                Block(x + 1, y + 1, ORANGE),
                Block(x + 1, y + 2, ORANGE)
            ]

    def z_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:

            self.blocks = [
                Block(x, y, VIOLET),
                Block(x + 1, y, VIOLET),
                Block(x + 1, y + 1, VIOLET),
                Block(x + 2, y + 1, VIOLET)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x + 1, y, VIOLET),
                Block(x, y + 1, VIOLET),
                Block(x + 1, y + 1, VIOLET),
                Block(x, y + 2, VIOLET)
            ]

#This is a piece that needs testing before full implementation.
    def y_piece(self):

        x = self.x
        y = self.y

        if self.rotation == 0:

            self.blocks = [
                Block(x, y, CYAN),
                Block(x + 2, y, CYAN),
                Block(x + 1, y + 1, CYAN),
                Block(x + 1, y + 2, CYAN)
            ]

        elif self.rotation == 1:

            self.blocks = [
                Block(x + 2, y, CYAN),
                Block(x, y + 1, CYAN),
                Block(x + 1, y + 1, CYAN),
                Block(x + 2, y + 2, CYAN)
            ]

        elif self.rotation == 2:

            self.blocks = [
                Block(x + 1, y, CYAN),
                Block(x + 1, y + 1, CYAN),
                Block(x, y + 2, CYAN),
                Block(x + 2, y + 2, CYAN)
            ]

        elif self.rotation == 3:

            self.blocks = [
                Block(x, y, CYAN),
                Block(x + 1, y + 1, CYAN),
                Block(x + 2, y + 1, CYAN),
                Block(x, y + 2, CYAN)
            ]

    def draw(self, screen):

        for block in self.blocks:
            block.draw(screen)


def spawn_piece():

    shapes = [
        "square",
        "line",
        "l",
        "j",
        "t",
        "s",
        "z"
    ]

    shape = random.choice(shapes)

    return Piece(shape)
