from sa_bundle import run_solver

# Parameters:
random_seed = 25
num_nodes = (3, 4, 15)
demand_range = (10, 30)
num_it = 5000
temperature_range = (3000, 100)
vehicle_specs = {'van': {'capacity': 40, 'cost_per_km': 5}}


def main():
    run_solver(random_seed, num_nodes, demand_range, num_it, temperature_range, vehicle_specs)


if __name__ == '__main__':
    main()
