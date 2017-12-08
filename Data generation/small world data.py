import axelrod as axl
import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from collections import Counter
from copy import copy

def ResultsFromCounter(cntrobj):
    valtot = sum(cntrobj.values())
    return "".join(['$|'] + [str(ind)[0] + ':' + "{0:.2f}".format(cntrobj[str(ind)]/valtot) + '|' for ind in strategy_pool] + ['$'])

def network_visualization(x_graph, filename, initial_players, player_colors):
    fig, ax = plt.subplots(figsize=(7,7))
    d = dict(nx.degree(x_graph))
    node_number = len(d)
    pos = nx.spring_layout(x_graph)
    nx.draw(x_graph, pos, node_size = [v / node_number *500 for v in d.values()], node_color = [player_colors[str(v)] for v in initial_players], edge_color = 'darkgray', width=0.3, alpha=0.3, arrows=False)
    plt.savefig(filename+'.png', dpi=900)
    plt.show()

filename = "small_world_data_2"
make_plots = True
generate_new_graph = False

# Generate graph
plt.close('all')
if generate_new_graph:
    n = 100
    k = 4
    p = 0.05
    x_graph = nx.watts_strogatz_graph(n, k, p)
else:
    x_graph = nx.Graph([(0, 1), (0, 99), (0, 98), (0, 90), (1, 2), (1, 3), (1, 99), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 35), (5, 6), (5, 7), (6, 7), (6, 8), (7, 8), (7, 9), (8, 9), (8, 10), (9, 10), (9, 11), (10, 12), (10, 70), (11, 12), (11, 13), (12, 14), (12, 78), (13, 14), (13, 15), (14, 16), (14, 30), (15, 16), (15, 17), (16, 17), (16, 18), (17, 18), (17, 19), (18, 19), (18, 20), (19, 20), (19, 21), (20, 21), (20, 22), (21, 22), (21, 23), (22, 23), (22, 24), (23, 24), (23, 25), (24, 25), (24, 26), (25, 26), (25, 27), (26, 27), (26, 28), (27, 29), (27, 94), (27, 32), (28, 29), (28, 30), (29, 30), (29, 31), (30, 31), (30, 32), (31, 32), (31, 33), (32, 33), (33, 34), (33, 35), (34, 35), (34, 36), (35, 36), (35, 37), (36, 37), (36, 38), (37, 38), (37, 39), (38, 39), (38, 40), (39, 40), (39, 41), (40, 41), (40, 42), (41, 42), (41, 43), (42, 43), (42, 44), (43, 44), (43, 45), (44, 45), (44, 46), (45, 46), (45, 47), (46, 47), (46, 48), (47, 48), (47, 49), (48, 50), (48, 94), (49, 50), (49, 51), (50, 51), (50, 52), (51, 52), (1, 53), (52, 53), (52, 54), (53, 54), (53, 55), (54, 55), (54, 56), (55, 56), (55, 57), (56, 57), (56, 58), (57, 58), (57, 59), (58, 59), (58, 60), (59, 60), (59, 61), (60, 61), (60, 62), (61, 62), (61, 63), (62, 63), (62, 64), (63, 64), (63, 65), (64, 65), (64, 66), (65, 66), (65, 67), (66, 67), (66, 68), (67, 68), (67, 69), (68, 69), (68, 70), (69, 70), (69, 71), (70, 71), (70, 72), (71, 72), (71, 73), (72, 73), (72, 74), (73, 74), (73, 75), (74, 75), (74, 76), (75, 76), (75, 77), (76, 77), (76, 78), (77, 78), (77, 79), (78, 79), (78, 80), (79, 80), (79, 81), (80, 81), (80, 82), (81, 82), (81, 83), (82, 83), (82, 84), (83, 84), (83, 85), (84, 85), (84, 86), (85, 86), (85, 87), (86, 87), (86, 88), (87, 88), (87, 89), (88, 89), (88, 90), (89, 90), (89, 91), (90, 91), (90, 92), (91, 92), (91, 93), (92, 93), (92, 94), (93, 94), (93, 95), (94, 95), (94, 96), (95, 96), (95, 97), (96, 97), (96, 98), (97, 98), (97, 99), (98, 99)])

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

# Make Pretty Picture
if make_plots:
    player_colors = {str(axl.Cooperator()):"black", str(axl.Defector()):"black", str(axl.TitForTat()):"black"}
    network_visualization(x_graph, "SmallWorldGraph", initial_players, player_colors)

# Iterate the population
max_iterations = 5000
selection_probability = 1
experiment_repetitions = 1
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
    plt.title('')

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