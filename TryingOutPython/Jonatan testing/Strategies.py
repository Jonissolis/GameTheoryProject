class Player:
    # A superclass to the different strategies. 
    
    def __init__(self, starting_points):
        self.points = starting_points
        self.history = [] # 1 for cooperation and 0 for deflecting. 
        self.title = ""
        
    def get_choice(self):
        raise NotImplementedError( "Should have implemented this" )
        
    def add_history(self, action):
        self.history.append(action)

class Copycat(Player):
    # A strategy that starts out by cooperating and then copies the opponents last move. 
    
    def __init__(self, starting_points):
        super(Copycat, self).__init__(starting_points)
        self.title = "Copycat"
    
    def get_choice(self):
        if len(self.history) == 0:
            return 1
        elif self.history[-1] == 1:
            return 1
        elif self.history[-1] == 0:
            return 0
    
class Betrayer(Player):
    # A strategy that always deflects the opponent. 
    
    def __init__(self, starting_points):
        super(Betrayer, self).__init__(starting_points)
        self.title = "Betrayer"
        
    def get_choice(self):
        return 0    

class Ally(Player):        
    # A strategy that always cooperates with the opponent. 
    
    def __init__(self, starting_points):
        super(Ally, self).__init__(starting_points)
        self.title = "Ally"
        
    def get_choice(self):
        return 1