import turtle
import math

# weight = 640
# height = 320
# resolution = weight*height
# class Center:
# def Center(self, weight, height):
# self.weight = weight / 2
# self.height = height / 2
v1 = 1
v2 = 4
x = 0
y = 0
R = 100  # pixels
proportion = 0.23
y_coord = (R - (proportion * 100))
r_win = proportion * R


def create_Pool():
    turtle.down()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(R)
    turtle.dot(5, "red")
    turtle.up()


def create_move_Teacher():
    turtle.speed(v2)
    turtle.circle(R)
    turtle.dot(5, "red")
    turtle.up()


def create_move_Student():
    turtle.goto(x, y_coord)
    turtle.down()
    turtle.circle(r_win)
    turtle.dot(5, "blue")
    turtle.up()
    turtle.goto(x, y_coord)
    turtle.down()
    turtle.speed(v1)


def move_Student():
    turtle.circle(r_win, 180)
    turtle.dot(5, "blue")
    turtle.right(90)
    turtle.forward(y_coord)
    turtle.dot(5, "blue")
    turtle.up()


def move_Teacher():
    turtle.goto(x, y)
    turtle.down()
    turtle.right(90)
    turtle.circle(R, 180)
    turtle.dot(5, "red")
    turtle.up()


create_Pool()
create_move_Teacher()
create_move_Student()
move_Student()
move_Teacher()

turtle.mainloop()