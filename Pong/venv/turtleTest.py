import os
import turtle

# janela do jogo
window = turtle.Screen()
window.setup(1280, 720)
window.title('Pong')
window.bgcolor('black')

# player
player1 = turtle.Turtle()
player1.penup()
player1.speed(0)
player1.shape('square')
player1.color('red')
player1.goto(-600, 0)
player1.shapesize(8, 1)

# player2
player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.shape('square')
player2.color('red')
player2.goto(600, 0)
player2.shapesize(8, 1)

# ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.goto(0, 0)
ball.shapesize(1, 1)
ball.velx = 2
ball.vely = 2

#score
score = turtle.Turtle()
score.shape('square')
score.color('red')
score.write('Score A: ')
# player 1 moviment functions
def up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

    if player1.ycor() >= 260:
        player1.sety(260)

    pass

def down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)


    if player1.ycor() <= -260:
        player1.sety(-260)
    pass

# player 2 moviment
def up2():
    y = player2.ycor()
    y += 20
    player2.sety(y)

    if player2.ycor() >= 260:
        player2.sety(260)

    pass

def down2():
    y = player2.ycor()
    y -= 20
    player2.sety(y)


    if player2.ycor() <= -260:
        player2.sety(-260)
    pass

def move_ball():
    ball.setx(ball.xcor() + ball.velx)
    ball.sety(ball.ycor() + ball.vely)

    if ball.xcor() > 600:
        ball.velx *= -1

    elif ball.xcor() < -600:
        ball.velx *= -1

    if ball.ycor() > 350:
        ball.sety(-350)
        ball.vely *= -1

    elif ball.ycor() < -350:
        ball.sety(350)
        ball.vely *= -1
# key input
window.listen()
window.onkeypress(up, 'w')
window.onkeypress(up2, 'Up')
window.onkeypress(down, 's')
window.onkeypress(down2, 'Down')

# repetition loop
loop = True
while loop:
    move_ball()
    window.update()
