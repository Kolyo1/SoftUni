import astronauts.base_astronaut as base


class ScientistAstronaut(base.BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization="ScientistAstronaut", stamina=70)

    def train(self):
        stamina_increase = 3
        self.stamina = min(100, self.stamina + stamina_increase)
    