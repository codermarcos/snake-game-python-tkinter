from tkinter import *

from constants import GAME_SIZE, GAME_SPACE_SIZE, GAME_SPEED
from food import Food
from snake import Snake


class Game(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.score = 0
        self.direction = "Down"

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
        self.food = Food(self.canvas)

    def loop(self):
        food_x, food_y = self.food.position

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

        self.snake.add_new_slice(snake_head_x, snake_head_y)

        if food_x == snake_head_x and food_y == snake_head_y:
            self.food_was_eaten()
        else:
            self.snake.remove_tail()

        self.after(GAME_SPEED, self.loop)

    def on_key_release(self, event):
        if event.keysym in ["Right", "Left", "Up", "Down"]:
            self.direction = event.keysym

    def food_was_eaten(self):
        self.score += 1
        self.food.place()
        self.score_label.config(text=self.score)
