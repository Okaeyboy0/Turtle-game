import turtle
import random
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
is_race_on = False
screen.setup(width=500, height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?, Enter a colour: ")
print(user)
colors = ["red", "blue", "pink", "orange", "green"]
y_position = [10, 40, 80, -40, -80]
all_turtle = []
for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)
if user:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        rad_dis = random.randint(a=0, b=10)
        turtle.forward(rad_dis)


        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()


            if winning_color == user:
                print(f"Congratulations! The {winning_color} turtle won!")
            else:
                print(f"Sorry, the {winning_color} turtle won. Better luck next time!")

            break

screen.exitonclick()