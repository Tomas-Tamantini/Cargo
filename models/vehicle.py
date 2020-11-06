van_cap = 40


class Vehicle:
    def __init__(self, capacity, cost_per_km):
        self.capacity = capacity
        self.cost_per_km = cost_per_km

    def assign_from_dict(self, vehicle_dict):
        if 'capacity' in vehicle_dict:
            self.capacity = vehicle_dict['capacity']
        if 'cost_per_km' in vehicle_dict:
            self.cost_per_km = vehicle_dict['cost_per_km']

    def __str__(self):
        return f'Capacity: {self.capacity}\nCost per km: {self.cost_per_km}'


van = Vehicle(van_cap, 5)
truck = Vehicle(5 * van_cap, 8)
