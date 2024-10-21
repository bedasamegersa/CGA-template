import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arcade Game")

# Set font for text rendering
font = pygame.font.SysFont("Arial", 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to display the menu
def draw_menu(selected_game):
    screen.fill(WHITE)  # Background color

    # Menu options
    games = ["1. Snake", "2. Tic-Tac-Toe", "3. Pong", "4. Flappy Bird", "5. Breakout", "6. Memory Game"]
    
    # Display each game option
    for i, game in enumerate(games):
        color = BLACK
        if i == selected_game:
            color = (0, 100, 255)  # Highlight selected game in blue

        text_surface = font.render(game, True, color)
        screen.blit(text_surface, (100, 100 + i * 40))

    pygame.display.update()

# Placeholder functions for games
def snake_game():
    print("Starting Snake Game...")
    # Insert Snake game logic here

def tic_tac_toe_game():
    print("Starting Tic-Tac-Toe Game...")
    # Insert Tic-Tac-Toe game logic here

# Add more game functions as needed

# Main loop function
def arcade_main_loop():
    selected_game = 0
    running = True

    while running:
        draw_menu(selected_game)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_game = (selected_game - 1) % 6  # Cycle up
                elif event.key == pygame.K_DOWN:
                    selected_game = (selected_game + 1) % 6  # Cycle down
                elif event.key == pygame.K_RETURN:
                    # Launch the selected game
                    if selected_game == 0:
                        snake_game()
                    elif selected_game == 1:
                        tic_tac_toe_game()
                    # Add more conditions for other games

        # Keep frame rate stable
        pygame.time.Clock().tick(30)

# Start the arcade loop
if __name__ == "__main__":
    arcade_main_loop()
