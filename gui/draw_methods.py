from gui.canvas import canvas
from models.node import Retailer, Wholesale, Factory


def draw_point(x, y):
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='#002200')


def draw_node(node):
    offset = 15
    xc = node.position.x
    yc = node.position.y
    x0 = xc - offset
    x1 = xc + offset
    y0 = yc - offset
    y1 = yc + offset

    if isinstance(node, Retailer):
        canvas.create_oval(x0, y0, x1, y1, fill='#82eefd')
        canvas.create_text(xc, yc, text=str(node.demand))
    elif isinstance(node, Wholesale):
        canvas.create_polygon(x0, yc, xc, y0, x1, yc, xc, y1, fill='#f9e076', outline='black')
    elif isinstance(node, Factory):
        canvas.create_polygon(x0, y0, x0, y1, x1, y1, x1, y0, fill='#d21404', outline='black')


def draw_network(network):
    nodes = network.retailers + network.wholesales + network.factories
    for node in nodes:
        draw_node(node)
