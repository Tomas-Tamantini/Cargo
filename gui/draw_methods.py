from gui.canvas import canvas
from models.node import Retailer, Wholesale, Factory


def draw_point(x, y):
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='#002200')


def draw_node(node, color=None):
    outline_color = 'black' if color is None else color
    width = 1 if color is None else 2
    radius = 15
    if isinstance(node, Retailer):
        radius = 9 + 0.25 * (node.demand - 10)
    xc = node.position.x
    yc = node.position.y
    x0 = xc - radius
    x1 = xc + radius
    y0 = yc - radius
    y1 = yc + radius

    if isinstance(node, Retailer):
        canvas.create_oval(x0, y0, x1, y1, fill='#82eefd', outline=outline_color, width=width)
        canvas.create_text(xc, yc, text=str(node.demand))
    elif isinstance(node, Wholesale):
        canvas.create_polygon(x0, yc, xc, y0, x1, yc, xc, y1, fill='#f9e076', outline=outline_color, width=width)
    elif isinstance(node, Factory):
        canvas.create_polygon(x0, y0, x0, y1, x1, y1, x1, y0, fill='#d21404', outline=outline_color, width=width)


def draw_edge(node_a, node_b, color):
    print(color)
    canvas.create_line(node_a.position.x, node_a.position.y, node_b.position.x, node_b.position.y, width=2,
                       fill=color)


def draw_network(network, routes=None, color_routes=True):
    canvas.delete('all')

    drawn_nodes = []

    preset_colors = color_generator()
    color_dict = {}
    route_colors = []

    if routes is not None:
        for route in routes:
            color = 'black'
            if not route.van_route or not color_routes:
                pass
            else:
                origin = route.origin.name
                if origin in color_dict:
                    color = color_neighbor(color_dict[origin])
                else:
                    color = next(preset_colors)
                    color_dict[origin] = color
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


def color_generator():
    colors = ['#d0312d', '#3cb043', '#1338be', '#f6ca03']
    idx = 0
    while True:
        yield colors[idx]
        idx = (idx + 1) % len(colors)


def color_neighbor(color):
    return color
