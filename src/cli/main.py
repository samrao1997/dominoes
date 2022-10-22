import random

from objects import *



def setup():
    # init board
    board = Board()
    
    # init players
    player1 = Player()
    player2 = Player()
    
    # players draw hand
    for _ in range(13):
        player1.draw(board)
        player2.draw(board)
    
    # first player
    first_player = random.choice([player1, player2])
    first_player.play(board, first_player.hand.dominoes[0])
    print(board.layout.layout)
    
    
def display_state():
    display_board()
    display_player()
    display_other_players()


def display_board():
    # display layout
    # display layout value
    # display boneyard
    pass

def display_player():
    # display possible dominoes to place
    # display your score
    pass

def display_other_players():
    # display # of dominoes
    # display there score
    pass

        
def main():
    setup()
    
    # main game loop
    while True:
        inp = input("What would you like to do? ")
        
        
        
        # QUIT
        if inp == "q" or inp == "quit":
            break
        
        
        
        




if __name__ == '__main__':
    main()
