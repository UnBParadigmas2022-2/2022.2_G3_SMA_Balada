import turtle
import mesa
import random
import time

RANGE = 5

class FormigaAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.comida = 1
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.shape("turtle")
        self.t.color("green")
        self.current_x = 0
        self.current_y = 0

    def step(self):
        new_x = self.current_x + random.randint(-1 * RANGE , RANGE)
        new_y = self.current_y + random.randint(-1 * RANGE , RANGE)
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        self.t.goto(new_x,new_y)
        self.current_x = new_x
        self.current_y = new_y
        print("formiga: " + str(self.unique_id) + " andou para :" + str(new_x) +"|" + str(new_y))


class FormigueiroModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = FormigaAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

novo_formigueiro = FormigueiroModel(5)

while True:
    novo_formigueiro.step()
    time.sleep(0.1)
