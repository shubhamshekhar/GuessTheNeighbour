import turtle
from turtle import Screen
from tkinter import PhotoImage
import pandas


def get_mouse_click_coord(x, y):
    print(x, y)


if __name__ == '__main__':
    screen = Screen()
    screen.title("Guess the Country")
    image = "world_map.gif"
    data = pandas.read_csv("countries.csv")
    larger = PhotoImage(file=image).subsample(1, 1)
    screen.addshape("larger", turtle.Shape("image", larger))
    tortoise = turtle.Turtle("larger")
    screen.setup(width=1.0, height=1.0)
    tortoise.stamp()

    turtle.onscreenclick(get_mouse_click_coord)
    country_list = []
    for country in data.countries:
        country_list.append(country.lower())
    guessed_country = []
    while len(guessed_country) < 7:
        answer_country = screen.textinput(f"{len(guessed_country)}/7 countries correct",
                                          prompt="What's another neighbouring country?").title()
        if answer_country == "Exit":
            break
        if answer_country is not None and answer_country.lower() in country_list:
            country = data[data.countries == answer_country.lower()]
            tortoise.penup()
            tortoise.goto(int(country.x), int(country.y))
            tortoise.pendown()
            tortoise.write(answer_country)
            guessed_country.append(answer_country)
    turtle.mainloop()

    #screen.exitonclick()
