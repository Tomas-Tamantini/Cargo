from scripts.str_scripts import list_to_str


class Route:
    def __init__(self, ordered_nodes, van_route=True):
        self.ordered_nodes = ordered_nodes
        self.van_route = van_route

    @property
    def origin(self):
        return self.ordered_nodes[0]

    def __str__(self):
        header = 'Van:' if self.van_route else 'Truck:'
        return list_to_str(header, self.ordered_nodes, lambda node: node.name, ',')
