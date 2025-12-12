from waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self) -> float:
        hourly_rate = 15.0
        return self.hours_worked * hourly_rate
    
    def report_shift(self) -> str:
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."