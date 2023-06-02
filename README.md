# Dominoes -- Keller 5

I have been playing a kind of dominoes with my roommate that I can't seem to find online. I am interested
in the theory and maybe developing a good strategy for the game, so I am going to implement it.

It will be called Keller 5

Then maybe train a agent to do some reinforcement learning.

## Domino Set (Tiles)

    - Each tile is divided into two square ends which are marked with a number 0 through 9
        - 3 examples of tiles
            - [ 0 | 0 ]
            - [ 2 | 3 ]
            - [ 9 | 9 ]
    - Every tile in the set has a unique combination of two numbers
        - So the tile [2 | 3] is treated the same as [3 | 2]
    - Therefore there are 45 tiles in total [10 choose 2 = 45]

## Setup

    1. All 45 tiles are flipped face down to not see the values
    2. Each player draws a certain number of tiles as their hand
        - 2 players = 13 tiles
        - 3 or more players = 11 tiles
    3. To see who goes first, each player draws a single tile from
    the leftover tiles [*also know as boneyard*]. The player that has
    the highest valued tile goes first. **Then play goes clockwise.**

## Rules

If you play doubles go again - cant add to doubles untill closed
go again if multiple of 5

## TODO

- display board on command line
- game logic
- input actions
- AI

## Notes

- player selects domino from hand displays possible places [should it show the end values? Nope]
- when player selects a position show possible orientations

## Resources

This is my first time implementing pygame and I used [https://github.com/World-of-Domino/pygame-dominos] as a jumping off point.
Also [https://github.com/abw333/dominoes]
