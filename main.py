#!/usr/bin/bash
# -*- coding: utf-8 -*
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
    data_sample = None #tablica populacji
    input_vetor = []

    def __init__(self):
        self.turtleWrapper = turtleWrap.TurtleWrapper()
        self.warehouse = warehouse.Warehouse()
        self.screen = turtle.Screen()
        self.current_position = Point(round(self.warehouse.WIDTH/2), round(self.warehouse.HEIGHT/2))
        self.init_screen()
        input_vector = []

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
            self.data_sample = [Population.Population(self.input_vetor, self.warehouse.matrix) for i in range(100)]

            #^^^ do tego momentu dziala
            for population in self.data_sample:
                population.putCargosIntoWarehouse()

    #takie tam wczytywanie towarow, nie wiazace    
    def getInput(self):
        counter = 0
        print("Input amount of cargos (truncated at 100)")
        
        user_input = input("Number of small squares:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(1)
            counter = counter+1

        user_input = input("Number of vertical small rectangles:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(2)
            counter = counter+1

        user_input = input("Number of horizontal small rectangles:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(3)
            counter = counter+1

        user_input = input("Number of medium squares:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(4)
            counter = counter+1

        user_input = input("Number of vertical medium rectangles:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(5)
            counter = counter+1

        user_input = input("Number of horizontal medium rectangles:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(6)
            counter = counter+1

        user_input = input("Number of big squares:")
        for i in range(int(user_input)):
            if counter >= 100:
                break
            self.input_vetor.append(7)
            counter = counter+1
        
        while counter < 100:
            self.input_vetor.append(1)
            counter = counter+1

    #powinno byc ok, nie sprawdzane, bo nie dziala wpisywanie towarow
    def reproduce(self):
        for population in self.data_sample:
            population.evaluateObjectiveFunction(self.warehouse.height, self.warehouse.width)

        self.sort()

        for i in range(50):
            a = random.random(0, 50, 1)
            b = random.random(0, 50, 1)
            while a == b:
                b = random.random(0, 50, 1)
            
            for j in range(50):
                self.data_sample.append(self.crossPopulations(self.data_sample[a], self.data_sample[b]))

        for population in self.data_sample:
            for cargo in population.individuals:
                cargo.mutate()

            population.warehouse = self.warehouse.matrix
            population.putputCargosIntoWarehouse()

        

    def crossPopulations(self, mother, father):
        x = []
        child = Population.Population(x)
        for i in range(100):
            crossed_item = Individual.Individual(0)

            crossed_item.cargo = mother[i].cargo

            a = choice(["mother","father"])
            if a == "mother":
                crossed_item.topLeftCorner_X = mother[i].topLeftCorner_X
            else:
                crossed_item.topLeftCorner_X = father[i].topLeftCorner_X
                
            a = choice(["mother","father"])
            if a == "mother":
                crossed_item.topLeftCorner_Y = mother[i].topLeftCorner_Y
            else:
                crossed_item.topLeftCorner_Y = father[i].topLeftCorner_Y

            a = choice(["mother","father"])
            if a == "mother":
                crossed_item.isVisible = mother[i].isVisible
            else:
                crossed_item.isVisible = father[i].isVisible

            child.append(crossed_item)
        
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
            key = value_map[self.keyWithMinValue(value_map)]
            new_sample.append(key)
            new_sample.pop(key)
        
        self.data_sample = new_sample


    #najszybsze wyszukiwanie maxa w mapie wg goscia ze stackoverflow, mial dowody
    def keyWithMinValue(self,value_map):
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
        #self.screen.onkey(self.reproduce, "space")
        self.screen.listen()
        #self.screen.mainloop() odrzucało mi to w necie znalazlem ze ma byc tak jak na dole
        turtle.mainloop()

    def exit_program(self):
        self.screen.bye()


################# PROGRAM ###################
program = Main()
program.getInput()
program.start()