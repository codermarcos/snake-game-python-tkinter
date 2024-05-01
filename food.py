from tkinter import Canvas

from numpy import random

from constants import GAME_SPACE_SIZE, GAME_SPACES


class Food:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.place()

    def generate_position(self) -> float:
        return random.randint(0, GAME_SPACES - 1) * GAME_SPACE_SIZE

    def place(self):
        x = self.generate_position()
        y = self.generate_position()
        self.position = [x, y]
        self.canvas.create_oval(
            x,
            y,
            x + GAME_SPACE_SIZE,
            y + GAME_SPACE_SIZE,
            fill="#ff0",
        )
