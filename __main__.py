from tkinter import *


class Game(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.score = 0

        self.setup_screen()

        self.mainloop()

    def setup_screen(self):
        self.title("Jogo da cobrinha")

        self.resizable(False, False)
        self.geometry("{}x{}".format(500, 500 + 70))

        self.score_label = Label(self, text="{}".format(self.score), font=("arial", 40))
        self.score_label.pack()

        self.canvas = Canvas(self, bg="#000", width=500, height=500)
        self.canvas.pack()


Game()
