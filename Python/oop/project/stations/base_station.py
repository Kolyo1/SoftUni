import re
from typing import List
import astronauts.base_astronaut as base
from abc import ABC, abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        name = name.strip()
        if name == "" or not re.fullmatch(r"[A-Za-z0-9-]+", name):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")

        self.name = name

        if capacity < 0:
            raise ValueError("A station cannot have a negative capacity!")

        self.capacity = int(capacity)
        self.astronauts: List[base.BaseAstronaut] = []

    def calculate_total_salaries(self) -> str:
        total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self) -> str:
        if not self.astronauts:
            astronauts_part = "N/A"
        else:
            ids = sorted(a.id_number for a in self.astronauts)
            astronauts_part = " #".join(ids)

        total_salaries = self.calculate_total_salaries()

        return f"Station name: {self.name}; Astronauts: {astronauts_part}; Total salaries: {total_salaries}"

    @abstractmethod
    def update_salaries(self, min_value: float):
        """Update salaries for assigned astronauts according to station rules."""
        raise NotImplementedError()
