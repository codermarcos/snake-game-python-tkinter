from tkinter import Canvas

from numpy import random

from constants import GAME_SPACE_SIZE


class Food:

    element: int | None

    def __init__(self, canvas: Canvas, free_positions: list[str]):
        self.element = None
        self.canvas = canvas
        self.place(free_positions)

    def place(self, free_positions: list[str]):
        sorted_position = free_positions[random.randint(0, len(free_positions))]
        x, y = map(int, sorted_position.split(","))

        self.position = [x, y]

        if self.element is not None:
            self.canvas.delete(self.element)

        self.element = self.canvas.create_oval(
            x,
            y,
            x + GAME_SPACE_SIZE,
            y + GAME_SPACE_SIZE,
            fill="#ff0",
        )
