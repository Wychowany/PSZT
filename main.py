import turtle
import turtleWrap
import warehouse


class Main:

    turtleWrapper = None
    warehouse = None
    screen = None

    def __init__(self):
        self.turtleWrapper = turtleWrap.TurtleWrapper()
        self.warehouse = warehouse.Warehouse()
        self.screen = turtle.Screen()
        self.init_screen()

    def init_screen(self):
        self.screen = turtle.Screen()
        self.screen.setup(1000, 1000)
        self.screen.title("Algorytm ewolucyjny")

    def up_pressed(self):
        self.turtleWrapper.move_up()

    def down_pressed(self):
        self.turtleWrapper.move_down()

    def left_pressed(self):
        self.turtleWrapper.move_left()

    def right_pressed(self):
        self.turtleWrapper.move_right()

    def start(self):
        self.screen.onkey(self.exit_program, "q")
        self.screen.onkey(self.up_pressed, "Up")
        self.screen.onkey(self.down_pressed, "Down")
        self.screen.onkey(self.left_pressed, "Left")
        self.screen.onkey(self.right_pressed, "Right")
        self.screen.listen()
        self.screen.mainloop()

    def exit_program(self):
        self.screen.bye()


################# PROGRAM ###################

program = Main()
program.start()
