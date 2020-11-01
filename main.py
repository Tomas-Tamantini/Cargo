from random import seed

from gui.canvas import root, canvas_width, canvas_height
from gui.draw_methods import draw_network
from scripts.network_generator import random_network

seed(2)

n = random_network(city_dimensions=(canvas_width, canvas_height))
print(n)

draw_network(n)
root.mainloop()
