"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int = 0

    def __init__(self):
        """Constructer method."""
        self.age = 0
    
    def one_day(self):
        """One day."""
        self.age += 1
    