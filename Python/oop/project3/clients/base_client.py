from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        if name is None or name.strip() == "":
            raise ValueError("Client name should be determined!")
        self.name = name

        if membership_type not in ("Regular", "VIP"):
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.membership_type = membership_type

        self.points: int = 0

    @abstractmethod
    def earning_points(self, order_amount: float) -> int:
        raise NotImplementedError()

    def apply_discount(self) -> tuple[int, int]:
        if self.points >= 100:
            used = 100
            discount = 10
        elif self.points >= 50:
            used = 50
            discount = 5
        else:
            used = 0
            discount = 0

        self.points = max(0, self.points - used)
        return discount, self.points