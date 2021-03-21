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
player1.goto(-550, 0)
player1.shapesize(8, 1)

# player2
player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.shape('square')
player2.color('red')
player2.goto(550, 0)
player2.shapesize(8, 1)

# ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.goto(0, 0)
ball.shapesize(1, 1)
ball.velx = 8
ball.vely = 4

#score
score = turtle.Turtle()
score.penup()
score.speed(0)
score.shape('square')
score.hideturtle()
score.color('white')
score.goto(0 , 330)
score.a = 0
score.b = 0
score.write(f'Score A: {score.a}     Score B: {score.b}', align='center', font=('Arial', 24, 'normal'))

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

# player 2 seguir a bolinha:
    player2.sety(ball.ycor())

    if ball.xcor() > 630:
        score.a += 1
        placar()

    elif ball.xcor() < -630:
        score.b += 1
        placar()

    if ball.ycor() > 350:
        ball.sety(350)
        ball.vely *= -1

    elif ball.ycor() < -350:
        ball.sety(-350)
        ball.vely *= -1

def placar():
    score.clear()
    ball.velx *= -1
    ball.goto(0, 0)
    score.write(f'Score A: {score.a}     Score B: {score.b}', align='center', font=('Arial', 24, 'normal'))

def colision():

    if ball.xcor() < -535 and ball.ycor() < player1.ycor() +90 and ball.ycor() > player1.ycor() -90:
        ball.setx(-535)
        ball.velx *= -1

    if ball.xcor() > 535 and ball.ycor() < player2.ycor() +90 and ball.ycor() > player2.ycor() -90:
        ball.setx(535)
        ball.velx *= -1

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
    colision()
    window.update()
