import random

class Player:
    points = 0
    opponent_last_choice = ""
    
    def __init__(self, starting_points):
        self.points = starting_points
        
class Copycat(Player):
    
    def __init__(self, starting_points):
        super().__init__(starting_points)
        
    def get_opening_choice(self):
        return "Ally"
    
    def get_choice(self):
        if self.opponent_last_choice == "Betray":
            return "Betray"
        elif self.opponent_last_choice == "Ally":
            return "Ally"

class Betrayer(Player):
    
    def __init__(self, starting_points):
        super().__init__(starting_points)
        
    def get_opening_choice(self):
        return "Betray"
    
    def get_choice(self):
        return "Betray"
    
class Ally(Player):
    
    def __init__(self, starting_points):
        super().__init__(starting_points)
        
    def get_opening_choice(self):
        return "Ally"
    
    def get_choice(self):
        return "Ally"

def play_game(player, opponent, number_of_games):
    if player.get_opening_choice() == "Ally":
        if opponent.get_opening_choice() == "Ally":
            player.points += 2
            player.opponent_last_choice = "Ally"
            opponent.points += 2
            opponent.opponent_last_choice = "Ally"
        elif opponent.get_opening_choice() == "Betray":
            player.points += 0
            player.opponent_last_choice = "Betray"
            opponent.points += 3
            opponent.opponent_last_choice = "Ally"
    elif player.get_opening_choice() == "Betray":
        if opponent.get_opening_choice() == "Ally":
            player.points += 3
            player.opponent_last_choice = "Ally"
            opponent.points += 0
            opponent.opponent_last_choice = "Betray"
        elif opponent.get_opening_choice() == "Betray":
            player.points += 0
            player.opponent_last_choice = "Betray"
            opponent.points += 0
            opponent.opponent_last_choice = "Betray"
    for n in range(1,number_of_games):
        if player.get_choice() == "Ally":
            if opponent.get_choice() == "Ally":
                player.points += 2
                player.opponent_last_choice = "Ally"
                opponent.points += 2
                opponent.opponent_last_choice = "Ally"
            elif opponent.get_choice() == "Betray":
                player.points += 0
                player.opponent_last_choice = "Betray"
                opponent.points += 3
                opponent.opponent_last_choice = "Ally"
        elif player.get_choice() == "Betray":
            if opponent.get_choice() == "Ally":
                player.points += 3
                player.opponent_last_choice = "Ally"
                opponent.points += 0
                opponent.opponent_last_choice = "Betray"
            elif opponent.get_choice() == "Betray":
                player.points += 0
                player.opponent_last_choice = "Betray"
                opponent.points += 0
                opponent.opponent_last_choice = "Betray"

def round_robin(players, number_of_games):
    for player_number in range(0,len(players)):
        for opponent in players[player_number+1:]:
            play_game(players[player_number], opponent, number_of_games)

def random_pairs(players, number_of_games):
    pool = list(range(0, len(players)))
    pairs = []
    while pool:
        a = random.choice(pool)
        pool.remove(a)
        b = random.choice(pool)
        pool.remove(b)
        pairs.append((a,b))

    for p in pairs:
        play_game(players[p[0]],players[p[1]],number_of_games)


def main():
    copycats = [Copycat(0) for i in range(0,6)]
    betrayers = [Betrayer(0) for i in range(0,6)]
    allies = [Ally(0) for i in range(0,6)]
    players = copycats + betrayers + allies
    for p in players:
       print((p.points, p.opponent_last_choice))
    # round_robin(players, 10)
    random_pairs(players, 1)
    for p in players:
        print((p.points, p.opponent_last_choice))
    

main()





















