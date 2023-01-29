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


# DESENHA A BOATE
boate_drawing = turtle.Turtle()
boate_drawing.penup()
boate_drawing.goto(TAMANHO_BOATE * -1, TAMANHO_BOATE * -1)
boate_drawing.pendown()
boate_drawing.hideturtle()

for _ in range(4):
    boate_drawing.forward(TAMANHO_BOATE * 2)
    boate_drawing.left(90)

# desenha a porta de entrada
entrada_drawing = turtle.Turtle()
entrada_drawing.penup()
entrada_drawing.goto((TAMANHO_BOATE * -1) + 80, TAMANHO_BOATE)
entrada_drawing.pendown()
entrada_drawing.right(90)
entrada_drawing.forward(40)
entrada_drawing.right(90)
entrada_drawing.forward(80)
entrada_drawing.hideturtle()

# desenha a porta de saida
saida_drawing = turtle.Turtle()
saida_drawing.penup()
saida_drawing.goto( TAMANHO_BOATE - 80, TAMANHO_BOATE)
saida_drawing.pendown()
saida_drawing.right(90)
saida_drawing.forward(40)
saida_drawing.left(90)
saida_drawing.forward(80)
saida_drawing.hideturtle()

#desenha o bar
bar_drawing = turtle.Turtle()
bar_drawing.penup()
bar_drawing.goto(TAMANHO_BOATE - 160, TAMANHO_BOATE * -1)
bar_drawing.pendown()
bar_drawing.left(90)
bar_drawing.forward(40)
bar_drawing.right(90)
bar_drawing.forward(160)
bar_drawing.hideturtle()



class FormigaAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model,x,y):
        self.comida = 1
        self.t = turtle.RawTurtle(canvas)
        self.t.hideturtle()
        self.t.penup()
        self.t.shape("turtle")
        self.t.color("green")
        self.current_x = x
        self.current_y = y
        self.t.setposition(self.current_x,self.current_y)
        self.t.showturtle()
        super().__init__(unique_id, model)

    def step(self):
        new_x = self.current_x + random.randint(-1 * RANGE , RANGE)
        new_y = self.current_y + random.randint(-1 * RANGE , RANGE)
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        self.t.goto(new_x,new_y)
        self.current_x = new_x
        self.current_y = new_y
        print("formiga: " + str(self.unique_id) + " andou para :" + str(new_x) +"|" + str(new_y))


class FormigaModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N, x, y):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = FormigaAgent(i, self, x, y)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()


## FORMIGUEIROS 

class FormigueiroAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.quantidade_de_formigas = 0
        self.capacidade_de_comida = 0
        self.t = turtle.RawTurtle(canvas)
        self.t.hideturtle()
        self.t.penup()
        self.t.shape("circle")
        self.t.color("brown")
        self.t.shapesize(3,3,15)
        self.fix_position_x = random.randint(-300, 300)
        self.fix_position_y = random.randint(-300, 300)
        self.t.setposition(self.fix_position_x,self.fix_position_y)
        self.t.showturtle()
        self.formigas = FormigaModel(5,self.fix_position_x, self.fix_position_y)
        self.numero_de_formigas = 0
        self.ids = 6

    def gerar_formiga(self):
        a = FormigaAgent(self.ids,self, self.fix_position_x, self.fix_position_y)
        self.formigas.schedule.add(a)
        self.ids += 1
        self.numero_de_formigas += 1

    def retirar_comida(self):
        self.capacidade_de_comida -= 1

    def depositar_comida(self):
        self.capacidade_de_comida += 1

    def step(self):
        if self.numero_de_formigas < 5:
            self.gerar_formiga()
        self.formigas.step()


class FormigueiroModel(mesa.Model):
    def __init__(self, N):
        self.num_agents = N

        self.schedule = mesa.time.RandomActivation(self)
        self.id = 0
        for i in range(self.num_agents):
            a = FormigueiroAgent(i, self)
            self.schedule.add(a)
            self.id +=1

    def step(self):
        self.schedule.step()
                    
    def addFormigueiro(self):
        a = FormigueiroAgent(self.id, self)
        self.schedule.add(a)
        self.id += 1




## Test Tkinker
window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
draw = turtle.RawTurtle(canvas)
formigueiros = FormigueiroModel(0)


def Play():
    global fomigueiros
    fomigueiros = FormigueiroModel(4)
    while True:
        fomigueiros.step()

def Add_formigueiro():
    global formigueiros
    formigueiros.addFormigueiro()

Play_Button = tkinter.Button(master = window, text ="Play!", command = Play)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Adicionar Formigueiro", command = Add_formigueiro)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')
#
window.mainloop()
