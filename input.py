import sys
import pygame
import functions as f
from snakes import Snakes 

def check(snake1, snake2, button, stats, blocks):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if button.rect.collidepoint(x, y) and not stats.active:
                    stats.active = True
                    stats.score = 0
                    blocks.empty()
                    snake1.blocks = []
                    snake2.blocks = []
                    snake1.grow((250, 300), blocks)
                    snake2.grow((250, 400), blocks)
                    
                    snake1.up = False
                    snake1.down = False
                    snake1.right = True
                    snake1.left = False

                    snake2.up = False
                    snake2.down = False
                    snake2.right = True
                    snake2.left = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake1.down == False:
                snake1.up = True
                snake1.right = False
                snake1.left = False

            elif event.key == pygame.K_s and snake1.up == False:
                snake1.down = True
                snake1.right = False
                snake1.left = False

            elif event.key == pygame.K_d and snake1.left == False:
                snake1.down = False
                snake1.right = True
                snake1.up = False

            elif event.key == pygame.K_a and snake1.right == False:
                snake1.up = False
                snake1.down = False
                snake1.left = True
                

            elif event.key == pygame.K_UP and snake2.down == False:
                snake2.up = True
                snake2.right = False
                snake2.left = False

            elif event.key == pygame.K_DOWN and snake2.up == False:
                snake2.down = True
                snake2.right = False
                snake2.left = False

            elif event.key == pygame.K_RIGHT and snake2.left == False:
                snake2.down = False
                snake2.right = True
                snake2.up = False


            elif event.key == pygame.K_LEFT and snake2.right == False:
                snake2.up = False
                snake2.down = False
                snake2.left = True


                
                    
        
        
