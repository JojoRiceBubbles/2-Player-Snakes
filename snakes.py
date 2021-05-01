import pygame
from pygame.sprite import Sprite
import functions as f

class Snakes():

    def __init__(self, screen, color, blocks, no):
        self.screen = screen
        self.color = color
        self.blocks = []
        self.no = no
        self.up = False
        self.down = False
        self.right = True
        self.left = False
        

    def grow(self,location,blocks):

        block = Blocks(self, location)
        self.blocks.append(block)
        blocks.add(block)
        
    def update(self,blocks,foods,stats,scoreboard):
        location = self.blocks[len(self.blocks) - 1].rect.topleft
        
        for block in reversed(self.blocks):
            if not block.no == 0:
                block.update()
                
            else:

                if self.up:
                    block.rect.y -= 50
                elif self.down:
                    block.rect.y += 50
                elif self.right:
                    block.rect.x += 50
                elif self.left:
                    block.rect.x -= 50

                if f.check_collisions(block, blocks):
                    stats.active = False

        test = pygame.sprite.groupcollide(blocks, foods, False, True)
        for food in test.values():
            if food[0].no == self.no:
                self.grow(location,blocks)
                stats.score += 1
                scoreboard.prep()
                f.create_food(food[0].color, blocks, self.screen, foods, self.no)
            else:
                print(1)
                stats.active = False
                f.create_food(food[0].color, blocks, self.screen, foods, self.no * -1)
                              
    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen, self.color, block.rect)

class Blocks(Sprite):

    def __init__(self,snake,location):

        super().__init__()
        self.snake = snake
        self.no = len(self.snake.blocks)

        self.rect = pygame.Rect(location,(50, 50))

    def update(self):
            self.rect.center = self.snake.blocks[self.no - 1].rect.center
            

        

    
