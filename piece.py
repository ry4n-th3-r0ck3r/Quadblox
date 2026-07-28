from block import Block


class Piece:

    def __init__(self, shape):

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

        RED = (220, 60, 60)

#This lets you specify starting location of the piece.
        x = 4
        y = 1

        self.blocks = [
            Block(x, y, RED),
            Block(x + 1, y, RED),
            Block(x, y + 1, RED),
            Block(x + 1, y + 1, RED)
        ]


    def line(self):
        pass


    def l_piece(self):
        pass


    def j_piece(self):
        pass


    def t_piece(self):
        pass


    def s_piece(self):
        pass


    def z_piece(self):
        pass


    def draw(self, screen):

        for block in self.blocks:
            block.draw(screen)