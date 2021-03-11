import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_map.gif"
ALIGNMENT = 'center'
FONT = ("Courier-Bold", 15, "normal")
screen.addshape(image)
turtle.shape(image)
guessed_states = []
states_data = pd.read_csv("us_states.csv")
all_states = states_data.state.to_list()

while len(guessed_states) < 50:
    answer = screen.textinput(title = f"{len(guessed_states)}/50 State correct",
                              prompt = "Guess a state's name").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv", index = False)
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_state_data = states_data[states_data.state == answer]
        t.goto(int(correct_state_data.x), int(correct_state_data.y))
        t.write(answer,font = FONT, align = ALIGNMENT)
screen.mainloop()