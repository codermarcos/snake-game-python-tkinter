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
        self.title("Jogo da cobrinha")
        self.iconbitmap(default="snake.ico")

        self.resizable(False, False)
        self.geometry("{}x{}".format(GAME_SIZE, GAME_SIZE + 70))

        self.score_label = Label(self, text="{}".format(self.score), font=("arial", 40))
        self.score_label.pack()

        self.canvas = Canvas(self, bg="#000", width=GAME_SIZE, height=GAME_SIZE)
        self.canvas.pack()

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas, self.free_positions)

    def loop(self):
        food_x, food_y = self.food.position

        snake_head, *_, snake_tail = self.snake.positions
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

        self.snake.add_new_slice(snake_head_x, snake_head_y)

        next_position = self.get_position_index(snake_head_x, snake_head_y)
        if next_position in self.free_positions:
            self.free_positions.remove(next_position)
        else:
            return self.game_over()

        if food_x == snake_head_x and food_y == snake_head_y:
            self.food_was_eaten()
        else:
            self.snake.remove_tail()
            to_be_free = ",".join(map(str, snake_tail))
            if to_be_free not in self.free_positions:
                self.free_positions.append(to_be_free)

        print(self.free_positions)

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

    def on_key_release(self, event):
        if event.keysym in ["Right", "Left", "Up", "Down"]:
            self.direction = event.keysym

    def food_was_eaten(self):
        self.score += 1
        self.food.place(self.free_positions)
        self.score_label.config(text=self.score)
