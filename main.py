from random import seed
from time import sleep

from gui.canvas import root, canvas_width, canvas_height
from gui.draw_methods import draw_network
from scripts.chromosome_to_routes import chromosome_to_routes
from scripts.network_generator import random_network
from scripts.chromosome_generator import random_chromosome
from scripts.optimize import AnnealingSolver

seed(1)

n = random_network(city_dimensions=(canvas_width, canvas_height))

c = random_chromosome(n)

solver = AnnealingSolver(c)
draw_network(n, chromosome_to_routes(solver.chromosome))
root.update()
sleep(.1)
for i in range(10000):
    change_happened, _ = solver.make_change()
    if change_happened:
        draw_network(n, chromosome_to_routes(solver.chromosome))
        root.update()
        # sleep(.1)
        print(i, solver.temperature, solver.current_cost)
print('done')
draw_network(n, chromosome_to_routes(solver.chromosome))
root.update()
root.mainloop()
