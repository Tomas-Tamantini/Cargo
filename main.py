from random import seed

from gui.canvas import root, canvas_width, canvas_height
from gui.draw_methods import draw_network
from scripts.network_generator import random_network
from scripts.chromossome_generator import random_chromosome


seed(2)

n = random_network(city_dimensions=(canvas_width, canvas_height))
print(n)

c = random_chromosome(n)
print(c)

draw_network(n)
root.mainloop()
