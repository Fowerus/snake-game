import sys
import json
import pygame



class Game:

	def __init__(self):
		self.red = (200,0,0)
		self.white = (255,255,255)
		self.brown = (150,75,0)
		self.black = (0,0,0)
		self.grey = (40,40,40)
		self.menu_grey = (20,20,20)

		self.sc_width = self.sc_height = 600

		self.score = 0
		self.start = False
		self.coef = 30

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