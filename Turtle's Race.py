import random
import turtle
from turtle import Turtle, Screen
# ---------- Third lesson ----------
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race? \nEnter a color from the following options: \n red / orange / yellow / green / blue / purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -65, -30, 5, 40, 75, 110]

all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True  # MAKE the game start only after the user has a bet .

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:  # GAME OVER - one turtle has won
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've Won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)  # making the turtles walk a random distance in a rang of 10
        turtle.forward(rand_distance)


screen.exitonclick()
