import pygame

# Constants for Tic-Tac-Toe
GRID_SIZE = 3
CELL_SIZE = 200
LINE_WIDTH = 15

# Colors
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Function to run the Tic-Tac-Toe game
def tic_tac_toe_game(screen, s_height,s_width,font,white,black):
    board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_turn = 'X'
    game_over = False
    winner = None

    def draw_board():
        screen.fill(white)
        
        # Draw grid lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (s_width, i * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, s_height), LINE_WIDTH)

        # Draw X's and O's
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board[row][col] == 'X':
                    draw_x(row, col)
                elif board[row][col] == 'O':
                    draw_o(row, col)
        
        pygame.display.update()

    def draw_x(row, col):
        pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + 50, row * CELL_SIZE + 50), 
                         (col * CELL_SIZE + CELL_SIZE - 50, row * CELL_SIZE + CELL_SIZE - 50), LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + CELL_SIZE - 50, row * CELL_SIZE + 50), 
                         (col * CELL_SIZE + 50, row * CELL_SIZE + CELL_SIZE - 50), LINE_WIDTH)

    def draw_o(row, col):
        pygame.draw.circle(screen, O_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), 
                           CELL_SIZE // 2 - 50, LINE_WIDTH)

    def check_winner():
        # Check rows, columns, and diagonals for a winner
        for i in range(GRID_SIZE):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]
        return None

    def is_draw():
        for row in board:
            if None in row:
                return False
        return True

    def display_winner(winner):
        message = f"Player {winner} wins!" if winner else "It's a draw!"
        display_message(message, black)
        pygame.display.update()
        pygame.time.delay(2000)

    def display_message(msg, color):
        message_surface = font.render(msg, True, color)
        screen.blit(message_surface, (s_width // 6, s_height // 3))

    while not game_over:
        draw_board()

        # Event handling for Tic-Tac-Toe input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x, mouse_y = event.pos
                clicked_row = mouse_y // CELL_SIZE
                clicked_col = mouse_x // CELL_SIZE

                # Make a move if the cell is empty
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player_turn
                    winner = check_winner()

                    if winner:
                        display_winner(winner)
                        game_over = True
                    elif is_draw():
                        display_winner(None)
                        game_over = True
                    else:
                        # Switch turns
                        player_turn = 'O' if player_turn == 'X' else 'X'

        # If game over, show a restart option
        if game_over:
            screen.fill(white)
            display_message("Game Over! Press C to Play Again or Q to Quit", black)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return
                    if event.key == pygame.K_c:
                        tic_tac_toe_game()  # Restart the game

    return  # Return to the main menu
