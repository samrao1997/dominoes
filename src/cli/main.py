import random

from objects import *


def setup():
    # init board
    board = Board()

    # init players
    player1 = Player(board)
    player2 = Player(board)

    # players draw hand
    for _ in range(13):
        player1.draw()
        player2.draw()

    # first player
    first_player = random.choice([player1, player2])

    return (first_player, player1, player2, board)


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
    first_player, player1, player2, board = setup()

    # main game loop
    while True:
        inp = input("What would you like to do? ")

        if inp == "b":
            print(board.layout)

        if inp == "p":
            print(first_player.hand, first_player.score)

        if inp == "play":
            print(first_player.get_valid_placements())
            dom_idx = int(input("Which domino would you like to play? "))
            dom = first_player.hand.dominoes[dom_idx]
            first_player.play(dom)

        # QUIT
        if inp == "q" or inp == "quit":
            break


if __name__ == "__main__":
    main()

"""
[(1,2)] -> [(1,2), (2,3)]
-> [(3,1), (1,2), (2,3)] -> [(3,3), (3,1), (1,2), (2,3)] plays double but doesn't create another tail till closed
-> [(6,3), (3,3), (3,1), (1,2), (2,3)] Creates another tail
== [[(6,3), (3,3), (3,1), (1,2), (2,3)], [(3,3)]] Tails 6, 3, 3, 3


tails
for line in layout:
    ltail = line[0][0]
    rtail = line[-1][1]
    
but the value of the other lines dont count till extended
also logic for creating new line? when double is surrounded make new line with double
"""
