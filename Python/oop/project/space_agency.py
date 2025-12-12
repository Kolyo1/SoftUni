import astronauts.base_astronaut as baseAstronaut
import stations.base_station as baseStation

class SpaceAgency:
    def __init__(self):
        self.astronauts: list[baseAstronaut.BaseAstronaut]  = []
        self.stations: list[baseStation.BaseStation] = []  # Fixed typo

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        import astronauts.engineer_astronaut as engineerAstronaut
        import astronauts.scientist_astronaut as scientistAstronaut
        astronaut_classes = {
            "EngineerAstronaut": engineerAstronaut.EngineerAstronaut,
            "ScientistAstronaut": scientistAstronaut.ScientistAstronaut
        }

        if astronaut_type not in astronaut_classes:
            raise ValueError("Invalid astronaut type!")
        
        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")
        
        self.astronauts.append(astronaut_classes[astronaut_type](astronaut_id_number, astronaut_salary))
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."
    
    def add_station(self, station_type: str, station_name: str):
        import stations.maintenance_station as maintenanceStation
        import stations.research_station as researchStation
        station_classes = {
            "MaintenanceStation": maintenanceStation.MaintenanceStation,
            "ResearchStation": researchStation.ResearchStation
        }

        if station_type not in station_classes:
            raise ValueError("Invalid station type!")
        
        if any(s.name == station_name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")
        
        self.stations.append(station_classes[station_type](station_name))
        return f"{station_name} is successfully added as a {station_type}."
    
    def assign_astronaut(self, station_name: str, astronaut_type: str):
        if not any(s.name == station_name for s in self.stations):
            raise ValueError(f"Station {station_name} does not exist!")

        # Find available astronaut of the given type (not already assigned to a station)
        available_astronauts = [a for a in self.astronauts if a.specialization == astronaut_type]
        if not available_astronauts:
            raise ValueError(f"No available astronauts of the type!")
        
        station = next(s for s in self.stations if s.name == station_name)
        if station.capacity <= 0:
            return "This station has no available capacity."

        # Take the first available astronaut
        astronaut = available_astronauts[0]

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1

        return f"{astronaut.id_number} was assigned to {station_name}."
    
    def train_astronauts(self, station: baseStation.BaseStation, sessions_number: int):
        if not isinstance(sessions_number, int) or sessions_number < 0 or sessions_number > 3:
            raise ValueError("sessions_number must be an integer in range [0..3]")

        for astronaut in station.astronauts:
            for _ in range(sessions_number):
                astronaut.train()

        total_stamina = sum(a.stamina for a in station.astronauts)
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: baseStation.BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)

        if astronaut is None or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1

        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float) -> str:
        if min_value < 0:
            raise ValueError("Minimum value cannot be negative!")

        for station in self.stations:
            station.update_salaries(min_value)

        available_astronauts_count = len(self.astronauts)
        stations_total_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations)

        stations_sorted = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        lines = ["*Space Agency Up-to-Date Report*"]
        lines.append(f"Total number of available astronauts: {available_astronauts_count}")
        lines.append(f"**Stations count: {stations_total_count}; Total available capacity: {total_available_capacity}**")

        for station in stations_sorted:
            lines.append(station.status())

        return "\n".join(lines)
    
# Create an instance of the Space Agency Manager 
manager = SpaceAgency() 
 
# Add astronauts (engineers & scientists) 
print(manager.add_astronaut("EngineerAstronaut", "02345", 780_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "1234", 500_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "789123", 800_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "45678999", 702_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "321654", 401_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "6543211", 490_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "334654", 600_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "034654", 395_000.0)) 
print() 
 
# Add stations 
print(manager.add_station("MaintenanceStation", "Lunar-Base")) 
print(manager.add_station("ResearchStation", "ISS-3")) 
print(manager.add_station("ResearchStation", "Mars-Habitat")) 
print() 
 
# Assign astronauts to stations 
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut")) 
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut")) 
print(manager.assign_astronaut("Lunar-Base", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut")) 
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut")) 
print() 
 
# Conduct training sessions 
print(manager.train_astronauts(manager.stations[0], 0)) 
print(manager.train_astronauts(manager.stations[0], 1)) 
print(manager.train_astronauts(manager.stations[0], 2)) 
print(manager.train_astronauts(manager.stations[0], 3)) 
print(manager.train_astronauts(manager.stations[0], 3)) 
print(manager.train_astronauts(manager.stations[1], 0)) 
print(manager.train_astronauts(manager.stations[2], 1)) 
# Create an instance of the Space Agency Manager 
manager = SpaceAgency() 
 
# Add astronauts (engineers & scientists) 
print(manager.add_astronaut("EngineerAstronaut", "02345", 780_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "1234", 500_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "789123", 800_000.0)) 
print(manager.add_astronaut("EngineerAstronaut", "45678999", 702_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "321654", 401_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "6543211", 490_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "334654", 600_000.0)) 
print(manager.add_astronaut("ScientistAstronaut", "034654", 395_000.0)) 
print() 
 
# Add stations 
print(manager.add_station("MaintenanceStation", "Lunar-Base")) 
print(manager.add_station("ResearchStation", "ISS-3")) 
print(manager.add_station("ResearchStation", "Mars-Habitat")) 
print() 
 
# Assign astronauts to stations 
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut")) 
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut")) 
print(manager.assign_astronaut("Lunar-Base", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut")) 
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut")) 
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut")) 
print() 
 
# Conduct training sessions 
print(manager.train_astronauts(manager.stations[0], 0)) 
print(manager.train_astronauts(manager.stations[0], 1)) 
print(manager.train_astronauts(manager.stations[0], 2)) 
print(manager.train_astronauts(manager.stations[0], 3)) 
print(manager.train_astronauts(manager.stations[0], 3)) 
print(manager.train_astronauts(manager.stations[1], 0)) 
print(manager.train_astronauts(manager.stations[2], 1)) 
print() 
 
# Retire an astronaut 
print(manager.retire_astronaut(manager.stations[2], "334654")) 
print(manager.retire_astronaut(manager.stations[0], "02345")) 
print(manager.stations[0].astronauts[0].id_number, manager.stations[0].astronauts[0].stamina) 
print(manager.retire_astronaut(manager.stations[0], "111111")) 
print(manager.retire_astronaut(manager.stations[1], "45678999")) 
print() 
 
# Perform an agency-wide update 
print(manager.agency_update(500_000.0)) 
print() 
 
# Check astronaut salaries after the update 
print(manager.stations[0].astronauts[0].salary) 
print(manager.stations[0].astronauts[1].salary) 
print(manager.stations[0].astronauts[2].salary) 
print() 
print(manager.stations[1].astronauts[0].salary) 
print(manager.stations[1].astronauts[1].salary) 
print(manager.stations[1].astronauts[2].salary) 
print() 
print(manager.astronauts[0].salary) 