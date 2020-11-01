from copy import deepcopy

from models.route import Route
from models.vehicle import VanSpecs, TruckSpecs


def chromosome_to_routes(chromosome):
    routes = []
    aux_retailers = [(i, r.demand) for i, r in enumerate(chromosome.gene_vans.ordered_nodes) if r.demand > 0]

    for orig_idx, origin in enumerate(chromosome.gene_vans.origins):
        nodes = [origin]
        acc_cargo = 0
        while len(aux_retailers) > 0:
            current_index, current_demand = aux_retailers[0]
            del aux_retailers[0]

            if acc_cargo + current_demand < VanSpecs['capacity']:
                acc_cargo += current_demand
                nodes.append(chromosome.gene_vans.ordered_nodes[current_index])
                continue
            elif acc_cargo + current_demand == VanSpecs['capacity']:
                nodes.append(chromosome.gene_vans.ordered_nodes[current_index])
            else:
                delivered = VanSpecs['capacity'] - acc_cargo
                nodes.append(chromosome.gene_vans.ordered_nodes[current_index])
                new_demand = current_demand - delivered
                new_element = current_index, new_demand
                insert_index = chromosome.gene_vans.offsets[orig_idx]
                if insert_index > len(aux_retailers):
                    insert_index = len(aux_retailers)
                aux_retailers.insert(insert_index, new_element)
            break

        new_route = Route(nodes, True)
        routes.append(new_route)

    aux_wholesales = []
    for i, wholesale in enumerate(chromosome.gene_trucks.ordered_nodes):
        demand = 0
        for r_idx, route in enumerate(routes):
            if route.origin == wholesale:
                if r_idx < len(routes) - 1:
                    demand += VanSpecs['capacity']
                else:
                    total_demand = sum(map(lambda r: r.demand, chromosome.gene_vans.ordered_nodes))
                    demand += total_demand % VanSpecs['capacity']
        if demand > 0:
            new_element = i, demand
            aux_wholesales.append(new_element)

    for orig_idx, origin in enumerate(chromosome.gene_trucks.origins):
        nodes = [origin]
        acc_cargo = 0
        while len(aux_wholesales) > 0:
            current_index, current_demand = aux_wholesales[0]
            del aux_wholesales[0]

            if acc_cargo + current_demand < TruckSpecs['capacity']:
                acc_cargo += current_demand
                nodes.append(chromosome.gene_trucks.ordered_nodes[current_index])
                continue

            elif acc_cargo + current_demand == TruckSpecs['capacity']:
                nodes.append(chromosome.gene_trucks.ordered_nodes[current_index])
            else:
                delivered = TruckSpecs['capacity'] - acc_cargo
                nodes.append(chromosome.gene_trucks.ordered_nodes[current_index])
                new_demand = current_demand - delivered
                new_element = current_index, new_demand
                insert_index = chromosome.gene_trucks.offsets[orig_idx]
                if insert_index > len(aux_wholesales):
                    insert_index = len(aux_wholesales)
                aux_wholesales.insert(insert_index, new_element)
            break
        new_route = Route(nodes, False)
        routes.append(new_route)
    return routes
