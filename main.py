from random import seed
from time import sleep

from gui.canvas import root, canvas_width, canvas_height
from gui.data_plot import plot
from gui.draw_methods import draw_network
from scripts.chromosome_to_routes import chromosome_to_routes
from scripts.network_generator import random_network
from scripts.chromosome_generator import random_chromosome
from scripts.optimize import AnnealingSolver

# Parameters
rnd_seed = 8
nit = 1000
initial_temperature = 10000
final_temperature = 1
animate = False

# Setup
seed(rnd_seed)

net = random_network(city_dimensions=(canvas_width, canvas_height))
chromosome = random_chromosome(net)
solver = AnnealingSolver(chromosome, initial_temperature, final_temperature, nit)

draw_network(net)
root.update()
sleep(1)

for i in range(nit):
    if i % (nit // 20) == 0:
        percentage = 100 * i // nit
        print(f'{percentage}%')
    change_happened, _ = solver.make_change()
    if change_happened and animate:
        draw_network(net, chromosome_to_routes(solver.chromosome))
        root.update()
        # sleep(.1)
print('100%')
draw_network(net, chromosome_to_routes(solver.chromosome))

plot(nit, solver.cost_history, solver.temp_history)

root.mainloop()
