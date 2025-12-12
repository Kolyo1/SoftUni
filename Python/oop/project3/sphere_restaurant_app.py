from project.clients.base_client import BaseClient
from clients.regular_client import RegularClient
from clients.vip_client import VIPClient
import waiters
from waiters.base_waiter import BaseWaiter
from waiters.full_time_waiter import FullTimeWaiter
from waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.clients : list[BaseClient]= []
        self.waiters : list[BaseWaiter] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        valid_types = {
            "FullTimeWaiter": FullTimeWaiter,
            "HalfTimeWaiter": HalfTimeWaiter,
        }

        if waiter_type not in valid_types:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name is None or waiter_name.strip() == "":
            return "Waiter name should be determined!"

        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."

        waiter_cls = valid_types[waiter_type]
        waiter = waiter_cls(waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."
    
    def admit_client(self, client_type: str, client_name: str):
        valid_types = {
            "RegularClient": RegularClient,
            "VIPClient": VIPClient,
        }

        if client_type not in valid_types:
            return f"{client_type} is not a recognized client type."

        if client_name is None or client_name.strip() == "":
            return "Client name should be determined!"

        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."

        client_cls = valid_types[client_type]
        client = client_cls(client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."
    
    def process_shifts(self,waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        
        report = waiter.report_shift()
        return report
    
    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} is not a registered client."
        
        earned_points = client.earning_points(order_amount)
        return f"{client_name} earned {earned_points} points from the order."
    
    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {remaining_points}."
    
    def generate_report(self) -> str:
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        
        total_client_points = sum(client.points for client in self.clients)
        
        clients_count = len(self.clients)
        
        sorted_waiters = sorted(
            self.waiters, 
            key=lambda w: w.calculate_earnings(), 
            reverse=True
        )
        
        waiter_details = []
        for waiter in sorted_waiters:
            waiter_earnings = waiter.calculate_earnings()
            waiter_details.append(f"Name: {waiter.name}, Total earnings: ${waiter_earnings:.2f}")
        
        report_lines = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {total_client_points}",
            f"Total Clients Count: {clients_count}",
            "** Waiter Details **"
        ]
        
        report_lines.extend(waiter_details)
        
        return "\n".join(report_lines)