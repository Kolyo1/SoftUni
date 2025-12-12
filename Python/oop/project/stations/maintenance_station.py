import stations.base_station as base


class MaintenanceStation(base.BaseStation):
    def __init__(self, name: str):
        super().__init__(name, capacity=3)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization == "EngineerAstronaut" and a.salary <= min_value:
                a.salary = float(a.salary) + 3000.0