from tkinter import Canvas

from constants import GAME_SPACE_SIZE


class Snake:
    slices: list[int]
    positions: list[list[float]]

    def __init__(self, canvas: Canvas, free_positions: list[str]):
        self.canvas = canvas

        self.slices = []
        self.body_size = 3
        self.positions = []

        for y in range(0, self.body_size):
            self.add_new_slice(0, y * GAME_SPACE_SIZE, free_positions)

    def add_new_slice(self, x: float, y: float, free_positions: list[str]):
        free_positions.remove(",".join(map(str, [x, y])))

        self.positions.insert(0, [x, y])

        self.slices.insert(
            0,
            self.canvas.create_rectangle(
                x,
                y,
                x + GAME_SPACE_SIZE,
                y + GAME_SPACE_SIZE,
                fill="#0F0",
            ),
        )

    def remove_tail(self, free_positions: list[str]):
        to_be_free = ",".join(map(str, self.positions[-1]))
        free_positions.append(to_be_free)

        del self.positions[-1]
        self.canvas.delete(self.slices[-1])
        del self.slices[-1]
