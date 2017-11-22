import random

# Play a number of games against the same opponent. 
# All history is cleared after the games. 
def play_game(player1, player2, number_of_games):
    awarded_points = [3, 2, 1, 0]   # This list gives the number of points awarded for the different outcomes. 
                                    # The first element in the list is points for deflect against cooperation. 
                                    # Second is cooperation against cooperation.
                                    # Third is deflect against deflect.
                                    # Fourth is cooperation against deflect. 
                                    
    for n in range(0, number_of_games):
        move1 = player1.get_choice()
        move2 = player2.get_choice()
        
        if move1 and move2:
            player1.points += awarded_points[1]
            player2.points += awarded_points[1]
            
        if not move1 and move2:
            player1.points += awarded_points[0]
            player2.points += awarded_points[3]
            
        if move1 and not move2:
            player1.points += awarded_points[3]
            player2.points += awarded_points[0]
        
        if not move1 and not move2:
            player1.points += awarded_points[2]
            player2.points += awarded_points[2]
        
        player1.add_history(move2)
        player2.add_history(move1)
    player1.history = []
    player2.history = []

# A mode where all players face each each other player a set number of times. 
def round_robin(players, number_of_games):
    nPlayers = len(players)
    for player_number in range(0, nPlayers):
        player1 = players[player_number]
        for player2 in players[player_number+1:]:
            play_game(player1, player2, number_of_games)


def random_pairs(players, number_of_games):
    nPlayers = len(players)
    if nPlayers % 2 == 1:
        raise ValueError( "Random pairs can't be used with an odd number of players. " )
    
    pool = list(players[i] for i in range(0, nPlayers))
    while pool:
        player1 = random.choice(pool)
        pool.remove(player1)
        player2 = random.choice(pool)
        pool.remove(player2)
        play_game(player1, player2, number_of_games)
    