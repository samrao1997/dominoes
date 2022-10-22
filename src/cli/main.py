from objects import *



def setup():
    board = Board()
    player1 = Player()
    player2 = Player()
    
    for _ in range(13):
        player1.draw(board)
        player2.draw(board)
        
    print(player1.hand)
    print(player2.hand)

def main():
    # main game loop
    setup()
    
    while True:
        inp = input("What would you like to do? ")
        
        
        
        if inp == "q" or inp == "quit":
            break
        
        
        
        




if __name__ == '__main__':
    main()
