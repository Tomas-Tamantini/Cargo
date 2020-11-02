from math import sqrt, pi, sin, cos
from random import uniform, randint

from class_lib.vector_2d import Vector2D
from models.network import Network
from models.node import Factory, Wholesale, Retailer


def random_network(num_factories=1, num_wholesales=3, num_retailers=30, demand_range=(10, 30),
                   city_dimensions=(300, 300), padding=0.05):
    city_area = city_dimensions[0] * city_dimensions[1]
    num_nodes = num_factories + num_wholesales + num_retailers
    min_distance = 0.8 * 0.537284966 * sqrt(city_area / num_nodes)

    factories = []
    wholesales = []
    retailers = []

    def too_close(new_position):
        nodes = factories + wholesales + retailers
        for node in nodes:
            if new_position.dist(node.position) < min_distance:
                return True
        return False

    def corrected_position(pos):
        c_x = pos.x * (1 - 2 * padding) + padding * city_dimensions[0]
        c_y = pos.y * (1 - 2 * padding) + padding * city_dimensions[0]
        return Vector2D(c_x, c_y)

    def factory_rand_position():
        x, y = 0, 0
        for i in range(100):
            x = uniform(0, city_dimensions[0] / 10)
            y = uniform(0, city_dimensions[1])
            new_pos = Vector2D(x, y)
            if not too_close(new_pos):
                return corrected_position(new_pos)
        return corrected_position(Vector2D(x, y))

    def wholesale_rand_position():
        radius = city_dimensions[0] * 0.42
        x, y = city_dimensions[0] / 2 - radius, city_dimensions[1] / 2
        for i in range(100):
            radius = city_dimensions[0] * uniform(0.4, 0.45)
            ang = uniform(pi / 2, 3 * pi / 2)
            y = city_dimensions[1] / 2 + radius * sin(ang)
            if y < 0 or y > city_dimensions[1]:
                continue
            x = city_dimensions[0] * 0.55 + radius * cos(ang)
            new_pos = Vector2D(x, y)
            if not too_close(new_pos):
                return corrected_position(new_pos)
        return corrected_position(Vector2D(x, y))

    def retailer_rand_position():
        radius = city_dimensions[0] * 0.32
        x, y = city_dimensions[0] / 2 - radius, city_dimensions[1] / 2
        for i in range(100):
            radius = city_dimensions[0] * uniform(0, 0.4)
            ang = uniform(0, 2 * pi)
            y = city_dimensions[1] / 2 + radius * sin(ang)
            if y < 0 or y > city_dimensions[1]:
                continue
            x = city_dimensions[0] * 0.55 + radius * cos(ang)
            new_pos = Vector2D(x, y)
            if not too_close(new_pos):
                return corrected_position(new_pos)
        return corrected_position(Vector2D(x, y))

    for i in range(num_factories):
        name = chr(ord('A') + i)
        new_fac = Factory(factory_rand_position(), name)
        factories.append(new_fac)

    for i in range(num_wholesales):
        name = chr(ord('α') + i)
        new_wholesale = Wholesale(wholesale_rand_position(), name)
        wholesales.append(new_wholesale)

    for i in range(num_retailers):
        name = chr(ord('a') + i)
        demand = randint(*demand_range)
        new_retailer = Retailer(retailer_rand_position(), demand, name)
        retailers.append(new_retailer)

    return Network(factories, wholesales, retailers)
