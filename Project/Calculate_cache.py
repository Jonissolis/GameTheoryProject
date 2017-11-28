# Load required packages
## Packages for game theory
import axelrod as axl
from typing import List
from collections import Counter

def calculate_cache(strategies: List[axl.Player], turns: int = 100) -> dict:
    """
    Used to calculacte cached outcomes. Does only work for deterministic strategies. 
    
    Parameters
    ----------
    strategies : [List[axelrod.Player]]
        A list containing the strategies to be cached. Only one instance of each strategy required. 
    turns : int
        The number of turns to be played. 
        
    returns : 
        A cache ready to be used by ApproximatedMoranProcess
    
    """
    cached_outcomes = dict()
    number_of_strategies = len(strategies)
    
    for i in range(0, number_of_strategies):
        for j in range(i + 1, number_of_strategies):
            strategy1 = strategies[i]
            strategy2 = strategies[j]
            match = axl.Match(players=[strategy1, strategy2], turns=turns)
            match.play()
            strategy_names = tuple([str(strategy1), str(strategy2)])
            scores = match.final_score()
            cached_outcomes[strategy_names] = Counter([scores[0], scores[1]])
    return cached_outcomes
        
        
        
def main():
    """ Example of how the calculate_cache function can be used. """
    
    # Initialization of players
    players = []
    # Edit here for different strategies, only one of each is neccesary
    players.append(axl.Adaptive([axl.Action.C, axl.Action.D]))
    players.append(axl.TitForTat())
    players.append(axl.Alternator())
    players.append(axl.Defector())
    turns = 100
    
    cached_outcomes = calculate_cache(players, turns)
    print(cached_outcomes)