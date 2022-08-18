import random
import pygame


class Food:
    def __init__(self, sc_width, sc_height, coefficient):
        self.food_pos = [random.randrange(1, int(sc_width / coefficient)) * coefficient,
                         random.randrange(1, int(sc_height / coefficient)) * coefficient]

    def food_draw(self, play_surface, food_color, coefficient):
        pygame.draw.rect(play_surface, food_color, (self.food_pos[0], self.food_pos[1], coefficient, coefficient))
