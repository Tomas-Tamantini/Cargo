from math import ceil
from random import sample, choice

from models.gene import Chromosome, Gene
from models.vehicle import van, truck


def random_chromosome(network):
    retailers_order = sample(network.retailers, len(network.retailers))
    num_vans = ceil(network.total_demand / van.capacity)
    van_origins = []
    for i in range(num_vans):
        van_origins.append(choice(network.wholesales))
    van_offsets = [0] * (num_vans - 1)
    gene_vans = Gene(retailers_order, van_offsets, van_origins, network.wholesales)

    wholesales_order = sample(network.wholesales, len(network.wholesales))
    num_trucks = ceil(network.total_demand / truck.capacity)
    truck_origins = []
    for i in range(num_trucks):
        truck_origins.append(choice(network.factories))
    truck_offsets = [0] * (num_trucks - 1)

    gene_trucks = Gene(wholesales_order, truck_offsets, truck_origins, network.factories)
    return Chromosome(gene_vans, gene_trucks)
