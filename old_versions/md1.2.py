#START: DECEMBER 16TH, 2019

#dec 19 - custom sprite, changed to black background, and gets harder
#dec 20 - added missile/player sprites, need to work on earth background

import turtle
import random
import os
import sys


t = turtle.Turtle()
s = turtle.Screen()

#set up screen
s.bgcolor("black")
t.penup()
t.setposition(-300,-300)
t.pendown()
t.pensize(3)
t.speed(0)
t.color("white")
for side in range(4):
    t.forward(600)
    t.left(90)
t.hideturtle()
s.bgpic("background.gif")

#set up sprites
s.register_shape('meteor.gif')
s.register_shape('missile.gif')
s.register_shape('spacecraft.gif')

#create player
player = turtle.Turtle()
player.color("orange")
player.shape('spacecraft.gif')
player.penup()
player.setposition(150,-150)

speed = 5

#motion functions for player
def moveleft():
    global speed
    speed = -5
def moveright():
    global speed
    speed = 5

#create missile

missile = turtle.Turtle()
missile.color('red')
missile.shape('missile.gif')
missile.shapesize(2,2)
missile.speed(0)
missile.setheading(90)
missile.hideturtle()
missile.penup()

missilespeed = 10

#define missile state
#ready to fire and bullet is fired
missilestate = "ready"


def fire_missile():
    
    #declare state of bullet
    global missilestate
    if missilestate == "ready":
        missilestate = "fire"
        #create launch position
        x,y = player.xcor(),player.ycor()
        missile.setposition(x,y+10)
        missile.showturtle()
        
    

#map controls
turtle.listen()
turtle.onkeypress(moveleft,"a")
turtle.onkeypress(moveright,"d")
turtle.onkey(fire_missile,"p")

#boundary check
def playerbound():
    if player.xcor() >= 300:
        moveleft()
    elif player.xcor() <= -300:
        moveright()

#create meteor(s)
m = turtle.Turtle()
m.color("red")
m.shape("meteor.gif")
m.penup()
m.speed(0)
m.setposition(random.randint(-300,300),250)

mspeed = 2

    
#missile-meteor collision
def mmcol():
    if abs(missile.ycor() - m.ycor()) < 29 and abs(missile.xcor() - m.xcor()) < 24:
        return True
    else:
        return False

#player-meteor collision

def pmcol():
    if abs(player.ycor() - m.ycor()) < 29 and abs(player.xcor() - m.xcor()) < 24:
        return True
    else:
        return False

#score
score = 0
#lives
lives = 3
#health of earth
health = 5

fifties_scores = []

#write score(x), lives(l), and earth health (e)
x = turtle.Turtle()
x.hideturtle()
x.penup()
x.setposition(-300,310)
x.color("white")
x.write("Score: {}".format(score),False,align="left",font=("Arial",15,"bold"))

l = turtle.Turtle()
l.hideturtle()
l.penup()
l.setposition(260,310)
l.color("white")
l.write("Lives: {}".format(lives),False,align="left",font=("Arial",15,"bold"))

e = turtle.Turtle()
e.hideturtle()
e.penup()
e.setposition(-280,-280)
e.color("black")
e.write("Earth Health: {}".format(health),False,align="left",font=("Arial",15,"bold"))

while True:

    
    player.forward(speed)
    playerbound()

    #Move missile
    if missilestate == "fire":
        y = missile.ycor()
        y += missilespeed
        missile.sety(y)

        #check missile and boundary
        if missile.ycor() >300:
            missile.hideturtle()
            missilestate = "ready"
    
    #move meteor
    y = m.ycor()
    y -= mspeed
    m.sety(y)

    #change meteor's speed over score
    if score % 50 == 0 and score > 0:
        if score not in fifties_scores:
            fifties_scores.append(score)
        if mspeed < 2 + 0.5*len(fifties_scores):
            mspeed += 0.5
                
    #meteor-earth collision
    if m.ycor() < -200:
        m.setposition(random.randint(-250,250),250)
        health -= 1
        #rewrite health
        e.clear()
        e.write("Earth Health: {}".format(health),False,align="left",font=("Arial",15,"bold"))
        
    #meteor-missile collision
    if mmcol() == True:
        missile.hideturtle()
        missilestate = "ready"
        missile.setposition(0,-400)
        m.setposition(random.randint(-250,250),250)
        score += 10
        #rewrite score
        x.clear()
        x.write("Score: {}".format(score),False,align="left",font=("Arial",15,"bold"))

    #player-meteor collision
    if pmcol() == True:
        player.setposition(random.randint(-250,200),-150)
        m.setposition(random.randint(-250,250),300)
        lives -= 1
        #rewrite lives
        l.clear()
        l.write("Lives: {}".format(lives),False,align="left",font=("Arial",15,"bold"))
        
    if lives == 0:
        break
        

    elif health == 0:
        break
        


game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.setposition(0,0)
game_over.color("white")
game_over.hideturtle()


if lives == 0:
    game_over.write("Game Over, You ran out of lives. Your Score was {}".format(score),False,align="center",font=("Arial",15,"bold"))
else:
    game_over.write("Game Over, the earth was destroyed beyond repair. Your Score was {}".format(score),False,align="center",font=("Arial",15,"bold"))
