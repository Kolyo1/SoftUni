import astronauts.base_astronaut as base

class EngineerAstronaut(base.BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="EngineerAstronaut", stamina=80)

    def train(self):
        stamina_increase = 5
        self.stamina = min(100, self.stamina + stamina_increase)
    