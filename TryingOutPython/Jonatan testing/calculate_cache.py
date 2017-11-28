# Load required packages
## Packages for game theory
import axelrod as axl
from typing import List


## Others
import warnings
warnings.filterwarnings("ignore")



def calculate_cache(players: List[axl.Player], turns: int = 100) -> dict:
    cached_outcomes = dict()
    
    
    for i in range(0, len(players)):
        for j in range(i + 1, len(players)):
            player1 = players[i]
            player2 = players[j]
            match = axl.Match(players=[player1, player2], turns=turns)
            match.play()
            player_names = tuple([str(player1), str(player2)])
            scores = match.final_score()
            cached_outcomes[player_names] = [scores[0], scores[1]]
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