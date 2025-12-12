from clients.base_client import BaseClient


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, membership_type="Regular")

    def earning_points(self, order_amount: float) -> int:
        if order_amount <= 0:
            return 0
        
        earned_points = int(order_amount // 10)
        self.points += earned_points
        return earned_points
