import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define colors (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set block size and speed
BLOCK_SIZE = 20
FPS = 10

# Set up the display
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font for score and game over text
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_food(food_pos):
    """Draw the food on the screen."""
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_score(score):
    """Draw the current score on the screen."""
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

def game_over_message(score):
    """Display game over message and final score."""
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, WHITE)
    score_text = font.render("Final Score: " + str(score), True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(game_over_text, [WIDTH // 2 - 100, HEIGHT // 2 - 50])
    screen.blit(score_text, [WIDTH // 2 - 100, HEIGHT // 2])
    screen.blit(restart_text, [WIDTH // 2 - 150, HEIGHT // 2 + 50])
    pygame.display.update()

def main():
    """Main game function."""
    game_over = False
    game_close = False

    # Initial snake position and body
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0
    snake_body = []
    length_of_snake = 1

    # Initial food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    score = 0

    while not game_over:
        while game_close:
            game_over_message(score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        main()  # Restart the game

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Check boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update snake position
        x += x_change
        y += y_change

        # Fill screen
        screen.fill(BLACK)

        # Draw food
        draw_food([food_x, food_y])

        # Update snake body
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check self-collision
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # Draw snake
        draw_snake(snake_body)

        # Draw score
        draw_score(score)

        # Update display
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
            score += 1

        # Control game speed
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
