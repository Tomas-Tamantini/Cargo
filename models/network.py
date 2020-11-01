from scripts.str_scripts import list_to_str


class Network:
    def __init__(self, factories, wholesales, retailers):
        self.factories = factories
        self.wholesales = wholesales
        self.retailers = retailers

    @property
    def total_demand(self):
        return sum(map(lambda ret: ret.demand, self.retailers))

    def __str__(self):
        return list_to_str('Factories:', self.factories) + '\n' + \
               list_to_str('Wholesales:', self.wholesales) + '\n' + \
               list_to_str('Retailers:', self.retailers)
