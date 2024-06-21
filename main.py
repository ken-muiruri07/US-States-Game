import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

score = 0
guess_again = True
correct_guesses = []
state_data = pandas.read_csv("50_states.csv")
states = state_data["state"].to_list()
while guess_again and score < 50:
    turtle.shape(image)
    answer = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state name?").title()
    print(answer)
    if answer == "Exit":
        break

    if answer in states:
        score += 1
        guess_again = True
        correct_guesses.append(answer)
        print(correct_guesses)
        correct_answer = state_data[state_data.state == answer]
        states.remove(answer)

        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        xcor = correct_answer.x
        ycor = correct_answer.y
        text.goto(int(xcor), int(ycor))
        text.write(f"{answer}", font=("arial", 8, "normal"))

    if score == 50:
        screen.textinput(title="You did it!", prompt="You did it!")

print(states)
new_data = pandas.DataFrame(states)
new_data.to_csv("New_states_to_learn")



