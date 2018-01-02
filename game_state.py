class GenGameState():

    
    
    def __init___(self, current_player,next_player,valid_moves): 
        
        """ a class trepresenting gamestates of any game with current player,
        next player,valid moves"""

        
        self.current_player = current_player
        
        self.next_player = next_player
        
        self.valid_moves = open( valid_moves,'r').read().splitlines()
        
    
        
        
    
    def __str__(self):
        
        if current_player == g.player1 and len(moves_avaliable_left)!= 0:
            return ' You choose {0} and your valid moves are {1} '.format(str(current_player),str(moves_avaliable_left))
        elif current_player == g.player2 and len(moves_avaliable_left)!= 0:
            return ' computer choose {0} '.format(str(current_player))
        elif current_player == g.player1 and len(moves_avaliable_left) == 0:
            return ' Sorry,you loose...'
        else:
            return ' Congragulation! You win!'
        
       
        
            
    
    
        
    
    def __repr__(self):
        
        pass
    
    def __eq__(self,other):
            return isinstance(self.current_player,GenGameState) and self.current_player, self.next_player,self.valid_moves == other and isinstance(self.next_player,GenGameState) and isinstance(self.valid_moves,GenGameState)        
        
        
        
        
    
    def move_available():
        
        raise NotImplementedError("Subclasses should implement this!")
    
    def display_winner():
        
        pass
    
    def evaluate():
        
        raise NotImplementedError("Subclasses should implement this!")


class SubSquare(GenGameState): 
    
    def __init__ (self, current_player, next_player, valid_moves):
        
        GenGameState.__init__(self, current_player, next_player, valid_moves)
        
    def __eq__(self,other):
        return isinstance(self.current_player,SubSquare) and self.current_player, self.next_player,self.valid_moves == other and isinstance(self.next_player,SubSquare) and isinstance(self.valid_moves,SubSquare)
        
        
    def __str__(self):
        return "({}, {})".format(str(self.current_player), str(self.next_player))
    
    def __repr__(self):
        
        return "SubSquare({}, {})".format(str(self.current_player), str(self.next_player))
        
    


     







