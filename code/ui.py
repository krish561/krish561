import pygame
from settings import * 

class UI:
	def __init__(self):
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)

		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			path = magic['graphic']
			magic = pygame.image.load(path).convert_alpha()
			self.magic_graphics.append(magic)

	def show_bar(self, current, max_amount, bg_rect, color):
		# draw bg 
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface, color, current_rect)
		pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

	def show_exp(self, exp):
		text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright=(x, y))

		pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
		self.display_surface.blit(text_surf, text_rect)
		pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

	def selection_box(self, left, top, has_switched):
		bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
		else:
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
		return bg_rect

	def weapon_overlay(self, weapon_index, has_switched):
		bg_rect = self.selection_box(10, 630, has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

		self.display_surface.blit(weapon_surf, weapon_rect)

	def magic_overlay(self, magic_index, has_switched):
		bg_rect = self.selection_box(80, 635, has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center=bg_rect.center)

		self.display_surface.blit(magic_surf, magic_rect)

	def display_game_over(self):
		# Display Game Over Screen
		game_over_surf = self.font.render("GAME OVER", False, (255, 0, 0))
		game_over_rect = game_over_surf.get_rect(center=self.display_surface.get_rect().center)

		self.display_surface.fill((0, 0, 0))  # Fill screen with black
		self.display_surface.blit(game_over_surf, game_over_rect)
		pygame.display.update()

	def display(self, player):
		if player.health > 0:
			self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
			self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

			self.show_exp(player.exp)

			self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
			self.magic_overlay(player.magic_index, not player.can_switch_magic)
		else:
			self.display_game_over()
   
def show_pause_menu(self):
        """Display the pause menu."""
        # Create a semi-transparent overlay
        overlay = pygame.Surface(self.display_surface.get_size())
        overlay.set_alpha(128)  # Set transparency level
        overlay.fill((0, 0, 0))  # Black overlay

        # Draw the overlay
        self.display_surface.blit(overlay, (0, 0))

        # Pause menu text
        pause_text = self.font.render("PAUSED", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(self.display_surface.get_width() / 2, self.display_surface.get_height() / 3))

        # Resume and quit options
        resume_text = self.font.render("Press R to Resume", True, (255, 255, 255))
        resume_rect = resume_text.get_rect(center=(self.display_surface.get_width() / 2, self.display_surface.get_height() / 2))

        quit_text = self.font.render("Press Q to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.display_surface.get_width() / 2, self.display_surface.get_height() / 2 + 50))

        # Draw the text on the screen
        self.display_surface.blit(pause_text, pause_rect)
        self.display_surface.blit(resume_text, resume_rect)
        self.display_surface.blit(quit_text, quit_rect)

        pygame.display.update()