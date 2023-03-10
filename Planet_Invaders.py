# Import modules
import turtle
import time
import random

#varibles 
invader_speed = 2
bullet_speed = 10
ibullet_speed = 10

# Functions
player_dx = 15


def move_left():
    
    x = player.xcor() - player_dx
    if x < -190:
        x = -190
        
    player.setx(x)

def move_right():
    
    x = player.xcor() + player_dx
    if x > 190:
        x = 190
        
    player.setx(x) 


def fire_bullet():
    
    print("\n Player: \n Fired Bullet")
    
    x = player.xcor()
    y = player.ycor()
    
    bullet.setposition(x,y+30)
    bullet.showturtle()
    

def llife():
    global life
    global ibullet_speed
    global invader_speed

    print("\n Player:\n Lost a Life")
    
    life-=1
    
    lscore_pen.clear()
    lscore_pen.write('Lives Left: %s' % life+ ' / 10')
    
    invader_speed=2
    
    ibullet_speed=10
    
    player.setposition(0,-180)
    
    
def enemyfire(inbaber):

    print("\n Invader:\n Fired Bullet")
    
    ex=inbaber.xcor()
    ey=inbaber.ycor()
    
    ibullet.setposition(ex,ey+-30)
    ibullet.showturtle()


def healthFire():
    print("\n Health Projectile:\n Fired")

    HealthBullet.setpos(random.randint(-180, 180),180)
    
    HealthBullet.showturtle()

## Game Setup
print("Setting Up Game")

# Set up window
wn = turtle.Screen()
wn.setup(width = 540,height = 540)
wn.bgcolor('lightgreen')
wn.title("Planet Invaders (Beta V1.1.0)")

# Draw border, 400x400 square
border = turtle.Turtle()
border.speed(0) 
border.color('black')
border.up()
border.setposition(-200,-200)
border.down()
border.pensize(3)
for side in range(4):
    border.fd(400)
    border.lt(90) # Turn left 90 degree
border.hideturtle()

# Score
# Set score to be 0 initially
score = 0

#Draw score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('black')
score_pen.up()
score_pen.setposition(-200,210)
score_pen.write('Score: %s' % score)
score_pen.hideturtle()

#Lives
life=3

#Draw lives left
lscore_pen = turtle.Turtle()
lscore_pen.speed(0)
lscore_pen.color('black')
lscore_pen.up()
lscore_pen.setposition(-200,-220)
lscore_pen.write('Lives Left: %s' % life+ ' / 10')
lscore_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.up()
player.speed(0)
player.setposition(0,-180)
player.setheading(90)

#Create player's bullet​
bullet = turtle.Turtle()
bullet.color('blue')
bullet.shape('triangle')
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#Create Health Projectile
HealthBullet = turtle.Turtle()
HealthBullet.color('#008900')
HealthBullet.shape('triangle')
HealthBullet.up()
HealthBullet.speed(0)
HealthBullet.setheading(-90)
HealthBullet.shapesize(0.5,0.5)
HealthBullet.hideturtle()
HealthBullet.setpos(0,200)

#Create invader turtles
invader = turtle.Turtle()
invader.up()
invader.speed(0)
invader.setposition(random.randint(-180, 180),random.randint(0, 180))

invader2 = turtle.Turtle()
invader2.up()
invader2.speed(0)
invader2.setposition(random.randint(-180, 180),random.randint(0, 180))

invader3 = turtle.Turtle()
invader3.up()
invader3.speed(0)
invader3.setposition(random.randint(-180, 180),random.randint(0, 180))

invader4 = turtle.Turtle()
invader4.up()
invader4.speed(0)
invader4.setposition(random.randint(-180, 180),random.randint(0, 180))

# Create Invaders's bullet​
ibullet = turtle.Turtle()
ibullet.color('red')
ibullet.shape('triangle')
ibullet.up()
ibullet.speed(0)
ibullet.setheading(-90)
ibullet.shapesize(0.5,0.5)
ibullet.hideturtle()
ibullet.setpos(0,-400)

# Create keyboard binding
turtle.listen()

turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,'Up')

turtle.onkey(move_left,'a')
turtle.onkey(move_right,'d')
turtle.onkey(fire_bullet,'w')

turtle.onkey(fire_bullet,'space')


invader_speed = 2
bullet_speed = 10
ibullet_speed = 10

print("Game Ready")

while True:
    
    # Invader movement
    invader.fd(invader_speed)
    invader2.fd(invader_speed)
    invader3.fd(invader_speed)
    invader4.fd(invader_speed)
    
    
    # Checking if player won
    if int(score) == 1000000:
        
        print("\n Player: \n Won Game")

        invader.hideturtle()
        invader2.hideturtle()
        invader3.hideturtle()
        invader4.hideturtle()
        player.hideturtle()
        bullet.hideturtle()
        ibullet.hideturtle()

        invader.color('lightgreen')
        invader2.color('lightgreen')
        invader3.color('lightgreen')
        invader4.color('lightgreen')
        player.color('lightgreen')
        bullet.color('lightgreen')
        ibullet.color('lightgreen')
        
        GO = turtle.Turtle()
        GO.pensize(3)
        GO.speed(0)
        GO.color('black')
        GO.up()
        GO.setposition(-30,0)
        GO.write('YOU WIN')
        GO.hideturtle()

        score_pen.speed(0)
        score_pen.color('black')
        score_pen.up()
        score_pen.setposition(-40,-30)
        score_pen.write('YOU GOT 1,000,000')
        score_pen.hideturtle()

        turtle.done()
        exit()
        quit()
        
        
    #Checking Lives
    if life == 0:

        print("\n Player: \n Lost Game")

        invader.hideturtle()
        invader2.hideturtle()
        invader3.hideturtle()
        invader4.hideturtle()
        player.hideturtle()
        bullet.hideturtle()
        ibullet.hideturtle()

        invader.color('lightgreen')
        invader2.color('lightgreen')
        invader3.color('lightgreen')
        invader4.color('lightgreen')
        player.color('lightgreen')
        bullet.color('lightgreen')
        ibullet.color('lightgreen')
        
        GO = turtle.Turtle()
        GO.pensize(3)
        GO.speed(0)
        GO.color('black')
        GO.up()
        GO.setposition(-30,0)
        GO.write('GAME OVER')
        GO.hideturtle()

        score_pen.speed(0)
        score_pen.color('black')
        score_pen.up()
        score_pen.setposition(-40,-30)
        score_pen.write('Your Score Was: \n           %s' % score)
        score_pen.hideturtle()

        turtle.done()
        exit()
        quit()


    # Check if invader's hit the border 
    if invader.xcor() > 190 or invader.xcor() < -190:
        
        invader.right(180)
        invader.sety(invader.ycor()-10)
        invader.fd(invader_speed)
        
    elif invader2.xcor() > 190 or invader2.xcor() < -190:
        
        invader2.right(180)
        invader2.sety(invader2.ycor()-10)
        invader2.fd(invader_speed)
        
    elif invader3.xcor() > 190 or invader3.xcor() < -190:
        
        invader3.right(180)
        invader3.sety(invader3.ycor()-10)
        invader3.fd(invader_speed)
        
    elif invader4.xcor() > 190 or invader4.xcor() < -190:
        
        invader4.right(180)
        invader4.sety(invader4.ycor()-10)
        invader4.fd(invader_speed)
        
        
        
    # Check if invader went outside of the border
    if invader.xcor() > 205 or invader.xcor() < -205:
        
        invader.right(180)
        invader.setpos(0,180)
        invader.fd(invader_speed)
        
    elif invader2.xcor() > 205 or invader2.xcor() < -205:
        
        invader2.right(180)
        invader2.setpos(0,180)
        invader2.fd(invader_speed)
        
    elif invader3.xcor() > 205 or invader3.xcor() < -205:
        
        invader3.right(180)
        invader3.setpos(0,180)
        invader3.fd(invader_speed)
        
    elif invader4.xcor() > 205 or invader4.xcor() < -205:
        
        invader4.right(180)
        invader4.setpos(0,180)
        invader4.fd(invader_speed)
        
    
        
    # Check if invader's hit the player
    if invader.ycor() <= player.ycor()+10:
        
        llife()
        x = random.randint(-180,180)
        invader.setposition(x,180)
        
    if invader2.ycor() <= player.ycor()+10:
        
        llife()
        x = random.randint(-180,180)
        invader2.setposition(x,180)
        
    if invader3.ycor() <= player.ycor()+10:
        
        llife()
        x = random.randint(-180,180)
        invader3.setposition(x,180)
        
    if invader4.ycor() <= player.ycor()+10:
        
        llife()
        x = random.randint(-180,180)
        invader4.setposition(x,180)
        
    
    # Bullet Movment
    bullet.fd(bullet_speed)
    ibullet.fd(ibullet_speed)
    HealthBullet.fd(bullet_speed)
    

    # Check if invaders were hit
    if abs(bullet.xcor() - invader.xcor()) < 15 and \
       abs(bullet.ycor() - invader.ycor()) < 15:
           
        print("\n Invader: \n Was Killed")

       # update the score
        score = score + 100
        score_pen.clear()
        score_pen.write('Score: %s' % score)
       
       #reset invader and player
        bullet.hideturtle()
        bullet.setpos(0, 200)
        invader.hideturtle()
        time.sleep(1)

        invader.showturtle()
        x = random.randint(-180,180)
        invader.setposition(x,180)

        invader_speed=invader_speed+0.65
        ibullet_speed=ibullet_speed+0.1
        
        
    elif abs(bullet.xcor() - invader2.xcor()) < 15 and \
       abs(bullet.ycor() - invader2.ycor()) < 15:
           
        print("\n Invader: \n Was Killed")
           
       # update the score
        score = score + 100
        score_pen.clear()
        score_pen.write('Score: %s' % score)
       
       #reset invader and player
        bullet.hideturtle()
        bullet.setpos(0, 200)
        invader2.hideturtle()
        time.sleep(1)

        invader2.showturtle()
        x = random.randint(-180,180)
        invader2.setposition(x,180)

        invader_speed=invader_speed+0.65
        ibullet_speed=ibullet_speed+0.1
        
        
    elif abs(bullet.xcor() - invader3.xcor()) < 15 and \
       abs(bullet.ycor() - invader3.ycor()) < 15:
           
        print("\n Invader: \n Was Killed")
           
       # update the score
        score = score + 100
        score_pen.clear()
        score_pen.write('Score: %s' % score)
       
       #reset invader and player
        bullet.hideturtle()
        bullet.setpos(0, 200)
        invader3.hideturtle()
        time.sleep(1)

        invader3.showturtle()
        x = random.randint(-180,180)
        invader3.setposition(x,180)

        invader_speed=invader_speed+0.65
        ibullet_speed=ibullet_speed+0.3
        
        
    elif abs(bullet.xcor() - invader4.xcor()) < 15 and \
       abs(bullet.ycor() - invader4.ycor()) < 15:
           
        print("\n Invader: \n Was Killed")
           
       # update the score
        score = score + 100
        score_pen.clear()
        score_pen.write('Score: %s' % score)
       
       #reset invader and player
        bullet.hideturtle()
        bullet.setpos(0, 200)
        invader4.hideturtle()
        time.sleep(1)

        invader4.showturtle()
        x = random.randint(-180,180)
        invader4.setposition(x,180)

        invader_speed=invader_speed+0.65
        ibullet_speed=ibullet_speed+0.1
        
        
    # Check if player was hit by invader's bullet
    if abs(ibullet.xcor() - player.xcor()) < 15 and \
       abs(ibullet.ycor() - player.ycor()) < 15:

        time.sleep(1)
        ibullet.setpos(0,-400)
        llife()


    # Check if bullet hit invader's bullet
    if abs(bullet.xcor() - ibullet.xcor()) < 15 and \
       abs(bullet.ycor() - ibullet.ycor()) < 15:
           
        print("\n Player: \n Hit Invader's Bullet")

        ibullet.hideturtle()
        ibullet.setpos(0,-400)

        bullet.hideturtle()
        bullet.setpos(0,400)

        score = score + 200
        score_pen.clear()
        score_pen.write('Score: %s' % score)


    # Check if health bullet collided
    if abs(HealthBullet.xcor() - player.xcor()) < 13 and \
       abs(HealthBullet.ycor() - player.ycor()) < 15:
           
        if life < 10:

            print("\n Player: \n Gained a Life")
            
            life+=1
            
            lscore_pen.clear()
            lscore_pen.write('Lives Left: %s' % life+ ' / 10')
            HealthBullet.setpos(player.xcor(), player.ycor()-30)
            
        else:
            
            # update the score
            score = score + 500
            score_pen.clear()
            score_pen.write('Score: %s' % score)
            HealthBullet.setpos(player.xcor(), player.ycor()-30)
        
        
    #Checking bullet's postion
    
    if ibullet.ycor() <= -190:
        ibullet.hideturtle()
        
        
    if HealthBullet.ycor() <= -190:
        HealthBullet.hideturtle()
        
        
    if bullet.ycor() >= 190:
        bullet.hideturtle()
        
        
    #Random firing
    if  ibullet.ycor() <= -700:
        
        if random.randint(1, 500000) > 250000:
            
            invf=random.randint(1, 4)
            
            if invf==1:
                enemyfire(invader)
                
            elif invf==2:
                enemyfire(invader2)
                
            elif invf==3:
                enemyfire(invader3)
                
            elif invf==4:
                enemyfire(invader4)
    
    
    if  HealthBullet.ycor() <= -1000:
        
        if random.randint(1, 500000) > 499000:
            
            healthFire()
            
##
# Credits:
# Main Game Programmer: Morgan
# Menu Designer: Pablo
# Sprite Designer: Soloman 