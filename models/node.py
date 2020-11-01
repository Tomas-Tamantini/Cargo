class Node:
    def __init__(self, position, name=None):
        self.position = position
        self.name = name

    def dist(self, other):
        return self.position.dist(other.position)

    def __str__(self):
        name = self.name if self.name is not None else 'node'
        return f'{name} - {self.position}'


class Factory(Node):
    pass


class Wholesale(Node):
    pass


class Retailer(Node):
    def __init__(self, position, demand, name=None):
        super().__init__(position, name)
        self.demand = demand

    def __str__(self):
        return super().__str__() + f' - Demand: {self.demand}'
