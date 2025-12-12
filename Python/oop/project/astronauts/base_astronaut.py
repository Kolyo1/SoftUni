from abc import ABC, abstractmethod


class BaseAstronaut(ABC):
    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        id_number = id_number.strip()
        if id_number == "" or not id_number.isdigit():
            raise ValueError("ID can contain only digits!")

        self.id_number = id_number

        if salary < 0.0:
            raise ValueError("Salary must be a positive number!")

        self.salary = float(salary)

        if specialization is None or specialization.strip() == "":
            raise ValueError("Specialization cannot be empty!")

        self.specialization = specialization.strip()

        if stamina < 0 or stamina > 100:
            raise ValueError("Stamina is out of range!")

        self.stamina = int(stamina)

    @abstractmethod
    def train(self):
        """Increase astronaut stamina for one training session.

        Concrete astronaut types must implement this method and ensure stamina
        does not exceed 100.
        """
        raise NotImplementedError()