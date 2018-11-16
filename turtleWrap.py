import turtle


class TurtleWrapper:

    tut = None
    previous_key = None

    def __init__(self):
        self.tut = turtle.Turtle()
        self.tut.speed(0) # prevents delays

    def move_forward_and_add_vertex(self):
        self.tut.forward(50)
        # warehouse.vertices.insert(len(warehouse.vertices), tut.pos())

    def move_up(self):
        if self.previous_key == "DOWN":
            return
        else:
            self.turn_north()
            self.move_forward_and_add_vertex()
            self.previous_key = "UP"

    def move_down(self):
        if self.previous_key == "UP":
            return
        else:
            self.turn_south()
            self.move_forward_and_add_vertex()
            self.previous_key = "DOWN"

    def move_right(self):
        if self.previous_key == "LEFT":
            return
        else:
            self.turn_east()
            self.move_forward_and_add_vertex()
            self.previous_key = "RIGHT"

    def move_left(self):
        if self.previous_key == "RIGHT":
            return
        else:
            self.turn_west()
            self.move_forward_and_add_vertex()
            self.previous_key = "LEFT"

    def turn_north(self):
        self.tut.setheading(90)

    def turn_south(self):
        self.tut.setheading(270)

    def turn_east(self):
        self.tut.setheading(0)

    def turn_west(self):
        self.tut.setheading(180)


    def write_hellow_message(self):
        self.tut.penup()
        self.tut.goto(0, 50)
        self.tut.write("Draw the warehouse", False, "left", font=("Arial", 50, "normal"))
        self.tut.goto(250,250)
