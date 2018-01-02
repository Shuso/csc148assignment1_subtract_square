import random
import math

def game():

    start_number = random.randrange(1, 10000)
    
    
    
    player_A = input("please enter player's name:")
    
    player_B = " computer "
    
    current_player = " "
    
    print('the start number is:' + str(start_number))
    
    current_number = start_number
    
    while current_number != 0:
        
        print('current player is: ' + current_player)
        
        perfect_square = int(input("please enter the square of a postive whole number: "))
        
    
        
        while perfect_square > current_number or not math.sqrt(perfect_square) - int(math.sqrt(perfect_square)) == 0 :
            perfect_square = int(input("the number you provide is not a valid number, please enter the square of a postive whole number:"))
    
        current_number -= perfect_square
        
        current_player = player_A
        
        print( "you choose: " + str(perfect_square))
    
        if current_number != 0:
            
            current_player = player_B
            
            print('current player is: computer')
            
            computer = (random.randrange(1, 10000))**2
        
            while computer > current_number:                                      
                
                computer = (random.randrange(1, 10000))**2
                
            print( " computer choose: " + str(computer) )   
            current_number -= computer
            
            
            
            print('current number is: ' + str(current_number))
        
    print("winner is:" + current_player + "."+ " the game is over")
    
    return current_number 
    
        
        
game()