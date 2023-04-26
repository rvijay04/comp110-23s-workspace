"""File to define River class."""

__author__ = "730555483"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class."""
    day: int = 0
    bears: list[Bear] = []
    fish: list[Fish] = []
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking age."""
        new_listf: list[Fish] = []
        for elem in self.fish:
            if elem.age <= 3:
                new_listf.append(elem)
        self.fish = new_listf
        new_listb: list[Bear] = []
        for elem in self.bears:
            if elem.age <= 5:
                new_listb.append(elem)
        self.bears = new_listb

    def remove_fish(self, amount: int):
        """Removing fish."""
        for elem in range(amount):
            self.fish.pop(0)

    def bears_eating(self):
        """Bear eating."""
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                elem.eat(3)
    
    def check_hunger(self):
        """Checking hunger."""
        new_list: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:
                new_list.append(elem)
        self.bears = new_list
        
    def repopulate_fish(self):
        """Repopulating fish."""
        new_fish = []
        for i in range(len(self.fish) // 2):
            for j in range(4):
                new_fish.append(Fish())
        self.fish += new_fish

    def repopulate_bears(self):
        """Repopulating bears."""
        num_bears = len(self.bears)
        new_bears = num_bears // 2
        for i in range(new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)
    
    def view_river(self):
        """Viewing river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One river week."""
        for i in range(7):
            self.one_river_day()