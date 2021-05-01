import pygame.font

class Scoreboard():

    def __init__(self, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        self.prep()
        
    def prep(self):

        
        score = self.stats.score
        score_str = str(score)
        self.score_image = self.font.render(score_str, True, self.color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def show(self):
        self.screen.blit(self.score_image, self.score_rect)
