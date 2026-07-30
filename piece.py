from block import Block
from settings import *


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
            Block(x + 1, y, CYAN),
            Block(x + 1, y + 1, CYAN),
            Block(x + 1, y + 2, CYAN),
            Block(x, y + 2, CYAN)
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
            Block(x, y, ORANGE),
            Block(x + 1, y, ORANGE),
            Block(x + 1, y + 1, ORANGE),
            Block(x + 2, y + 1, ORANGE)
        ]


    def draw(self, screen):

        for block in self.blocks:
            block.draw(screen)