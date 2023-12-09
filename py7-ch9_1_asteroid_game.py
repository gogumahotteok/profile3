import turtle
import random
import sys
import os

player = turtle.Turtle()
turtle.title("JBNU Computer Science & Coding = Python")
player.color("purple")
player.width(4)
player.shape("turtle")
player.up()
player.speed(0)
screen = player.getscreen()

player.up()
player.goto(-300, 300)
player.down()
player.goto(300, 300)                   # 경기장을 그린다. 
player.goto(300, -300)
player.goto(-300, -300)
player.goto(-300, 300)
player.up()
player.goto(0, 0)

score=0
display = turtle.Turtle()	        # 점수를 표시하는 터틀 객체를 생성한다. 
display.ht()
display.color("green")
display.up()
display.goto(-300,300)
display.write(f"Score : {score}", font=("font",20,"bold"))

asteroids = []				# 공백 리스트를 생성한다.

for i in range(5):			# n 개의 터틀을 생성한다.
        a = turtle.Turtle()
        a.color("red")
        a.shape("circle")
        a.penup()
        a.speed(0)
        a.goto(random.randint(-300, 300), random.randint(-300, 300))
        asteroids.append(a)		# 생성된 터틀을 리스트에 추가한다.

def turnleft():
    player.left(30)                     

def turnright():
    player.right(30)                   

def moveUp():
        #player.setheading(90)
        player.forward(15)

def moveDown():
        #player.setheading(270)
        player.forward(15)
        
def pause():  
    os.system("pause")

def stop():  
    screen.bye()

screen.listen()
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(moveUp,"Up")
screen.onkeypress(moveDown,"Down")
screen.onkeypress(pause, key='p')
screen.onkeypress(stop, key='q')

def check(a):
        global score
        if player.distance(a) <= 15:
              player.write("Kill !")
              a.ht()
              asteroids.remove(a)
              
              score = score + 1			# 점수를 하나 증가한다. 
              display.clear()			# 점수를 다시 표시한다. 
              display.write(f"Score : {score}", font=("font",20,"bold"))
              
        if not asteroids:
              player.color('green')
              player.write("You Win!",font=("Arial",30),align="center")
              sys.exit()

def ch_player(player):
        if player.xcor() <= -300 or player.xcor() >= 300 or player.ycor() <= -300 or player.ycor() >= 300:
                player.right(180)
        """        
        if player.xcor() <= -300:
            player.goto(300,player.ycor())
        elif player.xcor() >= 300:
            player.goto(-300,player.ycor())
        elif player.ycor() <= -300:
            player.goto(player.xcor(),300)
        elif player.ycor() >= 300:
            player.goto(player.xcor(),-300)
        """
def ch_a(a):
    if a.xcor() <= -300 or a.xcor() >= 300 or a.ycor() <= -300 or a.ycor() >= 300:
         a.home()
         
def play():
    player.forward(5)                           # 5픽셀 전진
    ch_player(player)
    for a in asteroids:                         # 리스트에 저장된 모든 터틀에 대하여
        a.right(random.randint(-180, 180))
        a.forward(5)
        ch_a(a)
        check(a)
    screen.ontimer(play, 10)                    # 10/1000 초가 지나면 play()를 다시 호출,(10 밀리세컨드(ms))

screen.ontimer(play, 10)
screen.mainloop()
