import turtle
import winsound
#Game without sounds

wn = turtle.Screen()
wn.title = ("Ping-Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

score1 = 0
score2 = 0

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
ball.dy = 1

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

wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

while 1:

    ball.setx(ball.xcor() + ball.dx)
    wn.update()
    ball.sety(ball.ycor() + ball.dy)
   


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
      

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(score1, score2), align = "center", font = ("Bell MT", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(score1, score2), align = "center", font = ("Bell MT", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)