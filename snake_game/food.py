import random
import pygame



class Food:

	def __init__(self,sc_width,sc_height, coef):

		self.food_pos = [random.randrange(1, int(sc_width/coef))*coef,random.randrange(1,int(sc_height/coef))*coef]


	def food_draw(self,play_surface,food_color, coef):
		pygame.draw.rect(play_surface,food_color,(self.food_pos[0],self.food_pos[1],coef,coef))