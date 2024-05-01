from tkinter import *

from constants import GAME_SIZE, GAME_SPACE_SIZE, GAME_SPACES, GAME_SPEED
from food import Food
from snake import Snake


class Game(Tk):
    free_positions: list[str]

    def __init__(self):
        Tk.__init__(self)

        self.score = 0
        self.direction = "Down"
        self.free_positions = []
        self.set_free_positions()

        self.bind("<KeyRelease>", self.on_key_release)
        self.setup_screen()

        self.loop()

        self.mainloop()

    def setup_screen(self):
        self.position_changed = False
        self.title("Jogo da cobrinha")
        self.iconbitmap(default="snake.ico")

        self.resizable(False, False)
        self.geometry("{}x{}".format(GAME_SIZE, GAME_SIZE + 70))

        self.score_label = Label(self, text="{}".format(self.score), font=("arial", 40))
        self.score_label.pack()

        self.canvas = Canvas(self, bg="#000", width=GAME_SIZE, height=GAME_SIZE)
        self.canvas.pack()

        self.snake = Snake(self.canvas, self.free_positions)
        self.food = Food(self.canvas, self.free_positions)

    def loop(self):
        snake_head, *_ = self.snake.positions
        snake_head_x, snake_head_y = snake_head

        match self.direction:
            case "Right":
                snake_head_x += GAME_SPACE_SIZE
            case "Left":
                snake_head_x -= GAME_SPACE_SIZE
            case "Down":
                snake_head_y += GAME_SPACE_SIZE
            case "Up":
                snake_head_y -= GAME_SPACE_SIZE

        next_position = self.get_position_index(snake_head_x, snake_head_y)

        if next_position not in self.free_positions:
            return self.game_over()

        self.snake.add_new_slice(snake_head_x, snake_head_y, self.free_positions)

        if not self.food_was_eaten(snake_head_x, snake_head_y):
            self.snake.remove_tail(self.free_positions)

        if len(self.free_positions) == 0:
            return self.win()

        self.position_changed = False
        self.after(GAME_SPEED, self.loop)

    def get_position_index(self, size_x: int, size_y: int):
        return "{},{}".format(int(size_x), int(size_y))

    def set_free_positions(self):
        for x in range(0, GAME_SPACES):
            for y in range(0, GAME_SPACES):
                self.free_positions.append(
                    "{},{}".format(x * GAME_SPACE_SIZE, y * GAME_SPACE_SIZE)
                )

    def game_over(self):
        self.canvas.create_text(
            (GAME_SPACES / 2) * GAME_SPACE_SIZE,
            (GAME_SPACES / 2) * GAME_SPACE_SIZE,
            text="GAME OVER",
            font=("arial", 40),
            fill="#f00",
        )

    def win(self):
        for slice in self.snake.slices:
            self.canvas.delete(slice)
        self.canvas.create_text(
            (GAME_SPACES / 2) * GAME_SPACE_SIZE,
            (GAME_SPACES / 2) * GAME_SPACE_SIZE,
            text="YOU WIN",
            font=("arial", 40),
            fill="#0f0",
        )

    def on_key_release(self, event):
        if event.keysym in ["Right", "Left", "Up", "Down"]:
            self.change_direction(event.keysym)

    def change_direction(self, new_direction):
        x_axis = ["Right", "Left"]
        y_axis = ["Up", "Down"]

        if self.position_changed:
            self.position_changed = False
            return None

        inverse_or_same_direction_x = (
            new_direction in x_axis and self.direction in x_axis
        )
        inverse_or_same_direction_y = (
            new_direction in y_axis and self.direction in y_axis
        )

        if not inverse_or_same_direction_x and not inverse_or_same_direction_y:
            self.direction = new_direction
            self.position_changed = True

    def food_was_eaten(self, head_x, head_y):
        food_x, food_y = self.food.position

        if food_x == head_x and food_y == head_y:
            self.score += 1
            self.food.place(self.free_positions)
            self.score_label.config(text=self.score)
            return True

        return False
