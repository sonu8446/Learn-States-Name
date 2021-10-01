import pandas
import turtle

screen = turtle.Screen()
screen.setup(700, 800)
screen.title("States Of India Game")
image = "blankImage.gif"
screen.addshape(image)
turtle.shape(image)


listOf_X_Cord = [0] * 28
listOf_Y_Cord = [0] * 28
i = 0
states = ["Jammu And Kashmir", "Himachal Pradesh", "Punjab", "Uttarakhand", "Haryana", "Rajasthan", "Gujarat",
          "Madhya Pradesh", "Uttar Pradesh", "Sikkim", "Arunachal Pradesh", "Assam", "Meghalaya", "Nagaland",
          "Manipur", "Mizoram", "Tripura", "West Bengal", "Jharkhand", "Chhattisgarh", "Odisha", "Maharashtra",
          "Telangana", "Goa", "Andhra Pradesh", "Tamil Nadu", "Bihar", "Karnataka"
          ]


def getCoordOnClick(x, y):
    global i
    listOf_X_Cord[i] = x
    listOf_Y_Cord[i] = y
    i += 1


statesAndCoord = {
    "X-axis": listOf_X_Cord,
    "Y-axis": listOf_Y_Cord,
    "States": states
}
turtle.onscreenclick(getCoordOnClick)
turtle.mainloop()
print(statesAndCoord)
df = pandas.DataFrame(statesAndCoord)
df.to_csv("statesAndCo-ordinates.csv", index=False)
