import pygame, sys
import argparse
from settings import *
from level import Level

class Game:
    def __init__(self, width, height):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Start menu flag
        self.start_menu = True

        # Load background image for animation
        self.bg_image = pygame.image.load('../graphics/background.png').convert()
        self.bg_width = self.bg_image.get_width()
        self.bg_x = 0  # Start position of background

        # Load custom button images
        self.button_image = pygame.image.load('../graphics/button_image.png').convert_alpha()
        self.exit_button_image = pygame.image.load('../graphics/exit_button_image.png').convert_alpha()
        self.button_rect = self.button_image.get_rect(center=(width / 2.2, height / 1.5))
        self.exit_button_rect = self.exit_button_image.get_rect(center=(width / 1.7, height / 1.5))

        # Font for UI elements (Pause Menu, etc.)
        self.font = pygame.font.Font(UI_FONT, 50)
        
        
    def animate_background(self):
        """Scroll the background horizontally."""
        self.bg_x -= 0  # Move background to the left (set this to a non-zero value if you want scrolling)
        if self.bg_x <= -self.bg_width:  # Reset position if it scrolls completely
            self.bg_x = 0

        # Draw two images to create the looping effect
        self.screen.blit(self.bg_image, (self.bg_x, 0))
        self.screen.blit(self.bg_image, (self.bg_x + self.bg_width, 0))

    def show_start_menu(self):
        """Function to display the start menu."""
        while self.start_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.start_game()
                    if self.exit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                        
            # Animate the background
            self.animate_background()

            # Render the title text
            font = pygame.font.Font(None, 74)
            title_text = font.render("Zelda Clone", True, (255, 255, 255))
            self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, self.screen.get_height() / 6))

            # Draw the custom buttons
            self.screen.blit(self.button_image, self.button_rect)
            self.screen.blit(self.exit_button_image, self.exit_button_rect)
            
            pygame.display.flip()
            self.clock.tick(FPS)

    def start_game(self):
        """Action to start the game."""
        self.start_menu = False

    def show_pause_menu(self):
        """Display the pause menu when the game is paused."""
        paused = True

        # Create a semi-transparent overlay
        overlay = pygame.Surface(self.screen.get_size())
        overlay.set_alpha(128)  # Set transparency level
        overlay.fill((0, 0, 0))  # Black overlay

        # Draw the overlay
        self.screen.blit(overlay, (0, 0))

        # Pause menu text
        pause_text = self.font.render("PAUSED", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 3))
        
        # Render the title text
        # font = pygame.font.Font(None, 74)
        title_text = self.font.render("Zelda_clone", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 1))
        # title_text = font.render("Zelda Clone", True, (255, 255, 255))
        # self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, self.screen.get_height() / 6))        
        
        # Resume and quit buttons
        button_font = pygame.font.Font(UI_FONT, 40)
        resume_text = button_font.render("Resume", True, (255, 255, 255))
        resume_rect = resume_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))

        quit_text = button_font.render("Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 + 60))

        # Draw the text and buttons on the screen
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
        self.screen.blit(quit_text, quit_rect)

        pygame.display.update()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press 'Esc' to resume
                        paused = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_rect.collidepoint(event.pos):
                        paused = False
                    if quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.clock.tick(15)  # Limit frame rate during pause

    def run(self):
        # Show start menu before starting the game
        self.show_start_menu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    if event.key == pygame.K_ESCAPE:  # Press 'Esc' to pause
                        self.show_pause_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the game with custom resolution.")
    parser.add_argument('--width', type=int, default=WIDTH, help='Width of the game window.')
    parser.add_argument('--height', type=int, default=HEIGTH, help='Height of the game window.')
    args = parser.parse_args()

    game = Game(args.width, args.height)
    game.run()
