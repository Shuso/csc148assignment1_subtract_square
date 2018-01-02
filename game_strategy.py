class GenStrategy():
    
    def __init__(self, moves):
        
        self.moves = open(moves,"r").read().splitlines()
        
    
    
  
import random
          
class Random(GenStrategy):
    """ a class representing a simple strategy that computer use to choose moves"""
   
   
    def __init__(self, moves):
        
        GenStrategy.__init__(self, moves)
        
    def move(self):
        
        return random.choice(moves)
        
moves = "SubSquare_valid_moves.txt"       
s = GenStrategy(moves)
s.moves 
