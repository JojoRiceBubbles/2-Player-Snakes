import sys
import pygame
from pygame.sprite import Group

import input
import functions as f
from snakes import Snakes
from snakes import Blocks
from settings import Settings
from time import sleep
from food import Food
from game_stats import Stats
from scoreboard import Scoreboard
from button import Button

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    stats = Stats()
    
    scoreboard = Scoreboard(screen, stats)
    button = Button(screen, 'play')
    pygame.display.set_caption('Snake')
    blocks = Group()
    foods = Group()
    snake1 = Snakes(screen, settings.color1, blocks, 1)
    snake2 = Snakes(screen, settings.color2, blocks, -1)
    food1 = Food((125,0,0), blocks, screen, foods, 1)
    food2 = Food((0,125,0), blocks, screen, foods, -1)
    while True:
        pygame.display.flip()
        input.check(snake1, snake2,  button, stats, blocks)
        if stats.active:
            snake1.update(blocks,foods,stats,scoreboard)
            snake2.update(blocks,foods,stats,scoreboard)
            
        f.update_screen(screen,settings,snake1,snake2,foods,scoreboard,button,stats)

        sleep(0.2)
run_game()
