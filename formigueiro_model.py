import turtle
import mesa 
import random
import time
import tkinter
import tkinter.messagebox

# MODEL.py 

ID = 4
RANGE = 5
turtle.register_shape("catiorinho.gif")
turtle.register_shape("osso.gif")
turtle.register_shape('chuva.gif')

class FormigaAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model,x,y):
        self.comida = 1
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.shape("catiorinho.gif")
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
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.hideturtle()
        self.t.shapesize(0.1,0.1,0.1)
        self.t.shape("osso.gif")
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

win = turtle.Screen()
win.screensize(1500,2000)
turtle.bgpic('gif.gif')
formigues = FormigueiroModel(4)
while(1):
    formigues.step()
