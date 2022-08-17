import random
import copy
import pygame



class Snake:

	def __init__(self,snake_color, coef, sc_width, sc_height):
		self.color = snake_color

		self.snake_body = [[sc_width - coef*i, sc_height/2] for i in range(2,-1, -1)]
		self.snake_head_pos = list(self.snake_body[0])

		self.base_snake_pos = copy.deepcopy(self.snake_body)

		self.direction = 'left'
		self.change_to = ''


	def change_direction(self):
		if any((self.change_to == 'right' and self.direction != 'left',
					self.change_to == 'left' and self.direction != 'right',
					self.change_to == 'up' and self.direction != 'down',
					self.change_to == 'down' and self.direction != 'up')):

			self.direction = self.change_to


	def change_head_pos(self, coef, sc_width, sc_height):
		if self.direction == 'right':
			self.snake_head_pos[0] += coef/2
		elif self.direction == 'left':
			self.snake_head_pos[0] -= coef/2
		elif self.direction == 'up':
			self.snake_head_pos[1] -= coef/2
		elif self.direction == 'down':
			self.snake_head_pos[1] += coef/2


	def body_mechanism(self,sc_width, sc_height, food_pos,score, coef):
		self.snake_body.insert(0,list(self.snake_head_pos))

		if (self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]):
			score +=1
			food_pos = [random.randrange(1, int(sc_width/coef))*coef,random.randrange(1,int(sc_height/coef))*coef]
		else:
			self.snake_body.pop()

		return score, food_pos


	def snake_draw(self,play_surface, play_surface_color, coef):
		play_surface.fill(play_surface_color)
		for block in self.snake_body:
			pygame.draw.rect(play_surface, self.color,(block[0],block[1],coef,coef))


	def check_for_boundaries(self,game_over,sc_width,sc_height, coef):
		if any((
			self.snake_head_pos[0] > sc_width-coef
			or self.snake_head_pos[0] < 0,
			self.snake_head_pos[1] > sc_height-coef
			or self.snake_head_pos[1] < 0
				)):

			self.snake_body = copy.deepcopy(self.base_snake_pos)
			self.snake_head_pos = copy.deepcopy(self.base_snake_pos)[0]

			self.direction = 'left'
			self.change_to = ''

			game_over()

		for block in self.snake_body[1:]:
			if (block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]):

				self.snake_body = copy.deepcopy(self.base_snake_pos)
				self.snake_head_pos = copy.deepcopy(self.base_snake_pos)[0]

				self.direction = 'left'
				self.change_to = ''

				game_over()