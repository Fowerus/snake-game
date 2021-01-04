import pygame
import random
import sys

import json
import copy


class Game():
	def __init__(self):
		self.red = (200,0,0)
		self.white = (255,255,255)
		self.brown = (150,75,0)
		self.black = (0,0,0)
		self.grey = (40,40,40)
		self.menu_grey = (20,20,20)

		self.sc_width = 500
		self.sc_height = 500
		self.score = 0

		self.start = False

		self.sc = pygame.display.set_mode((self.sc_width,self.sc_height+50))


	def initialization(self):
		pygame.init()
		pygame.display.set_caption('Snake game')
		self.sc.fill(self.black)

		pygame.display.update()


	def check_key(self,change_to):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				self.get_score(1)
				sys.exit()
			if i.type == pygame.KEYDOWN:
				if i.key == pygame.K_a:
					change_to = 'left'
				elif i.key == pygame.K_d:
					change_to = 'right'
				elif i.key == pygame.K_w:
					change_to = 'up'
				elif i.key == pygame.K_s:
					change_to = 'down'

		return change_to


	def update_screen(self):
		pygame.display.update()
		pygame.time.Clock().tick(30)


	def score_draw(self):
		self.score_text = pygame.font.SysFont('arial',24)
		self.score_text = self.score_text.render(f'Score: {self.score}',1,self.white)

		self.score_surf = pygame.Surface((self.sc_width,50))
		self.score_surf.fill(self.grey)

		self.sc.blit(self.score_surf,(0,self.sc_height))
		self.sc.blit(self.score_text,(5,self.sc_height+5))


	def get_score(self,code):
		if code == 0:
			with open('log.json','r') as file:
				data = json.load(file)
				file.close()
			with open('log.json','w') as file:
				json.dump(data,file)
				file.close()

			return data

		elif code == 1:
			with open('log.json','r') as file:
				data = json.load(file)
				file.close()
			with open('log.json','w') as file:
				if data["m_score"] < self.score:
					data["m_score"] = self.score
				data["l_score"] = self.score

				json.dump(data,file)
				file.close()

				self.score = 0


	def game_over(self):
		self.start = False
		self.get_score(1)



class Snake:
	def __init__(self,snake_color):
		self.color = snake_color
		self.snake_head_pos = [250,120]
		self.snake_body = [[250,120],[260,120],[270,120]]

		self.base_snake_pos = copy.deepcopy(self.snake_body)

		self.direction = 'left'
		self.change_to = ''


	def change_direction(self):
		if any((self.change_to == 'right' and self.direction != 'left',
					self.change_to == 'left' and self.direction != 'right',
					self.change_to == 'up' and self.direction != 'down',
					self.change_to == 'down' and self.direction != 'up')):

			self.direction = self.change_to


	def change_head_pos(self):
		if self.direction == 'right':
			self.snake_head_pos[0] += 10
		elif self.direction == 'left':
			self.snake_head_pos[0] -= 10
		elif self.direction == 'up':
			self.snake_head_pos[1] -= 10
		elif self.direction == 'down':
			self.snake_head_pos[1] += 10


	def body_mechanism(self,sc_width, sc_height, food_pos,score):
		self.snake_body.insert(0,list(self.snake_head_pos))

		if (self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]):
			score +=1
			food_pos = [random.randrange(1,sc_width/10)*10,random.randrange(1,sc_height/10)*10]
		else:
			self.snake_body.pop()

		return score, food_pos


	def snake_draw(self,play_surface, play_surface_color):
		play_surface.fill(play_surface_color)
		for block in self.snake_body:
			pygame.draw.rect(play_surface, self.color,(block[0],block[1],10,10))


	def check_for_boundaries(self,game_over,sc_width,sc_height):
		if any((
			self.snake_head_pos[0] > sc_width-10
			or self.snake_head_pos[0] < 0,
			self.snake_head_pos[1] > sc_height-10
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



class Food:
	def __init__(self,sc_width,sc_height):
		self.sc_width = sc_width
		self.sc_height = sc_height

		self.food_pos = [random.randrange(1,sc_width/10)*10,random.randrange(1,sc_height/10)*10]


	def food_draw(self,play_surface,food_color):
		pygame.draw.rect(play_surface,food_color,(self.food_pos[0],self.food_pos[1],10,10))



class Menu:
	def __init__(self):
		self.win_size = [pygame.display.get_surface().get_size()[0],pygame.display.get_surface().get_size()[1]]
		self.main_menu = pygame.Surface((self.win_size[0],self.win_size[1]))
		self.menu_bg = (70,70,70)
		self.light_grey = (120,120,120)
		self.dark_grey_light = (90,90,90)
		self.btn_bg = self.light_grey
		self.text_color = (255,255,255)
		self.title_color = (0,150,0)

		self.all_btn_color=[self.light_grey,self.light_grey,self.light_grey]


	def initialization_menu(self):
		self.title = pygame.font.SysFont('arial',60)
		self.title = self.title.render('Snake-game',1,self.title_color)

		self.start_game = pygame.font.SysFont('arial',40)
		self.start_game = self.start_game.render('Start',1,self.text_color)

		self.exit_game = pygame.font.SysFont('arial',40)
		self.exit_game = self.exit_game.render('Exit',1,self.text_color)

		self.all_fields = [self.start_game,self.exit_game]


	def draw_items(self,play_surface,get_score):
		self.score_game = pygame.font.SysFont('arial',20)
		self.score_game = self.score_game.render(f'Maximum score | {get_score(0)["m_score"]}',1,self.text_color)

		self.last_score_game = pygame.font.SysFont('arial',20)
		self.last_score_game = self.last_score_game.render(f'Last score | {get_score(0)["l_score"]}',1,self.text_color)

		self.main_menu.fill(self.menu_bg)
		play_surface.blit(self.main_menu,(0,0))

		play_surface.blit(self.title,(self.win_size[0]//2 - self.title.get_rect()[2]//2,self.win_size[1]*0.1))

		play_surface.blit(self.score_game,(self.win_size[0]*0.1,self.win_size[1]*0.9))
		play_surface.blit(self.last_score_game,(self.win_size[0] - self.win_size[0]*0.1 - self.last_score_game.get_rect()[2],self.win_size[1]*0.9))

		for i in range(len(self.all_fields)):
			pygame.draw.rect(play_surface,self.all_btn_color[i],[self.win_size[0]*0.25,self.win_size[1]*0.3*(i+1)-30*i,self.win_size[0]//2,self.win_size[1]//6])

		for j in range(len(self.all_fields)):
			play_surface.blit(self.all_fields[j],(self.win_size[0]*0.25+(self.win_size[0]//2 - self.all_fields[j].get_rect()[2])/2,(self.win_size[1]*0.3*(j+1))- 30*j + (self.win_size[1]//6 - self.all_fields[j].get_rect()[3])/2))


	def check_key(self,get_score):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				sys.exit()


	def keys_animation(self):
		pos = pygame.mouse.get_pos()

		for i in range(len(self.all_fields)):
			if (self.win_size[0]*0.25 <= pos[0] <= self.win_size[0]*0.25 + self.win_size[0]//2) and (self.win_size[1]*0.3*(i+1)-30*i <= pos[1] <= self.win_size[1]*0.3*(i+1)-30*i + self.win_size[1]//6):
				self.all_btn_color[i] = self.dark_grey_light
			else:
				self.all_btn_color[i] = self.light_grey


	def begin_game(self,start,get_score,sc_width,sc_height,food_pos):
		mouse = pygame.mouse.get_pressed()
		pos = pygame.mouse.get_pos()
		if start == False and mouse[0]:
			if (self.win_size[0]*0.25 <= pos[0] <= self.win_size[0]*0.25 + self.win_size[0]//2) and (self.win_size[1]*0.3 <= pos[1] <= self.win_size[1]*0.3 + self.win_size[1]//6):
				start = True
				food_pos = [random.randrange(1,sc_width/10)*10,random.randrange(1,sc_height/10)*10]

			elif (self.win_size[0]*0.25 <= pos[0] <= self.win_size[0]*0.25 + self.win_size[0]//2) and (self.win_size[1]*0.3*2-30 <= pos[1] <= self.win_size[1]*0.3*2-30 + self.win_size[1]//6):
				sys.exit()

		return start,food_pos



game = Game()
snake = Snake(game.white)
food = Food(game.sc_width,game.sc_height)
menu = Menu()

game.initialization()

menu.initialization_menu()

while True:
	if game.start == False:
		menu.draw_items(game.sc,game.get_score)
		menu.keys_animation()

		menu.check_key(game.get_score)

		game.start,food.food_pos = menu.begin_game(game.start,game.get_score,game.sc_width,game.sc_height,food.food_pos)


	elif game.start == True:
		snake.change_to = game.check_key(snake.change_to)

		snake.change_direction()
		snake.change_head_pos()

		game.score, food.food_pos = snake.body_mechanism(game.sc_width,game.sc_height,food.food_pos,game.score)

		snake.snake_draw(game.sc,game.black)
		food.food_draw(game.sc,game.red)
		snake.check_for_boundaries(game.game_over,game.sc_width,game.sc_height),

		game.score_draw()

	game.update_screen()