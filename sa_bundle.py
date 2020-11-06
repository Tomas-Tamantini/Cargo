from math import inf
from random import seed
from time import sleep

from gui.canvas import root, canvas_width, canvas_height
from gui.data_plot import plot
from gui.draw_methods import draw_network
from models.vehicle import truck, van
from scripts.chromosome_to_routes import chromosome_to_routes
from scripts.network_generator import random_network
from scripts.chromosome_generator import random_chromosome
from scripts.optimize import AnnealingSolver


def run_solver(random_seed=None,
               num_nodes=(2, 4, 10),
               demand_range=(10, 20),
               num_it=1000,
               temperature_range=(1000, 1),
               vehicle_specs=None):
    if vehicle_specs is not None:
        if 'van' in vehicle_specs:
            van.assign_from_dict(vehicle_specs['van'])
        if 'truck' in vehicle_specs:
            truck.assign_from_dict(vehicle_specs['truck'])
    if random_seed is not None:
        seed(random_seed)
    num_factories, num_wholesales, num_retailers = num_nodes
    initial_temperature, final_temperature = temperature_range
    net = random_network(num_factories, num_wholesales, num_retailers, demand_range,
                         city_dimensions=(canvas_width, canvas_height))
    chromosome = random_chromosome(net)
    solver = AnnealingSolver(chromosome, initial_temperature, final_temperature, num_it)

    draw_network(net)

    root.update()

    animate = num_it <= 5000

    if animate:
        sleep(2)

    stability_counter = 0
    stability_threshold = inf if num_it < 10000 else num_it // 10

    actual_nit = num_it
    for i in range(num_it):
        stability_counter += 1
        if i % (num_it // 20) == 0:
            percentage = 100 * i // num_it
            print(f'{percentage}% - cost {solver.current_cost}')
        change_happened, _ = solver.make_change()
        if change_happened:
            stability_counter = 0
            if animate:
                draw_network(net, chromosome_to_routes(solver.chromosome))
                root.update()
        elif stability_counter > stability_threshold:
            print('Stable solution found')
            actual_nit = i + 1
            break

    print('100%')
    print('\n'.join(map(str, chromosome_to_routes(solver.chromosome))) + f'\nTotal cost: {solver.current_cost}')
    draw_network(net, chromosome_to_routes(solver.chromosome))

    plot(actual_nit, solver.cost_history, solver.temp_history)

    root.mainloop()
