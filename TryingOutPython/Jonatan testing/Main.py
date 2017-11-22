# Continuation on Adrian's code. 
from Strategies import Copycat, Betrayer, Ally
from Rulevariants import round_robin, random_pairs



def initialize_players(nCopycats, nBetrayers, nAllies):
    copycats = [Copycat(0) for i in range(0, nCopycats)]
    betrayers = [Betrayer(0) for i in range(0, nBetrayers)]
    allies = [Ally(0) for i in range(0, nAllies)]
    players = copycats + betrayers + allies
    return players

def main1():
    nCopycats = 4
    nBetrayers = 2
    nAllies = 2
    nGames = 5
    players = initialize_players(nCopycats, nBetrayers, nAllies)

    print("Playing " + str(nGames) + " games with random pairings: ")
    random_pairs(players, nGames)
    for p in players:
        print(p.title + " earned " + str(p.points) + " points. ")

def main2():
    nCopycats = 4
    nBetrayers = 2
    nAllies = 2
    nGames = 10
    
    players = players = initialize_players(nCopycats, nBetrayers, nAllies)
    
    print("Playing " + str(nGames) + " games with round robin. ")
    round_robin(players, nGames)
    
    for p in players:
        print(p.title + " earned " + str(p.points) + " points. ")

    
def main():
    main1()
    print("")
    print("")
    main2()
    
main()
