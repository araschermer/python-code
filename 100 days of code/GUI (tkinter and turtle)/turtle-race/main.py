from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
valid_choice = False
colors = ["red", "green", "blue", "purple", "orange", "yellow", "black"]
# take a valid bet input from the user
user_ber=""
while not valid_choice:
    user_bet = screen.textinput(title = "Make your bet",
                                prompt = f"Which turtle will win the race? Enter a color: from this list: {colors} ").lower()
    if user_bet not in colors:
        continue
    else:
        valid_choice = True
# starting position is to the left of the current screen setup
x_starting_position = -230
y_starting_position = -150
turtles = []
for number in range(len(colors)): # create a  number of turtles of distinct colors
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[number])
    new_turtle.goto(x = x_starting_position, y = y_starting_position)
    y_starting_position += 50 # space between the turtles
    turtles.append(new_turtle) # add the new turtle to the list of turtles

race_on = True
winner = ""
while race_on:
    for new_turtle in turtles:
        new_turtle.forward(randint(0, 10))
        if new_turtle.xcor() > 230: # the race if on, till one turtle reaches the end of the screen (finish line)
            race_on = False
            winner = new_turtle.pencolor()
if winner == user_bet:
    print(f"\n\nYou won! The {winner} turtle is the winner!")
else:
    print(f"\n\nYou lost!\n\nyou bet on the {user_bet} turtle, but The {winner} turtle is the winner!")

screen.exitonclick()
