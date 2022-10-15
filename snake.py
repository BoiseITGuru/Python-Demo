# Snake game clone
# Author: Carlin Hornbostel
# Created: 7/6/2021
# Completed:
import tkinter
import random
import time

moving_speed = 7
boardwidth = 300
boardheight = 300

# main window


class main(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.initialize_game()
        self.make_canvas()
        self.make_scoreboard()
        self.make_snake()
        self.bind("<Key>", self.keybinding)

    def make_snake(self):
        self.snake_head = self.main_Canvas.create_rectangle(21, 21, 31, 31, fill='Green', dash=(1, 1))
        return

    def initialize_game(self):
        self.game_on = 1
        self.x = moving_speed
        self.y = 0
        self.length = 3
        self.current_score = 0
        self.apple = None
        self.endsnake = [(0, 0)]

    def make_canvas(self):
        self.main_Canvas = tkinter.Canvas(self, width=300, height=300, bg='black')
        self.main_Canvas.pack()

    def make_scoreboard(self):
        score = self.current_score
        self.SB = tkinter.Label(self, text="Score: {}".format(score))
        self.SB.pack(anchor='nw')

    def update_scoreboard(self):
        self.current_score = self.current_score + 1
        score = self.current_score
        self.SB.config(text="Score: {}".format(score))

    def keybinding(self, event):
        key = event.keysym
        if key == 'Left':
            self.x = -moving_speed
            self.y = 0
        elif key == 'Right':
            self.x = moving_speed
            self.y = 0
        elif key == 'Up':
            self.x = 0
            self.y = -moving_speed
        elif key == 'Down':
            self.x = 0
            self.y = moving_speed

    def move_snake(self):
        self.main_Canvas.move(self.snake_head, self.x, self.y)
        xinit, yinit, xfin, yfin = self.main_Canvas.coords(self.snake_head)
        # check to make sure snake is within border
        if xinit < 0:
            self.x = 0
            self.y = 0
            self.endgame()
        elif yinit < 0:
            self.x = 0
            self.y = 0
            self.endgame()
        elif xinit > boardwidth:
            self.x = 0
            self.y = 0
            self.endgame()
        elif yinit > boardheight:
            self.x = 0
            self.y = 0
            self.endgame()

    def endgame(self):
        self.main_Canvas.create_text(boardwidth / 2, boardheight / 2,
                                     text='Game over. Your score is: {}'.format(self.current_score), fill="white")

    def movement(self):
        self.move_snake()
        self.updating_snake()
        self.create_apples()

    def create_apples(self):
        if self.apple == None:
            xinit = random.randint(15, boardwidth - 15)
            yinit = random.randint(15, boardheight - 15)
            self.apple = self.main_Canvas.create_oval(xinit, yinit, xinit + 10, yinit + 10, fill='red', tag='apple')
        if self.apple:
            xinit, yinit, xfin, yfin = self.main_Canvas.coords(self.apple)
            if len(self.main_Canvas.find_overlapping(xinit, yinit, xfin, yfin)) != 1:
                self.main_Canvas.delete('apple')
                self.apple = None
                self.update_scoreboard()
                self.length = self.length + 1
            return

    def updating_snake(self):
        xinit, yinit, xfin, yfin = self.main_Canvas.coords(self.snake_head)
        xfin = xfin - ((xfin - xinit) / 2)
        yfin = yfin - ((yfin - yinit) / 2)
        self.endsnake.append((xfin, yfin))
        self.main_Canvas.delete('snakebody')
        if len(self.endsnake) >= self.length:
            self.endsnake = self.endsnake[-self.length:]
        self.main_Canvas.create_line(tuple(self.endsnake), tag="snakebody", width=10, fill='green')
        return


if __name__ == '__main__':
    root = main()
    while True:
        root.update()
        root.update_idletasks()
        root.movement()
        time.sleep(0.09)

