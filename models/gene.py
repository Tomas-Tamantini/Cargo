from copy import deepcopy
from random import random, randrange, choice

from scripts.str_scripts import list_to_str


class Gene:
    def __init__(self, ordered_nodes, offsets, origins, all_origins):
        self.ordered_nodes = ordered_nodes
        self.offsets = offsets
        self.origins = origins
        self.all_origins = all_origins

    @property
    def num_vehicles(self):
        return len(self.origins)

    def mutate(self):
        r = random()
        if r < 1 / 3:
            self.__mutate_order()
        elif r < 2 / 3:
            self.__mutate_offsets()
        else:
            self.__mutate_origins()

    def __mutate_order(self):
        if len(self.ordered_nodes) < 3:
            if len(self.all_origins) > 1 > 0:
                self.__mutate_origins()
                return
            if len(self.offsets) > 0:
                self.__mutate_offsets()
                return
            return

        first_index = randrange(len(self.ordered_nodes))
        second_index = randrange(1 + len(self.ordered_nodes))
        if second_index == first_index + 1:
            first_index -= 1
            if first_index == -1:
                first_index += len(self.ordered_nodes)
        if first_index > second_index:
            first_index, second_index = second_index, first_index

        r = random()
        if r < 1:
            self.ordered_nodes[first_index:second_index] = self.ordered_nodes[first_index:second_index][::-1]
        else:
            pass

    def __mutate_offsets(self):
        if len(self.offsets) == 0:
            if len(self.ordered_nodes) > 2:
                self.__mutate_order()
                return
            if len(self.all_origins) > 1 > 0:
                self.__mutate_origins()
                return
            return

        index = randrange(len(self.offsets))
        if self.offsets[index] >= len(self.ordered_nodes):
            self.offsets[index] -= 1
            return
        if self.offsets[index] <= 0:
            self.offsets[index] += 1
            return
        r = random()
        self.offsets[index] += 1 if r < 0.5 else -1

    def __mutate_origins(self):
        if len(self.all_origins) <= 1:
            if len(self.ordered_nodes) > 2:
                self.__mutate_order()
                return
            if len(self.offsets) > 0:
                self.__mutate_offsets()
                return
            return

        index = randrange(len(self.origins))
        new_origin = choice(self.all_origins)

        self.origins[index] = new_origin

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

    def child(self):
        new_chromosome = deepcopy(self)
        r = random()
        if r < 0.2:
            new_chromosome.gene_trucks.mutate()
        else:
            new_chromosome.gene_vans.mutate()
        return new_chromosome

    def __str__(self):
        return f'Vans ({self.gene_vans.num_vehicles}):\n{self.gene_vans}\n' \
               f'Trucks ({self.gene_trucks.num_vehicles}):\n{self.gene_trucks}'
