import random
import turtle
import tkinter as tk
import time
import threading

segundos = 0

def calcula_tempo(s):
    while True:
        s = s + 1
        time.sleep(1)


#x = threading.Thread(target=calcula_tempo, args=(segundos,))
#x.start()


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


def press():
    do_stuff()


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=200)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("cyan")
    button = tk.Button(root, text="Press me", command=press)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")


    label = tk.Label(root)
    label.pack()


    def update(s):
        print("updating")
        s = s + 1
        label['text'] = str(s)

        root.after(1000, update, s)  # run itself again after 1000 ms


    # run first time
    update(segundos)

    root.mainloop()
