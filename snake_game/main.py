from snake_game.game import Game
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.menu import Menu



class Start:

	def __init__(self):
		self.game = Game()
		self.snake = Snake(self.game.white, self.game.coef, self.game.sc_width, self.game.sc_height)
		self.food = Food(self.game.sc_width, self.game.sc_height, self.game.coef)
		self.menu = Menu()

		self.game.initialization()
		self.menu.initialization_menu()

	@property
	def game_status(self):
		return self.game.start


	def menu(self):
		self.menu.draw_items(self.game.sc, self.game.get_score)
		self.menu.keys_animation()

		self.menu.check_key()

		self.game.start, self.food.food_pos = self.menu.begin_game(self.game.start, self.game.sc_width,
																	 self.game.sc_height, self.food.food_pos,
																	 self.game.coef)


	def snake_game(self):
		self.snake.change_to = self.game.check_key(self.snake.change_to)

		self.snake.change_direction()

		self.snake.change_head_pos(self.game.coef, self.game.sc_width, self.game.sc_height)

		self.game.score, self.food.food_pos = self.snake.body_mechanism(self.game.sc_width, self.game.sc_height,
																		self.food.food_pos, self.game.score,
																		self.game.coef)

		self.snake.snake_draw(self.game.sc, self.game.black, self.game.coef)
		self.food.food_draw(self.game.sc, self.game.red, self.game.coef)
		self.snake.check_for_boundaries(self.game.game_over, self.game.sc_width, self.game.sc_height, self.game.coef)
		self.game.score_draw()


	def update_screen(self):
		return self.game.update_screen()


	def game_desision(self):
		if self.game_status:
			return self.menu()
		elif not self.game_status:
			return self.snake_game()



start = Start()

while True:
	start.game_desision()
	start.update_screen()