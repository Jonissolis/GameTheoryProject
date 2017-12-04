import axelrod as axl
import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from collections import Counter

def ResultsFromCounter(cntrobj):
    valtot = sum(cntrobj.values())
    return "".join(['$|'] + [str(ind)[0] + ':' + "{0:.2f}".format(cntrobj[str(ind)]/valtot) + '|' for ind in strategy_pool] + ['$'])

filename = None ### INSERT FILENAME AS STRING

# Generate graph
plt.close('all')
x_graph = None ### INSERT NETWORKX GRAPH OBJECT HERE
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
strategy_pool = [] ### FILL LIST WITH STRATEGIES TO BE SELECTED FROM
initial_players = [rand.choice(strategy_pool).clone() for _ in range(number_of_nodes)]

# Initialize game
number_of_turns = None ### INSERT NUMBER OF TURNS TO PLAY
noise_level = None ### APPLY NOISE LEVEL, FROM 0 TO 1
# Game rules, set scores for r = (C, C), s = (C, D), t = (D, C) and p = (D, D)
game_rules = axl.Game(r = 3, s = 0, t = 5, p = 1) # default: r=3, s=0, t=5, p=1
axelrod_graph = axl.graph.Graph(x_graph.edges())
mp = axl.MoranProcess(initial_players,
                      turns=number_of_turns,
                      noise=noise_level,
                      game = game_rules,
                      interaction_graph=axelrod_graph)

# Iterate the population
max_iterations = None ### INSERT NUMBER OF MAXIMUM ITERATIONS
selection_probability = None ### INSERT PROBABILITY OF SELECTION FOR ANY ONE NODE
experiment_repetitions = None ### INSERT NUMBER OF TIMES TO REPEAT EXPERIMENT AND AVERAGE OVER
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
    experiments.append(mp.population_distribution())
    initial_players = [rand.choice(strategy_pool).clone() for _ in range(number_of_nodes)]
    mp.initial_players = initial_players
    mp.reset()

# Show results
mp.populations_plot()

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
