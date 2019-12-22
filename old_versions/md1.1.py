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

speed = 0

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

    #change meteors/player's speed over score
    if score % 50 == 0 and score > 0:
        if score not in fifties_scores:
            fifties_scores.append(score)
        if mspeed < 2 + 0.5*len(fifties_scores):
            mspeed += 0.5
            print('new meteor speed:',mspeed)
                
    #meteor-earth collision
    if m.ycor() < -200:
        m.setposition(random.randint(-250,250),250)
        health -= 1
        print("Earth Health:", health)
        
    #meteor-missile collision
    if mmcol() == True:
        missile.hideturtle()
        missilestate = "ready"
        missile.setposition(0,-400)
        m.setposition(random.randint(-250,250),250)
        score += 10
        print('Score:',score)

    #player-meteor collision
    if pmcol() == True:
        player.setposition(random.randint(-250,200),-150)
        m.setposition(random.randint(-250,250),300)
        lives -= 1
        print('Lives left:',lives)
        
    if lives == 0:
        break
        

    elif health == 0:
        break
        

if lives == 0:
    print("Game Over, You ran out of lives. Your Score was",score)
else:
    print("Game Over, the earth was destroyed beyond repair. Your Score was",score)
