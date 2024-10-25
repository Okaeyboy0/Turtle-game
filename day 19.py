import turtle
import random
import time
import winsound
from turtle import Turtle, Screen

# Setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

# Initialize currency
total_currency = 100
print(f"You have {total_currency} currency.")

# Betting input
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
bet_amount = int(screen.textinput("Bet Amount", f"How much do you want to bet? You have {total_currency} currency: "))

# Validate bet amount
if bet_amount > total_currency:
    print("You don't have enough currency for that bet. Exiting the game.")
    screen.bye()
else:
    total_currency -= bet_amount
    print(f"You placed a bet of {bet_amount} on the {user_bet} turtle. Remaining currency: {total_currency}")

# Create countdown function
def countdown(seconds):
    countdown_turtle = Turtle()
    countdown_turtle.color("white")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(x=0, y=0)

    for i in range(seconds, 0, -1):
        countdown_turtle.clear()
        countdown_turtle.write(i, align="center", font=("Arial", 48, "normal"))
        winsound.Beep(frequency=1000, duration=500)  # Play sound
        time.sleep(1)

    countdown_turtle.clear()

# Create turtles
colors = ["red", "blue", "pink", "orange", "green"]
y_position = [10, 40, 80, -40, -80]
all_turtles = []

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-730, y=y_position[i])
    all_turtles.append(new_turtle)

# Draw finish line
tom = Turtle()
tom.color("white")
tom.pensize(20)
tom.penup()
tom.goto(x=500, y=900)
tom.right(90)
tom.pendown()
tom.forward(1800)

# Start countdown and race
if user_bet:
    countdown(5)
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            rad_dis = random.randint(0, 15)
            turtle.forward(rad_dis)

            if turtle.xcor() > 500:
                is_race_on = False
                winning_color = turtle.pencolor()

                if winning_color == user_bet:
                    winnings = bet_amount * 2
                    total_currency += winnings
                    print(f"Congratulations! The {winning_color} turtle won! You won {winnings}! Your new balance is: {total_currency}")
                else:
                    print(f"Sorry, the {winning_color} turtle won. Your remaining balance is: {total_currency}")

                break

# Final currency balance
print(f"Final currency balance: {total_currency}")
screen.exitonclick()
