from tkinter import *

from constants import GAME_SIZE
from food import Food


class Game(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.score = 0

        self.setup_screen()

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

        self.food = Food(self.canvas)
