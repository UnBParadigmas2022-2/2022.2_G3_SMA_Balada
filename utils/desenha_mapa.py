import turtle


def desenha_entrada(TAMANHO_BOATE, canvas):
    entrada_drawing = turtle.RawTurtle(canvas)
    entrada_drawing.penup()
    entrada_drawing.goto((TAMANHO_BOATE * -1) + 80, TAMANHO_BOATE)
    entrada_drawing.pendown()
    entrada_drawing.right(90)
    entrada_drawing.forward(40)
    entrada_drawing.right(90)
    entrada_drawing.forward(80)
    entrada_drawing.hideturtle()

def desenha_saida(TAMANHO_BOATE, canvas):
    saida_drawing = turtle.RawTurtle(canvas)
    saida_drawing.penup()
    saida_drawing.goto(TAMANHO_BOATE - 80, TAMANHO_BOATE)
    saida_drawing.pendown()
    saida_drawing.right(90)
    saida_drawing.forward(40)
    saida_drawing.left(90)
    saida_drawing.forward(80)
    saida_drawing.hideturtle()