import turtle
import mesa
import random
import time
import tkinter
import tkinter.messagebox

from utils.nomes import nomes
from utils.desenha_mapa import desenha_entrada, desenha_saida

# MODEL.py

ID = 4
RANGE = 5
TAMANHO_BOATE = 200
COORD_SAIDA = (160, 180)
COORD_BEBIDA = (150, -180)

window = tkinter.Tk()

canvas = tkinter.Canvas(master=window, width=800, height=800)
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
desenha_entrada(TAMANHO_BOATE, canvas)

# desenha a porta de saida
desenha_saida(TAMANHO_BOATE, canvas)

# desenha o bar
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
        self.nome = nomes[unique_id]
        self.energia = 50
        self.embriaguez = 0
        self.shape = turtle.RawTurtle(canvas)
        self.shape.hideturtle()
        self.shape.shape("circle")
        self.shape.penup()
        self.shape.color("blue")
        self.shape.setposition(self.x, self.y)
        self.shape.showturtle()

    def move(self):
        if(self.energia == 0):
            self.gotocoordinate()
        else:
            if self.shape.xcor() >= 180:
                self.x -= 5
            elif self.shape.ycor() >= 180:
                self.y -= 5
            elif self.shape.xcor() <= -180:
                self.x += 5
            elif self.shape.ycor() <= -180:
                self.y += 5

            elif(self.shape.distance(self.shape) > 100):
                self.x += random.randint(5, 10)
                self.y += random.randint(-20, -10)
            else:
                self.x += random.randint(-10, 10)
                self.y += random.randint(-10, 10)
            self.shape.goto(self.x, self.y)

            self.energia -= 1

    def gotocoordinate(self):
        x, y = self.shape.position()
        xs, ys = COORD_SAIDA

        if(x < xs):
            self.x += 5
        if(y < ys):
            self.y += 5

        if(x >= 160 and y >= 180):
            self.shape.hideturtle()

        self.shape.goto(self.x, self.y)

    def mostra_status(self):
        print(self.unique_id)
        print(self.energia)
        print(self.nome)


class BaladaModel(mesa.Model):
    def __init__(self, N):
        self.num_pessoas = N
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.pessoas = []

        for i in range(self.num_pessoas):
            p = Pessoa(i, self, -170, 180)
            self.pessoas.append(p)
            self.schedule.add(p)
            escreverLog(f'{p.nome} entrou na balada\n')

    def step(self):
        for pessoa in self.schedule.agents:
            pessoa.move()
            if(pessoa.shape.position == COORD_SAIDA):
                self.schedule.remove(pessoa)

    def numero_pessoas(self):
        print(self.schedule.get_agent_count())

    def remover_pessoa(self):
        for i in self.pessoas:
            i.mostra_status()

def escreverLog(mensagem):
    log = open("utils/log.txt", "a")
    log.write(f"{mensagem}\n")
    log.close()


FLAG = True

# Test Tkinker
global balada
balada = BaladaModel(10)


def Play():
    while FLAG:
        balada.step()


def funcao_placeholder():
    balada.remover_pessoa()


Play_Button = tkinter.Button(
    master=window, text="Iniciar balada", command=Play)
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Check todo mundo", command=funcao_placeholder)
Board_Button.config(bg="cyan", fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

window.mainloop()
