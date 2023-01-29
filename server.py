import turtle
import mesa 
import random
import time
import tkinter
import tkinter.messagebox

# MODEL.py 

ID = 4
RANGE = 5
TAMANHO_BOATE = 200

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)


# DESENHA A BOATE
boate_drawing = turtle.RawTurtle(canvas)
boate_drawing.penup()
boate_drawing.goto(TAMANHO_BOATE * -1, TAMANHO_BOATE * -1)
boate_drawing.pendown()
boate_drawing.hideturtle()

for _ in range(4):
    boate_drawing.forward(TAMANHO_BOATE * 2)
    boate_drawing.left(90)

# desenha a porta de entrada
entrada_drawing = turtle.RawTurtle(canvas)
entrada_drawing.penup()
entrada_drawing.goto((TAMANHO_BOATE * -1) + 80, TAMANHO_BOATE)
entrada_drawing.pendown()
entrada_drawing.right(90)
entrada_drawing.forward(40)
entrada_drawing.right(90)
entrada_drawing.forward(80)
entrada_drawing.hideturtle()

# desenha a porta de saida
saida_drawing = turtle.RawTurtle(canvas)
saida_drawing.penup()
saida_drawing.goto( TAMANHO_BOATE - 80, TAMANHO_BOATE)
saida_drawing.pendown()
saida_drawing.right(90)
saida_drawing.forward(40)
saida_drawing.left(90)
saida_drawing.forward(80)
saida_drawing.hideturtle()

#desenha o bar
bar_drawing = turtle.RawTurtle(canvas)
bar_drawing.penup()
bar_drawing.goto(TAMANHO_BOATE - 160, TAMANHO_BOATE * -1)
bar_drawing.pendown()
bar_drawing.left(90)
bar_drawing.forward(40)
bar_drawing.right(90)
bar_drawing.forward(160)
bar_drawing.hideturtle()


class Pessoa(mesa.Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.x = x
        self.y = y
        self.shape = turtle.RawTurtle(canvas)
        self.shape.hideturtle()
        self.shape.shape("circle")
        self.shape.penup()
        self.shape.color("blue")
        self.shape.setposition(self.x, self.y)
        self.shape.showturtle()

    def move(self):

        if self.shape.distance(self.shape) > 100:
            self.x += random.randint(5,10)
            self.y += random.randint(-20,-10)
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.shape.goto(self.x, self.y)

class BaladaModel(mesa.Model):
    def __init__(self, N):
        self.num_pessoas = N
        self.schedule = mesa.time.SimultaneousActivation(self)
        for i in range(self.num_pessoas):
            p = Pessoa(i, self, -300, 300)
            self.schedule.add(p)

    def step(self):
        for pessoa in self.schedule.agents:
            pessoa.move()





## Test Tkinker
global balada
balada = BaladaModel(10)
def Play():
    while True:
        balada.step()

def Add_formigueiro():
    pass

Play_Button = tkinter.Button(master = window, text ="Play!", command = Play)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Adicionar Formigueiro", command = Add_formigueiro)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

window.mainloop()