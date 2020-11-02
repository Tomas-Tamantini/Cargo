from math import exp
from random import random

from scripts.chromosome_to_routes import chromosome_to_routes


def cost(chromosome):
    total_cost = 0
    for route in chromosome_to_routes(chromosome):
        total_cost += route.cost
    return total_cost


class AnnealingSolver:
    def __init__(self, initial_chromosome, initial_temperature=100, final_temperature=1, num_it=1000):
        self.chromosome = initial_chromosome
        self.temperature = initial_temperature
        self.final_temperature = final_temperature
        self.num_iterations = num_it
        self.temp_decay_rate = (final_temperature / initial_temperature) ** (1 / num_it)
        self.current_cost = cost(initial_chromosome)
        self.temp_history = [initial_temperature]
        self.cost_history = [self.current_cost]

    def make_change(self):
        change_happened = False
        probability = 1

        new_chromosome = self.chromosome.child()
        new_cost = cost(new_chromosome)
        if new_cost < self.current_cost:
            self.chromosome = new_chromosome
            self.current_cost = new_cost
            change_happened = True
        else:

            probability = exp((self.current_cost - new_cost - 1) / self.temperature)

            r = random()
            if r < probability:
                self.chromosome = new_chromosome
                self.current_cost = new_cost
                change_happened = True

        self.temperature *= self.temp_decay_rate
        self.temp_history.append(self.temperature)
        self.cost_history.append(self.current_cost)
        return change_happened, probability

    def __str__(self):
        return f'Temperature: {self.temperature} °C\nCost: {self.current_cost}'
