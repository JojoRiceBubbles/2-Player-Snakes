import pygame
from food import Food
from pygame.sprite import Sprite

def update_screen(screen,settings,snake1,snake2,foods,scoreboard, button, stats):
        screen.fill(settings.bg_color)
        snake1.draw()
        snake2.draw()
        for food in foods.sprites():
            food.draw()

        scoreboard.show()

        if not stats.active:
            button.draw()

        pygame.display.flip()
        
def food_check(location, blocks, foods):
        for block in blocks:
            if block.rect.collidepoint(location):
                return True
            
        for food in foods:
            if food.rect.collidepoint(location):
                return True
        
def create_food(color, blocks, screen, foods, no):
        food = Food(color, blocks, screen, foods, no)

def check_collisions(block, blocks):
        blocks.remove(block)
        if pygame.sprite.spritecollideany(block, blocks):
                return True
        if block.rect.left < 0:
                return True
        if block.rect.right > 750:
                return True
        if block.rect.top < 0:
                return True
        if block.rect.bottom > 750:
                return True
        blocks.add(block)
#def check_eat(blocks, food)
        

            
