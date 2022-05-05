import turtle
import time
import random
random.seed()
player1score = 0
player2score = 0
print("how many players? (0,1,2)")
temp = int(input("? "))
if temp == 2:
    twoPlayer = True
elif temp == 1:
    twoPlayer = False
elif temp == 0:
    twoPlayer = 3
else:
    exit()
#setup of window
window = turtle.Screen()
window.title("Tennis New Game 2023")
window.bgcolor("lime")
window.setup(width=1280, height=720)
window.tracer(0)

#paddle left
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(5, 1)
paddle1.penup()
paddle1.goto(-600, 0)

#paddle right
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("Red")
paddle2.shapesize(5, 1)
paddle2.penup()
paddle2.goto(600, 0)

#score initialise
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.color("red")
pen.goto(300,280)
pen.write(str(player2score), align= "center", font=("arial", 50, "normal"))
pen.color("blue")
pen.goto(-300,280)
pen.write(str(player1score), align= "center", font=("arial", 50, "normal"))
pen.hideturtle()
#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.shapesize(0.75,0.75)
ball.penup()
ball.dx = 0.2
ball.dy = 0.2

def leftPaddleUp():
    y = paddle1.ycor()
    y = y + 20
    paddle1.sety(y)
def leftPaddleDown():
    y = paddle1.ycor()
    y = y - 20
    paddle1.sety(y)

def rightPaddleUp():
    y = paddle2.ycor()
    y = y + 20
    paddle2.sety(y)
def rightPaddleDown():
    y = paddle2.ycor()
    y = y - 20
    paddle2.sety(y)

#keybaord input
window.listen()
if not(twoPlayer == 3):
    window.onkeypress(leftPaddleUp, "w")
    window.onkeypress(leftPaddleDown, "s")
if twoPlayer == True:
    window.onkeypress(rightPaddleUp, "Up")
    window.onkeypress(rightPaddleDown, "Down")
else:
    pass
#main game loop
while True:
    window.update()
    if not(twoPlayer == True) and random.randint(0,99) == 1:
        temp = random.randint(0,2)
        if paddle2.ycor() < ball.ycor():
            #go up
            y = paddle2.ycor()
            y = y + 20
            paddle2.sety(y)
        elif paddle2.ycor() > ball.ycor():
            #go down
            y = paddle2.ycor()
            y = y - 20
            paddle2.sety(y)
    if twoPlayer == 3 and random.randint(0,99) == 1:
        if paddle1.ycor() < ball.ycor():
            #go up
            y = paddle1.ycor()
            y = y + 20
            paddle1.sety(y)
        elif paddle1.ycor() > ball.ycor():
            #go down
            y = paddle1.ycor()
            y = y - 20
            paddle1.sety(y)
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #ball colission with paddle
    if ball.xcor() < -580 and ball.xcor() >-590 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.setx(-580)
        ball.dx = ball.dx * -1
    elif ball.xcor() < 590 and ball.xcor() > 580 and ball.ycor() < paddle2.ycor() +50 and ball.ycor() > paddle2.ycor() - 50:
        ball.setx(580)
        ball.dx = ball.dx * -1

    #border checking
    #top and bottom
    if ball.ycor() > 360:
        ball.sety(359)
        ball.dy = ball.dy * -1
    elif ball.ycor() < -360:
        ball.sety(-359)
        ball.dy = ball.dy * -1
        #left and right sides + score display
    elif ball.xcor() > 630:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        player1score = player1score + 1
        pen.clear()
        pen.showturtle()
        pen.color("red")
        pen.goto(300,280)
        pen.write(str(player2score), align= "center", font=("arial", 50, "normal"))
        pen.color("blue")
        pen.goto(-300,280)
        pen.write(str(player1score), align= "center", font=("arial", 50, "normal"))
        pen.hideturtle()
    elif ball.xcor() < -630:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        player2score = player2score + 1
        pen.clear()
        pen.showturtle()
        pen.color("red")
        pen.goto(300,280)
        pen.write(str(player2score), align= "center", font=("arial", 50, "normal"))
        pen.color("blue")
        pen.goto(-300,280)
        pen.write(str(player1score), align= "center", font=("arial", 50, "normal"))
        pen.hideturtle()
    #win check
    if player1score >=7:
        print("Blue Win!")
        time.sleep(2)
        player1score = 0
        player2score = 0
    elif player2score >=7:
        print("Red Win!")
        time.sleep(2)
        player1score = 0
        player2score = 0
