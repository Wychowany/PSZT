import Individual


class Population:

    individuals = []

    def __init__(self) -> None:

        super().__init__()
        self.individuals = Individual.Individual()
