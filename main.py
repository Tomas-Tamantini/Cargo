from random import seed

from gui.canvas import root, canvas_width, canvas_height
from gui.draw_methods import draw_network
from scripts.chromosome_to_routes import chromosome_to_routes
from scripts.network_generator import random_network
from scripts.chromossome_generator import random_chromosome

seed(2)

n = random_network(city_dimensions=(canvas_width, canvas_height))

c = random_chromosome(n)

r = chromosome_to_routes(c)

# print(n)

# print(c)


# print(n)
# print(c)
draw_network(n, r)
root.mainloop()
