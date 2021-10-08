import turtle
import pandas
screen = turtle.Screen()
screen.setup(700, 800)
screen.title("States Of India Game")
image = "blankImage.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
data = pandas.read_csv("statesAndCo-ordinates.csv")
allStates = data["States"].to_list()
numberOfStates = 29
while count < numberOfStates:
    answer = screen.textinput(title="Guess the State"+str(count)+"/29", prompt="Enter Name Of State").title()
    answer = answer.title()
    if answer == "Exit":
        statesToLearn = pandas.DataFrame(allStates)
        print(statesToLearn)
        statesToLearn.to_csv("statesToLearn.csv")
        break
    if answer in allStates:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.States == answer]
        t.goto(float(stateData.X_axis), float(stateData.Y_axis))
        t.write(stateData.States.item())
        allStates.remove(answer)
        print(stateData)
        count += 1
screen.exitonclick()
