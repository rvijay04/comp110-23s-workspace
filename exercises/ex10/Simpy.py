"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730555483"


class Simpy:
    """Simpy Class."""

    values: list[float]

    def __init__(self, values: list[float]):
        """Initializing constructer."""
        self.values = values

    def __str__(self):
        """Str method."""
        return f"Simpy({str(self.values)})"

    def fill(self, value: float, num: float):
        """Fill method."""
        self.values = [value] * num

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Arange method."""
        assert step != 0.0
        value: float = start
        while value != stop:
            self.values.append(value)
            value += step

    def sum(self) -> float:
        """Sum method."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add method."""
        result: Simpy = Simpy([])
        if isinstance (rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(rhs.values[i] + self.values[i])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Pow method."""
        if isinstance(rhs, float):
            return Simpy([x ** rhs for x in self.values])
        else:
            assert len(self.values) == len(rhs.values)
            return Simpy([x ** y for x, y in zip(self.values, rhs.values)])
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Eq method."""
        new_list: list[bool] = []
        result: Simpy = Simpy([])
        if isinstance (rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(rhs.values[i] == self.values[i])
        return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than method."""
        new_list: list[bool] = []
        result: Simpy = Simpy([])
        if isinstance (rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] > rhs.values[i])
        return new_list
    
    def __getitem__(self, rhs: int) -> float:
        """Subscription notation operator overload."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new_list: Simpy = Simpy([])
            for i in range(len(self.values)):
                new_list.values.append(self.values[i])
            return new_list