import sys
import random
import pygame


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

		self.all_btn_color=[self.light_grey]*2


	def initialization_menu(self):
		self.title = pygame.font.SysFont('arial',60)
		self.title = self.title.render('Snake-game',1,self.title_color)

		self.start_game = pygame.font.SysFont('arial',40)
		self.start_game = self.start_game.render('Start',1,self.text_color)

		self.exit_game = pygame.font.SysFont('arial',40)
		self.exit_game = self.exit_game.render('Exit',1,self.text_color)

		self.all_fields = [self.start_game,self.exit_game]
		self.select_menu_pos = 0


	def draw_items(self,play_surface,get_score):
		self.score_game = pygame.font.SysFont('arial',20)
		self.score_game = self.score_game.render(f'Maximum score | {get_score(0)["m_score"]}',1,self.text_color)

		self.last_score_game = pygame.font.SysFont('arial',20)
		self.last_score_game = self.last_score_game.render(f'Last score | {get_score(0)["l_score"]}',1,self.text_color)

		self.main_menu.fill(self.menu_bg)
		play_surface.blit(self.main_menu,(0,0))

		play_surface.blit(self.title,(self.win_size[0]//2 - self.title.get_rect()[2]//2,self.win_size[1]*0.1))

		play_surface.blit(self.score_game,(self.win_size[0]*0.1,self.win_size[1]*0.9))
		play_surface.blit(self.last_score_game,(self.win_size[0] - self.win_size[0]*0.1 - \
			self.last_score_game.get_rect()[2],self.win_size[1]*0.9))

		for i in range(len(self.all_fields)):
			pygame.draw.rect(play_surface,self.all_btn_color[i],[self.win_size[0]*0.25,self.win_size[1]*0.3*(i+1)-30*i,
				self.win_size[0]//2,self.win_size[1]//6])
			play_surface.blit(self.all_fields[i],(self.win_size[0]*0.25+(self.win_size[0]//2 - \
			self.all_fields[i].get_rect()[2])/2,(self.win_size[1]*0.3*(i+1))- 30*i + \
			(self.win_size[1]//6 - self.all_fields[i].get_rect()[3])/2))


	def check_key(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				sys.exit()
			elif i.type == pygame.KEYDOWN:
				if i.key == pygame.K_w or i.key == pygame.K_s:
					self.select_menu_pos ^= 1


	def keys_animation(self):
		self.all_btn_color[self.select_menu_pos] = self.dark_grey_light
		self.all_btn_color[self.select_menu_pos-1] = self.light_grey


	def begin_game(self,start,sc_width,sc_height,food_pos, coef):
		k = pygame.key.get_pressed()

		if k[pygame.K_RETURN] or k[pygame.K_a] or k[pygame.K_d]:
			if self.select_menu_pos == 0:
				start = True
				food_pos = [random.randrange(1, int(sc_width/coef))*coef,random.randrange(1,int(sc_height/coef))*coef]
			else:
				sys.exit()

		return start,food_pos