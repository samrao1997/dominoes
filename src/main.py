#!usr/bin/env python


#-----------------IMPORTS-----------------#
import pygame as pg
from sys import exit

#-----------------------------------------#
#-----------------------------------------#




def draw_bg(screen):
    # draw red textured background
    bg = pg.image.load("./images/red_bg.jpg").convert()
    bg = pg.transform.scale(bg, screen.get_size())
    bg_rect = bg.get_rect()
    screen.blit(bg, bg_rect)


#-----------------------------------------#

def initialize(screen):
    draw_bg(screen)
    
    

#-----------------------------------------#

def main():
    
    
    
    
    # pygame initialization
    pg.init()
    
    
    # create the main surface
    screen = pg.display.set_mode((800, 400))
    pg.display.set_caption("[ ~ Dominos ~ ]")
    
    # set a clock
    clock = pg.time.Clock()
    
    
    
    # load the sound files
    
    # load images
    
    # initialize the game
    initialize(screen)
    
    
    
    
    #-----------------MAIN LOOP-----------------#
    
    while True:
    
        # event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
                
                
                
        # Update screen
        pg.display.update()

        # set fps
        clock.tick(60)






if __name__ == '__main__':
    main()