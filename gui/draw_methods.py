from random import randint, random

from gui.canvas import canvas
from gui.colors import *
from models.node import Retailer, Wholesale, Factory


def draw_node(node, color=None):
    outline_color = outline_default_color if color is None else color
    width = 1 if color is None else 2
    radius = 18 if not isinstance(node, Wholesale) else 15
    if isinstance(node, Retailer):
        radius = 12 + 0.25 * (node.demand - 10)
    xc = node.position.x
    yc = node.position.y
    x0 = xc - radius
    x1 = xc + radius
    y0 = yc - radius
    y1 = yc + radius

    if isinstance(node, Retailer):
        canvas.create_oval(x0, y0, x1, y1, fill=retailer_color, outline=outline_color, width=width)
        draw_text(str(node.demand), xc, yc, color=black)
    elif isinstance(node, Wholesale):
        y2 = y0 - radius * 0.4
        canvas.create_polygon(x0, y2, x0, y1, x1, y1, x1, y0, fill=wholesale_color, outline=outline_color, width=width)
        draw_text(str(node.name), xc, yc, color=black)
    elif isinstance(node, Factory):
        chimney_height = radius * 1.5
        chimney_base_width = 0.3 * radius
        chimney_top_width = chimney_base_width * 1
        roof_height = radius / 2

        chimney_width_offset = (chimney_base_width - chimney_top_width) / 2

        y2 = y0 - chimney_height
        y3 = y0 - roof_height
        x2 = x1 - chimney_width_offset
        x3 = x2 - chimney_top_width
        x4 = x1 - chimney_base_width
        x5 = (x0 + x4) / 2

        canvas.create_polygon(x0, y0, x0, y1, x1, y1, x1, y0, x2, y2, x3, y2, x4, y0, x5, y3, x5, y0, x0, y3,
                              fill=factory_color,
                              outline=outline_color, width=width)
        draw_text(str(node.name), xc, yc)


def draw_edge(node_a, node_b, color):
    canvas.create_line(node_a.position.x, node_a.position.y, node_b.position.x, node_b.position.y, width=2,
                       fill=color)


def draw_network(network, routes=None, color_routes=True):
    canvas.delete('all')

    drawn_nodes = []

    color_gen = RouteColorsGenerator()
    route_colors = []

    if routes is not None:
        for route in routes:
            color = outline_default_color if (not route.van_route or not color_routes) else color_gen.get_color(route)

            route_colors.append(color)
            for i in range(len(route.ordered_nodes)):
                node_a = route.ordered_nodes[i]
                node_b = route.ordered_nodes[i - 1]
                draw_edge(node_a, node_b, color)

        for i, route in enumerate(routes):
            color = route_colors[i]
            for node in route.ordered_nodes:
                if node.name not in drawn_nodes:
                    draw_node(node, color)
                    drawn_nodes.append(node.name)

    nodes = network.retailers + network.wholesales + network.factories
    for node in nodes:
        if node.name not in drawn_nodes:
            draw_node(node)


def draw_text(text, x=0, y=0, color=text_default_color):
    canvas.create_text(x, y, text=text, fill=color, font=('Helvetica', 12, 'bold'))


def draw_point(x, y):
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='#002200')
