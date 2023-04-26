"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int = 0
    hunger_score: int = 0

    def __init__(self):
        """Initializing method."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Age and hunger score."""
        self.age += 1
        self.hunger_score -= 1
    
    def eat(self, num_fish: int):
        """Adding how much fish bear ate."""
        self.hunger_score += num_fish

    
