import turtle

# Настройка окна
window = turtle.Screen()
window.title("Пинг-Понг")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Левая ракетка
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Правая ракетка
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Мяч
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05

# Счет
left_score = 0
right_score = 0

# Пен для счета
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Игрок 1: 0  Игрок 2: 0", align="center", font=("Courier", 24, "normal"))

# Функции для управления ракетками
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 30
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 30
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 30
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 30
    right_paddle.sety(y)

# Клавиатурные бинды
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Главный игровой цикл
while True:
    window.update()
    
    # Перемещение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Границы
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        pen.clear()
        pen.write("Игрок 1: {}  Игрок 2: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        pen.clear()
        pen.write("Игрок 1: {}  Игрок 2: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    # Отражение мяча от ракеток
    if (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
