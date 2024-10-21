import random
import pygame
import sys
# Constants for the Snake game
SNAKE_SPEED = 15
SNAKE_SIZE = 20

# Function to run the Snake game
def snake_game(screen, s_width, s_height, font, white, black):
    # Initial settings
    clock = pygame.time.Clock()
    game_over = False
    game_close = False

    # Snake's initial position and movement
    x_pos = s_width // 2
    y_pos = s_height // 2
    x_change = 0
    y_change = 0

    snake_body = []
    snake_length = 1

    # Food's initial position
    food_x = random.randrange(0, s_width - SNAKE_SIZE, SNAKE_SIZE)
    food_y = random.randrange(0, s_height - SNAKE_SIZE, SNAKE_SIZE)

    def draw_snake(snake_body):
        for segment in snake_body:
            pygame.draw.rect(screen, black, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

    def display_message(msg, color):
        message_surface = font.render(msg, True, color)
        screen.blit(message_surface, [s_width // 6, s_height // 3])

    while not game_over:
        # Game over loop
        while game_close:
            screen.fill(white)
            display_message("Game Over! Press C to Play Again or Q to Quit", black)
            pygame.display.update()

            # Game over event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return  # Return to main menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return  # Return to main menu
                    if event.key == pygame.K_c:
                        snake_game(screen=screen, s_height=s_height,s_width=s_width,font=font,white=white,black=black)

        # Event handling for snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -SNAKE_SIZE
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = SNAKE_SIZE

        # Snake position update
        x_pos += x_change
        y_pos += y_change

        # Check for collisions with screen borders
        if x_pos >= s_width or x_pos < 0 or y_pos >= s_height or y_pos < 0:
            game_close = True

        # Update screen and snake body
        screen.fill(white)
        pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])  # Draw food
        snake_head = [x_pos, y_pos]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collision with self
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_body)
        pygame.display.update()

        # Check if food is eaten
        if x_pos == food_x and y_pos == food_y:
            food_x = random.randrange(0, s_width - SNAKE_SIZE, SNAKE_SIZE)
            food_y = random.randrange(0, s_height - SNAKE_SIZE, SNAKE_SIZE)
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    # pygame.quit()
    # sys.exit()
    return # After game_over, return to the main menu
