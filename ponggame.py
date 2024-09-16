# import the modull
import turtle

win=turtle.Screen()#intialize screen
win.bgcolor("black")#set the background color of the window 
win.title("Ping Pong BY Abokamer")#set the title of the window 
win.setup(width=800,height=600)#set the width and heirht of the window 
win.tracer(0)#stops the window from updating automatically

# madrab1
madrab1=turtle.Turtle()# intialize tutle object (shape)
madrab1.speed(0)#set the speed of the animation
madrab1.shape("square")#set the shape of the object 
madrab1.color("blue")#set the color of the shape
madrab1.shapesize(stretch_wid=5,stretch_len=1)# streches the shape to meet the size 
madrab1.penup()# stops the object from drawing lines 
madrab1.goto(-350,0)# set the position of the object 


# madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)

# ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.4
ball.dy=0.4
# score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0  Player 2: 0 ",align="center",font=("Courier",24,"normal") )
#functions 
def madrab1_up():
    if madrab1.ycor() ==260 :
        madrab1.sety(260)
    else:
        madrab1.sety(madrab1.ycor()+20)

def madrab1_down():
    if madrab1.ycor()==-260:
        madrab1.sety(-260)
    else:
        madrab1.sety(madrab1.ycor()-20)

def madrab2_up():
    if madrab2.ycor() in(300,260) :
        madrab2.sety(260)
    else:
        madrab2.sety(madrab2.ycor()+20)

def madrab2_down():
    if madrab2.ycor()in(-260,-300):
        madrab2.sety(-260)
    else:
        madrab2.sety(madrab2.ycor()-20)

#key board binding 
win.listen()
win.onkeypress(madrab1_up,"w")
win.onkeypress(madrab1_down,"s")
win.onkeypress(madrab2_up,"Up")
win.onkeypress(madrab2_down,"Down")


t = turtle.Turtle()
t.color("white")
t.penup()
t.goto(0, 300)
t.pendown()
t.setheading(270)  # Point downwards
t.forward(600)  # Draw the vertical line (600 units)
t.hideturtle()



#main game loop
while True:
    win.update()# updates the screen every time the game
    #move the ball
    ball.setx(ball.xcor()+ball.dx)#ball starts at 0 and every time loops run ---> + 0.3 x axis 
    ball.sety(ball.ycor()+ball.dy)#ball starts at 0 and every time loops run ---> + 0.3 y axis 
    #border check , top border + 300px ,bottom border -300px ,ball is 20 px 
    if ball.ycor ()>290:#if ball is at top border 
        ball.sety(290)#set Y coordinate +290
        ball.dy *=-1 #reverse direction 

    if ball.ycor ()<-290:# if ball is at bottom
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() >390:# if is at right border
        ball.goto (0,0)# return ball to center 
        ball.dx *=-1# reverse the xdirection 
        score1 +=1
        score.clear()
        score.write(f"Player 1: {score1}  Player 2: {score2} ",align="center",font=("Courier",24,"normal") )


    if ball.xcor() <-390:# if is at left  border
        ball.goto (0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write(f"Player 1: {score1}  Player 2: {score2} ",align="center",font=("Courier",24,"normal") )

    # tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() <350 and ball.ycor() < madrab2.ycor()+40 and ball.ycor() > madrab2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
    
    if (ball.xcor() < -340 and ball.xcor() >-350 and ball.ycor() < madrab1.ycor()+40 and ball.ycor() > madrab1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
    
    if score2 == 10 or score1 == 10:
        win.clear()  # Clear the current game window
        new_win = turtle.Screen()  # Create a new window
        new_win.bgcolor("black")  # Set the background color of the new window
        new_win.title("Ping Pong BY Abokamer")  # Set the title of the window
        new_win.setup(width=800, height=600)  # Set the width and height of the new window

        string = turtle.Turtle()  # Initialize a new turtle object for the end message
        string.color("white")
        string.penup()
        string.hideturtle()  # Hide the turtle object to show only the text
        string.goto(0, 0)

        winner = "Player 1" if score1 == 10 else "Player 2"
        string.write(f"END THE GAME - {winner} WINS", align="center", font=("Courier", 24, "bold"))

        sgin = turtle.Turtle()  # Initialize a new turtle object for the end message
        sgin.color("red")
        sgin.penup()
        sgin.hideturtle()  # Hide the turtle object to show only the text
        sgin.goto(-360, -260)

        sgin.write("BY Abokamer", font=("Courier", 24, "bold"))

        new_win.update()  # Update the new window
        new_win.mainloop()  # Keep the new window open

