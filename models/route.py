from models.vehicle import TruckSpecs, VanSpecs
from scripts.str_scripts import list_to_str


class Route:
    def __init__(self, ordered_nodes, van_route=True):
        self.ordered_nodes = ordered_nodes
        self.van_route = van_route

    @property
    def origin(self):
        return self.ordered_nodes[0]

    @property
    def cost(self):
        total_distance = 0
        for i in range(len(self.ordered_nodes)):
            total_distance += self.ordered_nodes[i].dist(self.ordered_nodes[i - 1])
        if self.van_route:
            return total_distance * VanSpecs['cost_per_km']
        else:
            return total_distance * TruckSpecs['cost_per_km']

    def __str__(self):
        header = 'Van:' if self.van_route else 'Truck:'
        return list_to_str(header, self.ordered_nodes, lambda node: node.name, ',')
