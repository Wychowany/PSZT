import turtle
import warehouse


class TurtleWrapper:
    tut = None
    previous_key = None
    starting_position = None  # Wspolrzedne
    current_position = None          # Indeksy
    drawing_finished = False
    possible_finish_coordinates = [[0, 0], [0, -0], [-0, 0], [-0, -0]]

    def __init__(self):
        self.tut = turtle.Turtle()
        self.tut.speed(0)  # prevents delays
        self.starting_position = self.tut.pos()
        self.current_position = Point(warehouse.Warehouse.WIDTH/2, warehouse.Warehouse.HEIGHT/2)

    def move_forward(self):
        if self.drawing_finished is False:
            self.tut.forward(50)
            if self.get_current_position() in self.possible_finish_coordinates:
                print("KONIEC RYSOWANIA")
                self.drawing_finished = True

    def move_up(self):
        if self.previous_key == "DOWN":
            return False
        else:
            self.turn_north()
            self.move_forward()
            self.previous_key = "UP"
            return True

    def move_down(self):
        if self.previous_key == "UP":
            return False
        else:
            self.turn_south()
            self.move_forward()
            self.previous_key = "DOWN"
            return True

    def move_right(self):
        if self.previous_key == "LEFT":
            return False
        else:
            self.turn_east()
            self.move_forward()
            self.previous_key = "RIGHT"
            return True

    def move_left(self):
        if self.previous_key == "RIGHT":
            return False
        else:
            self.turn_west()
            self.move_forward()
            self.previous_key = "LEFT"
            return True

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
        self.tut.goto(250, 250)

    def get_turtle_x(self):
        return self.current_position.x

    def get_turtle_y(self):
        return self.current_position.y

    def get_current_position(self):
        return [int(round(self.tut.pos()[0])), int(round(self.tut.pos()[1]))]

    def drawCargo(self, x_corner, y_corner, width, height):
        self.tut.penup()
        self.tut.goto(x_corner, y_corner)
        self.turn_east()
        self.tut.pendown()
        self.tut.forward(width)
        self.turn_south()
        self.tut.forward(height)
        self.turn_west()
        self.tut.forward(width)
        self.turn_north()
        self.tut.forward(height)


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


