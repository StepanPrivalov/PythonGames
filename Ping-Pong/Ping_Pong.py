import turtle
import winsound
#Game without sounds

wn = turtle.Screen()
wn.title = ("Ping-Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

global score1, score2
score2, score1 = 0, 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid = 4, stretch_len = 1)
paddle1.penup()
paddle1.goto(-350, 0)


paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid = 4, stretch_len = 1)
paddle2.penup()
paddle2.goto(350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1.2

ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("red")
ball2.penup()
ball2.goto(-50, -50)
ball2.dx = 1.2
ball2.dy = 1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Player A:0     Player B:0", align = "center", font = ("Bell MT", 24, "normal"))


def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

def yUp(b):
    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

def yDown(b):
    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

def xLeft(b):
    global score1, score2
    if b.xcor() > 390:
        b.goto(0, 0)
        b.dx *= -1
        score1 += 1
        b.dx += 0.05
        b.dy += 0.05
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(score1, score2), align = "center", font = ("Bell MT", 24, "normal"))

def xRight(b):
    global score1, score2
    if b.xcor() < -390:
        b.goto(0, 0)
        b.dx *= -1
        b.dx += 0.1
        b.dy += 0.1
        score2 += 1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(score1, score2), align = "center", font = ("Bell MT", 24, "normal"))

def colLeft(b, pad):
    if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < pad.ycor() + 40 and b.ycor() > pad.ycor() - 40):
        b.setx(-340)
        b.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)


def colRight(b, pad):
    if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < pad.ycor() + 40 and b.ycor() > pad.ycor() - 40):
        b.setx(340)
        b.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

while 1:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)   

    yUp(ball)
    yUp(ball2)
    yDown(ball)
    yDown(ball2)

    xLeft(ball2)
    xRight(ball2)

    xLeft(ball)
    xRight(ball)    

    colRight(ball, paddle2)
    colRight(ball2, paddle2)
    colLeft(ball, paddle1)
    colLeft(ball2, paddle1)