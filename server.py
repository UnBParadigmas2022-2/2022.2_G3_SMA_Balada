import turtle
import mesa
import random
import time
import tkinter
import tkinter.messagebox
from utils.calcula_disntacia import distance 

from utils.nomes import nomes
from utils.desenha_mapa import desenha_entrada, desenha_saida, desenha_bar

# MODEL.py

ID = 4
RANGE = 5
TAMANHO_BOATE = 200
COORD_SAIDA = (160, 180)
COORD_BEBIDA = (150, -180)

window = tkinter.Tk()

canvas = tkinter.Canvas(master=window, width=800, height=800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
screen = turtle.TurtleScreen(canvas)
screen.register_shape('gifs/boneco_normal.gif')
screen.register_shape('gifs/boneco_bebida.gif')
screen.register_shape('gifs/boneco_cansado.gif')

# DESENHA A BOATE
boate_drawing = turtle.RawTurtle(screen)
boate_drawing.penup()
boate_drawing.goto(TAMANHO_BOATE * -1, TAMANHO_BOATE * -1)
boate_drawing.pendown()
boate_drawing.hideturtle()

for _ in range(4):
    boate_drawing.forward(TAMANHO_BOATE * 2)
    boate_drawing.left(90)

# desenha a porta de entrada
desenha_entrada(TAMANHO_BOATE, screen)

# desenha a porta de saida
desenha_saida(TAMANHO_BOATE, screen)

# desenha o bar
desenha_bar(TAMANHO_BOATE, screen)

class Pessoa(mesa.Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.x = x
        self.y = y
        self.nome = nomes[unique_id]
        self.energia = random.randint(200,400)
        self.embriaguez = 0
        self.bebida = False
        self.shape = turtle.RawTurtle(screen)
        self.shape.hideturtle()
        self.shape.shape('gifs/boneco_normal.gif')
        self.shape.penup()
        self.shape.setposition(self.x, self.y)
        self.shape.showturtle()

    def move(self):
        if(self.energia == 0):
            self.gotosaida()
        elif(distance(self.shape.position(), COORD_BEBIDA) < 320 and self.bebida == False):
            self.gotobebida()
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

    def gotobebida(self):
        x, y = self.shape.position()
        xs, ys = COORD_BEBIDA

        if(x < xs):
            self.x += 5
        if(y > ys):
            self.y -= 5

        if(x >= 150 and y <= -180):
            self.energia += 20
            self.bebida = True
            self.shape.shape('gif/boneco_bebida.gif')

        self.shape.goto(self.x, self.y)

    def gotosaida(self):
        x, y = self.shape.position()
        xs, ys = COORD_SAIDA

        if(x < xs):
            self.x += 5
        if(y < ys):
            self.y += 5

        if(x >= 160 and y >= 180):
            self.shape.hideturtle()

        self.shape.shape('gifs/boneco_cansado.gif')
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
        self.id = 10

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
    
    def adicionar_pessoa(self):
        a = Pessoa(self.id,self,-170,180)
        self.id += 1
        self.pessoas.append(a)
        self.schedule.add(a)
        escreverLog(f'{a.nome} entrou na balada\n')

    def next_agent_id(self):
        return max([agent.unique_id for agent in self.schedule.agents]) + 1

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

def adicionar_pessoas():
    balada.adicionar_pessoa()


Play_Button = tkinter.Button(
    master=window, text="Iniciar balada", command=Play)
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Check todo mundo", command=funcao_placeholder)
Board_Button.config(bg="cyan", fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Adicionar pessoas", command=adicionar_pessoas)
Board_Button.config(bg="cyan", fg="black")
Board_Button.grid(padx=2, pady=2, row=2, column=11, sticky='nsew') 
window.mainloop()