from scripts.str_scripts import list_to_str


class Gene:
    def __init__(self, ordered_nodes, offsets, origins):
        self.ordered_nodes = ordered_nodes
        self.offsets = offsets
        self.origins = origins

    @property
    def num_vehicles(self):
        return len(self.origins)

    def __str__(self):
        def str_fun(node):
            return node.name

        return list_to_str('Origins:', self.origins, str_fun, ', ') + '\n' + \
               list_to_str('Nodes:', self.ordered_nodes, str_fun, ', ') + \
               f'\nOffsets: {self.offsets}\n'


class Chromosome:
    def __init__(self, gene_vans, gene_trucks):
        self.gene_vans = gene_vans
        self.gene_trucks = gene_trucks

    def __str__(self):
        return f'Vans ({self.gene_vans.num_vehicles}):\n{self.gene_vans}\n' \
               f'Trucks ({self.gene_trucks.num_vehicles}):\n{self.gene_trucks}'
