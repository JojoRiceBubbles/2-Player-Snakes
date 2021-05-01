import pygame
from pygame.sprite import Sprite
from random import randint
import functions as f


class Food(Sprite):

    def __init__(self, color, blocks, screen, foods, no):

        super().__init__()
        self.screen = screen
        self.no = no
        self.color = color
        self.location = self.random_location(blocks, foods)
        self.rect = pygame.Rect(self.location,(50, 50))
        foods.add(self)
        
    def random_location(self, blocks, foods):
        x = randint(0, 14) * 50
        y = randint(0, 14) * 50
        location = (x, y)
        if f.food_check(location, blocks, foods):
            return self.random_location(blocks, foods)
        else:
            #print(location)
            return location


    def draw(self):
        pygame.draw.rect(self.screen, self.color , self.rect)
        
