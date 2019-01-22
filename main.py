#!/usr/bin/bash
# -*- coding: utf-8 -*
import turtle
import turtleWrap
import warehouse
import Population
import Individual
import random
import copy

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
    data_sample = None #tablica populacji
    input_vector = None
    NUMBER_OF_ITERATIONS = 100

    def __init__(self):
        self.turtleWrapper = turtleWrap.TurtleWrapper()
        self.warehouse = warehouse.Warehouse()
        self.screen = turtle.Screen()
        self.current_position = Point(round(self.warehouse.WIDTH/2), round(self.warehouse.HEIGHT/2))
        self.init_screen()
        self.input_vector = []

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

    #tworzenie magazynu, tworzenie zestawu populacji
    def finish_drawing(self):
        if self.turtleWrapper.drawing_finished:
            self.warehouse.fill_warehouse()
            self.data_sample = [Population.Population(self.input_vector, self.warehouse.matrix) for i in range(100)]

            for population in self.data_sample:
                population.putCargosIntoWarehouse()


    def iteration(self):
        for population in self.data_sample:
            population.evaluateObjectiveFunction(self.warehouse.HEIGHT, self.warehouse.WIDTH)
        print("Po liczeniu funkcji przystosowania")
        self.sort()
        print("po sortowaniu")

        for i in range(50):
            a = random.randrange(0, 50, 1)
            b = random.randrange(0, 50, 1)
            while a == b:
                b = random.randrange(0, 50, 1)

            #for j in range(50):
            self.data_sample.append(self.crossPopulations(self.data_sample[a], self.data_sample[b]))
        print("po krzyżowaniu")
        for population in self.data_sample:
            for cargo in population.individuals:
                cargo.mutate()

            population.warehouse = copy.deepcopy(self.warehouse.matrix)
            population.putCargosIntoWarehouse()
        print("po mutacji")
        #self.print_warehouse()

    def run_iteration(self):
        for i in range(self.NUMBER_OF_ITERATIONS):
            self.iteration()
            print(i)
        self.print_warehouse()

    def print_warehouse(self):
        self.data_sample[0].debug_warehouse_shape()
        for i in range(100):
            print(self.data_sample[i].objectiveFunctionValue)


    #takie tam wczytywanie towarow, nie wiazace    
    def getInput(self):
        for i in range(20):
            self.input_vector.append(1)
            self.input_vector.append(4)
            self.input_vector.append(7)

        for i in range(10):
            self.input_vector.append(2)
            self.input_vector.append(3)
            self.input_vector.append(5)
            self.input_vector.append(6)

    #powinno byc ok, nie sprawdzane, bo nie dziala wpisywanie towarow
    #def reproduce(self):

    def crossPopulations(self, mother, father):
        x = [i for i in range(100)]
        child = Population.Population(x,self.warehouse.matrix)
        
        for k in range(100):
            child.individuals.pop(0)

        for i in range(100):
            crossed_item = Individual.Individual(0)

            crossed_item.cargo = mother.individuals[i].cargo

            a = random.choice(["mother", "father"])
            if a == "mother":
                crossed_item.topLeftCorner_X = mother.individuals[i].topLeftCorner_X
            else:
                crossed_item.topLeftCorner_X = father.individuals[i].topLeftCorner_X
                
            a = random.choice(["mother", "father"])
            if a == "mother":
                crossed_item.topLeftCorner_Y = mother.individuals[i].topLeftCorner_Y
            else:
                crossed_item.topLeftCorner_Y = father.individuals[i].topLeftCorner_Y

            a = random.choice(["mother", "father"])
            if a == "mother":
                crossed_item.isVisible = mother.individuals[i].isVisible
            else:
                crossed_item.isVisible = father.individuals[i].isVisible

            child.individuals.append(crossed_item)
        
        return child


    '''
    tu zaczyna sie jazda bez trzymanki xd
    mapujemy wartosci funkcji celu, do pozycji populacji w naszej probce
    wyciagamy klucz funkcji o najmniejszej wartosci
    przepisujemy te populacje do nowej probki
    usuwamy populacje z mapy
    podmieniamy probki
    '''
    def sort(self):
        value_map = {a: self.data_sample[a].objectiveFunctionValue for a in range(100)}

        new_sample = []
        # 50 best populations
        for i in range(50):
            key = self.keyWithMinValue(value_map)
            new_sample.append(self.data_sample[key])
            value_map.pop(key)
        
        self.data_sample = new_sample


    #najszybsze wyszukiwanie maxa w mapie wg goscia ze stackoverflow, mial dowody
    def keyWithMinValue(self, value_map):
        v = list(value_map.values())
        k = list(value_map.keys())
        return k[v.index(min(v))]

    def start(self):
        self.screen.onkey(self.exit_program, "q")
        self.screen.onkey(self.up_pressed, "Up")
        self.screen.onkey(self.down_pressed, "Down")
        self.screen.onkey(self.left_pressed, "Left")
        self.screen.onkey(self.right_pressed, "Right")
        self.screen.onkey(self.finish_drawing, "k")
        self.screen.onkey(self.start_test_rysowania_cargo, "a")
        self.screen.onkey(self.run_iteration, "i")
        self.screen.onkey(self.print_warehouse, "w")
        #self.screen.onkey(self.reproduce, "space")
        self.screen.listen()
        #self.screen.mainloop() #odrzucało mi to w necie znalazlem ze ma byc tak jak na dole
        turtle.mainloop()

    def start_test_rysowania_cargo(self):
        self.turtleWrapper.drawCargo(0, 0, 50, 100)
        self.turtleWrapper.drawCargo(200, -200, 200, 100)
        self.screen.exitonclick()

    def exit_program(self):
        self.screen.bye()


################# PROGRAM ###################
program = Main()
program.getInput()
program.start()
#program.start_test_rysowania_cargo() #należy wykomentować tylko program.start()