# Load required packages
## Packages for game theory
import axelrod as axl
from axelrod.graph import Graph
## Package for network science
import networkx as nx
## Packages for math, statistics
import pandas as pd
import numpy as np
## Packages for visualization
import matplotlib.pyplot as plt
import matplotlib
import calculate_cache as cc
## Others
import warnings
warnings.filterwarnings("ignore")

# Visualization- To make it pretty
matplotlib.style.use('seaborn-colorblind')
font = {'size' : 14}
matplotlib.rc('font', **font)

# Initialization of players
population_size = 20
number_Defector = 6
number_Cooperator = 6
number_TitForTat = 6
number_Adaptive = population_size - number_Defector - number_Cooperator - number_TitForTat
players = [axl.Defector()]*number_Defector + [axl.Cooperator()]*number_Cooperator + [axl.TitForTat()]*number_TitForTat + [axl.Adaptive()]*number_Adaptive
seed_number = 15 # for reproducible example

################### 1 Basic tournament with moran process ##################
## Winning strategy as a function of noise
#winner_record = dict()
#for noise in np.arange(0,1.1,0.1):
#    axl.seed(seed_number) # for reproducible example
#    mp = axl.MoranProcess(players=players, turns=200, noise=noise)
#    populations = mp.play()
#    winner_record[noise]=mp.winning_strategy_name
#winner_record = pd.DataFrame([winner_record]).transpose()
#winner_record.index.names = ['Noise']
#winner_record.columns = ['Strategy']
#print(winner_record)

################## 2 Moran process on graphs ##############################
# Initialization of network
def network_generation(node_number, k, p, degree, name, seed_number, vis_flag):
    if name == 'Small-world':
        X = nx.connected_watts_strogatz_graph(node_number, k, p, tries=100, seed=axl.seed(seed_number))
    if name == 'Regular':
        X = nx.random_regular_graph(degree, node_number)
    if name == 'Random':
        X = nx.connected_watts_strogatz_graph(node_number, k, p, tries=100,seed=axl.seed(seed_number))
    # Visualize generated network
    if vis_flag == 1:
        fig, ax = plt.subplots(figsize=(7,7))
        G = nx.DiGraph()
        G.add_nodes_from(X.nodes())
        G.add_edges_from(X.edges())
        pos = nx.circular_layout(G)
        nx.draw(G, pos, node_size = 200, node_color = 'darkgreen', edge_color = 'darkgray', width=2, arrows=False)
        plt.show()
    return X.edges()

# Simulation start here
noise = 0
winner_record = dict()
## Network parameters
network_name = 'Small-world' # {0:'Regular', 1:'Small-world', 2:'Random'}
node_number = population_size
p = 1 # The probability of rewiring each edge
degree = 3
vis_flag = 1
for k in range(2,7):
    axl.seed(seed_number) # for reproducible example
    players = []
    players.append(axl.Defector())
    players.append(axl.Cooperator())
    players.append(axl.TitForTat())
    players.append(axl.Adaptive())
    cached_outcomes = cc.calculate_cache(players, turns=200)
    mp = axl.ApproximateMoranProcess(players=players, cached_outcomes = cached_outcomes)
    populations = mp.play()
    winner_record[k]=mp.winning_strategy_name
winner_record = pd.DataFrame([winner_record]).transpose()
winner_record.index.names = ['k']
winner_record.columns = ['Strategy']
print(winner_record)






