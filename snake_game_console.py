import os
import random
import time

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game board
def draw_board(width, height, snake, food, score):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Place snake on board
    for x, y in snake:
        if 0 <= x < width and 0 <= y < height:
            board[y][x] = 'O'
    
    # Place food on board
    food_x, food_y = food
    if 0 <= food_x < width and 0 <= food_y < height:
        board[food_y][food_x] = 'X'
    
    # Print the board
    print(f"Score: {score}")
    print("-" * (width + 2))
    for row in board:
        print("|" + "".join(row) + "|")
    print("-" * (width + 2))

# Main game function
def main():
    width = 20
    height = 10
    
    # Initial snake position
    snake = [(width // 2, height // 2)]
    direction = (1, 0)  # Moving right initially
    
    # Initial food position
    food = (random.randint(0, width-1), random.randint(0, height-1))
    
    score = 0
    game_over = False
    
    print("Welcome to Snake Game!")
    print("Use WASD keys to move: W=Up, A=Left, S=Down, D=Right")
    print("Press Q to quit")
    input("Press Enter to start...")
    
    while not game_over:
        clear_screen()
        draw_board(width, height, snake, food, score)
        
        # Get user input
        user_input = input("Move (W/A/S/D) or Q to quit: ").upper()
        
        if user_input == 'Q':
            break
        elif user_input == 'W' and direction != (0, 1):
            direction = (0, -1)
        elif user_input == 'S' and direction != (0, -1):
            direction = (0, 1)
        elif user_input == 'A' and direction != (1, 0):
            direction = (-1, 0)
        elif user_input == 'D' and direction != (-1, 0):
            direction = (1, 0)
        
        # Move snake
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if not (0 <= new_head[0] < width and 0 <= new_head[1] < height):
            game_over = True
            continue
        
        # Check self collision
        if new_head in snake:
            game_over = True
            continue
        
        snake.insert(0, new_head)
        
        # Check food collision
        if new_head == food:
            score += 1
            food = (random.randint(0, width-1), random.randint(0, height-1))
            # Ensure food doesn't spawn on snake
            while food in snake:
                food = (random.randint(0, width-1), random.randint(0, height-1))
        else:
            snake.pop()  # Remove tail if no food eaten
        
        time.sleep(0.1)  # Small delay for game speed
    
    clear_screen()
    print(f"Game Over! Final Score: {score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
