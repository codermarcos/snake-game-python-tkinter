from tkinter import Canvas

from constants import GAME_SPACE_SIZE


class Snake:
    slices: list[int]
    positions: list[list[int]]

    def __init__(self, canvas: Canvas):
        self.canvas_tag = "Food"
        self.canvas = canvas

        self.slices = []
        self.body_size = 3
        self.positions = []

        for _ in range(0, self.body_size):
            self.add_new_slice(0, 0)

    def add_new_slice(self, x, y):
        self.positions.insert(0, [x, y])

        self.slices.insert(
            0,
            self.canvas.create_rectangle(
                x,
                y,
                x + GAME_SPACE_SIZE,
                y + GAME_SPACE_SIZE,
                fill="#0F0",
                tag=self.canvas_tag,
            ),
        )

    def remove_tail(self):
        del self.positions[-1]
        self.canvas.delete(self.canvas_tag)
        del self.slices[-1]
