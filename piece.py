from block import Block
from settings import *
import random


class Piece:

    def __init__(self, shape):

        self.x = SPAWN_X
        self.y = SPAWN_Y

        self.name = shape
        self.blocks = []

        if shape == "square":
            self.square()

        elif shape == "line":
            self.line()

        elif shape == "l":
            self.l_piece()

        elif shape == "j":
            self.j_piece()

        elif shape == "t":
            self.t_piece()

        elif shape == "s":
            self.s_piece()

        elif shape == "z":
            self.z_piece()

#Lets the piece move downward. Simply increases y value to create downward movement.
    def move_down(self):

        for block in self.blocks:
            block.y += 1

#Tests if piece CAN move downard.
    def can_move_down(self, board):

        for block in self.blocks:
            next_y = block.y + 1

            if board.is_occupied(block.x, next_y):
                return False

        return True

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

        self.blocks = [
            Block(x, y, BLUE),
            Block(x + 1, y, BLUE),
            Block(x + 2, y, BLUE),
            Block(x + 3, y, BLUE)
        ]


    def l_piece(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x, y, GREEN),
            Block(x, y + 1, GREEN),
            Block(x, y + 2, GREEN),
            Block(x + 1, y + 2, GREEN)
        ]


    def j_piece(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x + 1, y, INDIGO),
            Block(x + 1, y + 1, INDIGO),
            Block(x + 1, y + 2, INDIGO),
            Block(x, y + 2, INDIGO)
        ]


    def t_piece(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x, y, YELLOW),
            Block(x + 1, y, YELLOW),
            Block(x + 2, y, YELLOW),
            Block(x + 1, y + 1, YELLOW)
        ]


    def s_piece(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x + 1, y, ORANGE),
            Block(x + 2, y, ORANGE),
            Block(x, y + 1, ORANGE),
            Block(x + 1, y + 1, ORANGE)
        ]


    def z_piece(self):
        x = self.x
        y = self.y

        self.blocks = [
            Block(x, y, VIOLET),
            Block(x + 1, y, VIOLET),
            Block(x + 1, y + 1, VIOLET),
            Block(x + 2, y + 1, VIOLET)
        ]

#This is a piece that needs testing before full implementation.
    def y_piece(self):
        self.blocks = [
            Block(self.x, self.y, CYAN),
            Block(self.x + 2, self.y, CYAN),
            Block(self.x + 1, self.y + 1, CYAN),
            Block(self.x + 1, self.y + 2, CYAN)
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
