import turtle
import turtleWrap
import warehouse
import Population


class Point:
    index_x = None
    index_y = None

    def __init__(self, x, y):
        self.index_x = x
        self.index_y = y


class Main:

    turtleWrapper = None
    warehouse = None
    screen = None
    current_position = None
    population = None

    def __init__(self):
        self.turtleWrapper = turtleWrap.TurtleWrapper()
        self.warehouse = warehouse.Warehouse()
        self.screen = turtle.Screen()
        self.current_position = Point(round(self.warehouse.WIDTH/2), round(self.warehouse.HEIGHT/2))
        self.init_screen()

    def init_screen(self):
        self.screen = turtle.Screen()
        self.screen.setup(1000, 1000)
        self.screen.title("Algorytm ewolucyjny")

    def up_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_up():
            self.warehouse.set_way_on_matrix_when_moving_up()

    def down_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_down():
            self.warehouse.set_way_on_matrix_when_moving_down()

    def left_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_left():
            self.warehouse.set_way_on_matrix_when_moving_left()

    def right_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_right():
            self.warehouse.set_way_on_matrix_when_moving_right()

    def finish_drawing(self):
        if self.turtleWrapper.drawing_finished:
            self.warehouse.fill_warehouse()
            self.population = Population.Population(self.warehouse.matrix)

    def reproduce(self):
        print("reproducing!!!")

    def start(self):
        self.screen.onkey(self.exit_program, "q")
        self.screen.onkey(self.up_pressed, "Up")
        self.screen.onkey(self.down_pressed, "Down")
        self.screen.onkey(self.left_pressed, "Left")
        self.screen.onkey(self.right_pressed, "Right")
        self.screen.onkey(self.finish_drawing, "k")
        self.screen.onkey(self.reproduce, "space")
        self.screen.listen()
        self.screen.mainloop()

    def exit_program(self):
        self.screen.bye()


################# PROGRAM ###################
program = Main()
program.start()
