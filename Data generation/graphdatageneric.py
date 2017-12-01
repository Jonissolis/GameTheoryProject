import axelrod as axl
import networkx as nx
import matplotlib.pyplot as plt
import random as rand

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
noise_level = 0 ### APPLY NOISE LEVEL, FROM 0 TO 1
# Game rules, set scores for r = (C, C), s = (C, D), t = (D, C) and p = (D, D)
game_rules = axl.Game(r = 3, s = 0, t = 5, p = 1) # default: r=3, s=0, t=5, p=1
axelrod_graph = axl.graph.Graph(x_graph.edges())
mp = axl.MoranProcess(initial_players,
                      turns=number_of_turns,
                      noise=noise_level,
                      game = game_rules,
                      interaction_graph=axelrod_graph)

# Iterate the population
previous_generation = initial_players
max_iterations = None ### INSERT NUMBER OF MAXIMUM ITERATIONS

for _ in range(max_iterations):
    results = mp.score_all()
    next_generation = []
    for ind in axelrod_graph.vertices():
        selection_candidates = [ind] + axelrod_graph.out_vertices(ind)
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
        next_generation.append(new_player)
        
    # Prepare Moran Process Object for next iteration
    mp.players = next_generation
    mp.populations.append(mp.population_distribution())
    previous_generation = next_generation
    
    if mp.fixation_check():
        break

# Show results
print(mp.score_history)
mp.population_distribution()
mp.populations_plot()