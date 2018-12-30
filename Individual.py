class Individual:

    coverage = None  # pokrycie magazynu
    matrix = None

    def __init__(self, matrix) -> None:
        super().__init__()
        self.matrix = matrix
