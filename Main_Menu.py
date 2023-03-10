#set up window
import turtle
import tkinter

wn = turtle.Screen()
wn.setup(width = 540,height = 540)
wn.bgcolor('lightgreen')

#background

wn.title("Planet Invaders")
style = ('Arial', 45, 'normal')
Style = ('Arial', 20, 'normal')

#title text and button to navigate to level, credits, and how to play the game

turtle.hideturtle()
turtle.up()
turtle.goto(0,180)
turtle.down()
turtle.write("Planet Invaders", font=style, align="center")

def play():
    turtle.clear()
    Play_Button.destroy()
    import Planet_Invaders

Play_Button = tkinter.Button(text ="Play!", command = play)

Play_Button.place(x = 500, y = 500)

turtle.mainloop()

