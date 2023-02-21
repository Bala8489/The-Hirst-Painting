# import colorgram
#
# colors = colorgram.extract("image.jpg", 15)
#
# # print(colors)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     colors_list.append(new_tuple)


import turtle as t

import random

t.colormode(255)

color_list = [(229, 243, 249), (244, 230, 73), (195, 10, 67), (212, 156, 90), (20, 117, 173), (166, 170, 29),
              (107, 179, 208),
              (217, 131, 165), (161, 74, 31), (237, 72, 34), (27, 138, 72), (126, 181, 144)]

timmy = t.Turtle()

timmy.penup()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()
no_of_dots = 100

for no_of_dots in range(1, no_of_dots + 1):
    timmy.color(random.choice(color_list))
    timmy.begin_fill()
    timmy.circle(20)
    timmy.end_fill()
    timmy.forward(50)

    if no_of_dots % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
