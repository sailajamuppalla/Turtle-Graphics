from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed("normal")

colors = ["medium blue", "dark magenta", "dark red", "Dark green", "green yellow"]
angle = [0, 90, 180, 270]
#distance = ["5", "10", "15", "20", "25"]


for _ in range(75):
    tim.color(random.choice(colors))
    tim.forward(20)
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()