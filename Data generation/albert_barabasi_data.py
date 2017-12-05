import axelrod as axl
import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from collections import Counter
from copy import copy
#To make it pretty
import matplotlib.pyplot as plt
import matplotlib
import pylab as pl
matplotlib.style.use('seaborn-colorblind')
font = {'size' : 14}
matplotlib.rc('font', **font)

def ResultsFromCounter(cntrobj):
    valtot = sum(cntrobj.values())
    return "".join(['$|'] + [str(ind)[0] + ':' + "{0:.2f}".format(cntrobj[str(ind)]/valtot) + '|' for ind in strategy_pool] + ['$'])

def network_visualization(x_graph,filename,initial_players,player_colors):
    fig, ax = plt.subplots(figsize=(7,7))
    d = dict(nx.degree(x_graph))
    node_number = len(d)
    pos = nx.spring_layout(x_graph)
    nx.draw(x_graph, pos, node_size = [v / node_number *500 for v in d.values()], node_color = [player_colors[str(v)] for v in initial_players], edge_color = 'darkgray', width=0.3, alpha=0.3, arrows=False)
    plt.savefig(filename+'.png', dpi=900)
    plt.show()
    
filename = 'albert_barabasi_data_p=0.05'
make_plots = False
generate_new_graph = False

# Generate graph
plt.close('all')
if generate_new_graph:
    n = 80
    m = 3
    x_graph = nx.barabasi_albert_graph(n,m)
else:
    x_graph = nx.Graph([(0, 4), (0, 5), (0, 12), (0, 13), (0, 25), (0, 32), (0, 45), (0, 53), (0, 55), (0, 57), (0, 59), (0, 67), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 11), (1, 16), (1, 22), (1, 30), (1, 31), (1, 33), (1, 35), (1, 36), (1, 44), (1, 47), (1, 48), (1, 54), (1, 73), (1, 75), (2, 4), (2, 8), (3, 4), (3, 5), (3, 6), (3, 7), (3, 9), (3, 11), (3, 12), (3, 15), (3, 22), (3, 26), (3, 34), (3, 38), (3, 39), (3, 42), (3, 46), (3, 54), (3, 55), (3, 56), (3, 61), (3, 62), (3, 68), (3, 74), (4, 5), (4, 6), (4, 7), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 15), (4, 16), (4, 18), (4, 19), (4, 20), (4, 21), (4, 25), (4, 40), (4, 41), (4, 45), (4, 52), (4, 57), (4, 60), (4, 67), (4, 78), (5, 6), (5, 7), (5, 8), (5, 10), (5, 16), (5, 18), (5, 26), (5, 29), (5, 30), (5, 35), (5, 37), (5, 51), (5, 59), (5, 69), (6, 8), (6, 10), (6, 12), (6, 13), (6, 14), (6, 16), (6, 18), (6, 21), (6, 24), (6, 25), (6, 27), (6, 35), (6, 36), (6, 40), (6, 43), (6, 44), (6, 56), (6, 61), (6, 64), (7, 9), (7, 10), (7, 11), (7, 17), (7, 8), (7, 19), (7, 22), (7, 23), (7, 48), (7, 58), (7, 70), (7, 73), (7, 79), (8, 13), (8, 17), (8, 24), (8, 28), (8, 65), (8, 69), (8, 70), (9, 14), (9, 25), (9, 30), (9, 52), (9, 61), (10, 17), (10, 42), (10, 45), (10, 62), (10, 79), (11, 20), (11, 27), (11, 31), (11, 36), (11, 46), (11, 57), (12, 14), (12, 19), (12, 27), (12, 29), (12, 37), (12, 71), (13, 14), (13, 15), (13, 17), (13, 19), (13, 20), (13, 27), (13, 28), (13, 29), (13, 32), (13, 33), (13, 49), (13, 63), (13, 66), (13, 68), (14, 15), (14, 21), (14, 33), (14, 46), (14, 58), (14, 66), (14, 79), (15, 24), (15, 26), (15, 41), (15, 48), (15, 49), (15, 53), (15, 72), (15, 76), (16, 23), (16, 32), (16, 41), (16, 43), (16, 45), (16, 49), (16, 63), (16, 77), (16, 78), (17, 20), (17, 29), (17, 31), (17, 32), (17, 38), (17, 40), (17, 41), (17, 44), (17, 50), (17, 54), (17, 58), (17, 68), (17, 74), (18, 21), (18, 23), (18, 26), (19, 23), (19, 24), (19, 47), (19, 51), (19, 52), (19, 55), (19, 56), (19, 65), (19, 69), (19, 75), (20, 22), (20, 28), (20, 38),  (20, 55), (20, 59), (21, 65), (22, 30), (22, 39), (22, 74), (23, 31), (23, 36), (23, 49), (23, 58), (24, 28), (24, 34), (24, 48), (24, 56), (24, 63), (24, 74), (24, 76), (27, 33), (27, 34), (27, 51), (27, 53), (27, 54), (27, 59), (27, 65), (27, 78), (28, 50), (28, 60), (28, 77), (29, 34), (29, 42), (29, 53), (29, 57), (30, 35), (30, 43), (30, 51), (31, 37), (31, 39), (31, 46), (31, 50), (31, 72), (32, 37), (32, 44), (32, 69), (32, 79), (33, 42), (34, 39), (34, 50), (34, 60), (34, 61), (34, 72), (34, 73), (35, 63), (36, 62), (36, 64), (37, 38), (37, 64), (37, 75), (38, 40), (38, 43), (38, 70), (39, 76), (40, 64), (40, 75), (41, 71), (43, 47), (44, 47), (44, 66), (44, 71), (44, 76), (48, 72), (49, 52), (49, 60), (49, 62), (49, 73), (52, 78), (54, 77), (56, 66), (59, 68), (61, 70), (62, 67), (63, 67), (65, 71), (76, 77)])

if make_plots:
    plt.subplots()
    nx.draw(x_graph, with_labels=True)

# Network Analysis
x_degree = x_graph.degree() # Number of edges for each node
x_degree_centrality = nx.degree_centrality(x_graph) # Fraction of nodes connected to
x_clustering = nx.clustering(x_graph) # Number of triangles for each node
x_transitivity = nx.transitivity(x_graph) # Transitivity, or Global Clustering Coefficient
x_average_clustering = nx.average_clustering(x_graph) # Average of all nodes' local clustering
x_order = x_graph.order() # Number of nodes
x_size = x_graph.size() # Number of edges
x_density = nx.density(x_graph) # Number of edges divided by max possible edges
x_diameter = nx.diameter(x_graph) # Max eccentricity or max possible distance between any two nodes

# Generate players by uniform picks from pool of strategy objects
number_of_nodes = len(x_graph.nodes())
strategy_pool = [axl.Cooperator(), axl.Defector(), axl.TitForTat()]
initial_players = [rand.choice(strategy_pool).clone() for _ in range(number_of_nodes)]

# Visualization of generated network
player_colors = {str(strategy_pool[0]):'darkgreen', str(strategy_pool[1]):'darkred',str(strategy_pool[2]):'darkblue'}
network_visualization(x_graph,filename,initial_players,player_colors)

# Initialize game
number_of_turns = 50
noise_level = 0.05
# Game rules, set scores for r = (C, C), s = (C, D), t = (D, C) and p = (D, D)
game_rules = axl.Game(r = 3, s = 0, t = 5, p = 1) # default: r=3, s=0, t=5, p=1
axelrod_graph = axl.graph.Graph(x_graph.edges())
mp = axl.MoranProcess(initial_players,
                      turns=number_of_turns,
                      noise=noise_level,
                      game = game_rules,
                      interaction_graph=axelrod_graph)

# Iterate the population
max_iterations = 5000
selection_probability = 1
experiment_repetitions = 10
experiments = []

for _ in range(experiment_repetitions):
    previous_generation = initial_players
    for _ in range(max_iterations):
        results = mp.score_all()
        next_generation = []
        for node_index in axelrod_graph.vertices():
            if rand.random() <= selection_probability:
                selection_candidates = [node_index] + axelrod_graph.out_vertices(node_index)
                selection_scores = [results[n] for n in selection_candidates]
                selection_total = sum(selection_scores)
                selection_pdf = [n/selection_total for n in selection_scores]
            
                # Roulette-wheel selection
                random_number = rand.random()
                for i in range(len(selection_candidates)):
                    random_number -= selection_pdf[i]
                    if random_number <= 0:
                        new_player = previous_generation[selection_candidates[i]].clone();
                        break
            else:
                new_player = previous_generation[node_index].clone()
                
            next_generation.append(new_player)
            
        # Prepare Moran Process Object for next iteration
        mp.players = next_generation
        mp.populations.append(mp.population_distribution())
        previous_generation = next_generation
        
        if mp.fixation_check():
            break
    
    # Prepare for next experiment
    if make_plots:
        saved_mp = copy(mp)
    experiments.append(mp.population_distribution())
    initial_players = [rand.choice(strategy_pool).clone() for _ in range(number_of_nodes)]
    mp.initial_players = initial_players
    mp.reset()

# Show results
if make_plots:
    saved_mp.populations_plot()

# Write results to file
networkstring = 'Degree: ' + str(x_degree) + '. Description: ' + 'Number of edges for each node' + '\n' +\
                'Degree Centrality: ' + str(x_degree_centrality) + '. Description: ' + 'Fraction of nodes connected to' + '\n' +\
                'Clustering: ' + str(x_clustering) + '. Description: ' + 'Number of triangles for each node' + '\n' +\
                'Transitivity: ' + str(x_transitivity) + '. Description: ' + 'Transitivity, or Global Clustering Coefficient' + '\n' +\
                'Average Clustering: ' + str(x_average_clustering) + '. Description: ' + 'Average of all nodes\' local clustering' + '\n' +\
                'Order: ' + str(x_order) + '. Description: ' + 'Number of nodes' + '\n' +\
                'Size: ' + str(x_size) + '. Description: ' + 'Number of edges' + '\n' +\
                'Density: ' + str(x_density) + '. Description: ' + 'Number of edges divided by max possible edges' + '\n' +\
                'Diameter: ' + str(x_diameter) + '. Description: ' + 'Max eccentricity or max possible distance between any two nodes' + '\n'

# (´・ω・`) Absolutely Incomprehensible String wIzÄrDRü (´・ω・`)
initstratsstring = ResultsFromCounter(Counter([str(entry) for entry in strategy_pool]))
gamerulesstring = 'R:' + str(game_rules.RPST()[0]) + ',P:' + str(game_rules.RPST()[1]) + ',S:' + str(game_rules.RPST()[2]) + ',T:' + str(game_rules.RPST()[3])
avgres = Counter([ResultsFromCounter(cntr) for cntr in experiments])
avgrestot = sum(avgres.values())
avgexp = "\\begin{tabular}{c}" + "\\\\".join(["".join([str(round(100*avgres[key]/avgrestot))] + ["\% "] + [key]) for key in avgres.keys()]) + "\\end{tabular}"
tablestring = initstratsstring + '&$' + gamerulesstring + '$&$' + str(noise_level) + '$&' + avgexp + '\\'*2 + '\n'

with open(filename + '.txt', 'w') as file:
    file.write(networkstring)
    file.write('\n\n')
    file.write('\\begin{table}\n')
    file.write('\\centering\n')
    file.write('\\begin{tabular}{c|c|c|c}\n')
    file.write('Initial population distribution&Game rules&Noise&Average resulting population distribution\\\\\n')
    file.write('\\hline\n')
    file.write(tablestring)
    file.write('\\end{tabular}\n')
    file.write('\\end{table}')
