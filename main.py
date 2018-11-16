import turtle

wn = turtle.Screen()
wn.title("Handling keypresses!")
tut = turtle.Turtle()
previous_key = ""
def move_up():
    if previous_key == "DOWN":
        return
    else:
        tut.setheading(90)
        tut.forward(50)


def move_down():
    if previous_key == "DOWN":
        return
    else:
        tut.setheading(270)
        tut.forward(50)


def move_right():
    if previous_key == "DOWN":
        return
    else:
        tut.setheading(0)
        tut.forward(50)


def move_left():
    if previous_key == "DOWN":
        return
    else:
        tut.setheading(180)
        tut.forward(50)

def exit_program():
    wn.bye()


wn.onkey(move_up, "Up")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_down, "Down")
wn.onkey(exit_program, "q")
wn.listen()
wn.mainloop()
