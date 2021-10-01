"""import json
import pandas
import csv
with open("WeatherData.csv") as dataFile:
    data = csv.reader(dataFile)
    temperature = []
    for i in data:
        if i[1] != "temp":
            temperature.append(int(i[1]))
######################################################################################################
data = pandas.read_csv("WeatherData.csv")
print(data["temp"])
dataDict = data.to_dict()
print(dataDict)
temperatureList = data["temp"].to_list()
averageTemperature = sum(temperatureList)/len(temperatureList)

maxTempData = data[data.temp == data.temp.max()]
tempInFehrenheit = float((maxTempData.temp*1.8)+32)
print(tempInFehrenheit)

squirrelData = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grayColor = sum(squirrelData["Primary Fur Color"] == "Gray")
cinnamonColor = sum(squirrelData["Primary Fur Color"] == "Cinnamon")
blackColor = sum(squirrelData["Primary Fur Color"] == "Black")
print(grayColor)
print(cinnamonColor)
print(blackColor)


dataOutput = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "NumberOfCount": [grayColor, cinnamonColor, blackColor]
}

df = pandas.DataFrame(dataOutput)
df.to_csv("outputData")
"""
#######################################################################################################################
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

while count < 28:
    answer = screen.textinput(title="Guess the State"+str(count)+"/28", prompt="Enter Name Of State")
    answer = answer.title()
    if answer in allStates:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.States == answer]
        t.goto(float(stateData.X_axis), float(stateData.Y_axis))
        t.write(arg=answer)
        allStates.remove(answer)
        print(allStates)
        count += 1

screen.exitonclick()

