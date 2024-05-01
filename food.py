from tkinter import Canvas

from constants import GAME_SPACE_SIZE
from numpy import random


class Food:

    element: int | None

    def __init__(self, canvas: Canvas, free_positions: list[str]):
        self.element = None
        self.canvas = canvas
        self.place(free_positions)

    def place(self, free_positions: list[str]):
        number_of_free_positions = len(free_positions)

        if self.element is not None:
            self.canvas.delete(self.element)

        if number_of_free_positions == 0:
            return None

        sorted_position = free_positions[random.randint(0, number_of_free_positions)]
        x, y = map(int, sorted_position.split(","))

        self.position = [x, y]

        self.element = self.canvas.create_oval(
            x,
            y,
            x + GAME_SPACE_SIZE,
            y + GAME_SPACE_SIZE,
            fill="#ff0",
        )
