import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SIZE = 50
OBSTACLE_SIZE = 30
CHARACTER_SPEED = 5
OBSTACLE_SPEED = 3
OBSTACLE_GAP = 200

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Create the character
character = pygame.Rect(SCREEN_WIDTH // 2 - CHARACTER_SIZE // 2, SCREEN_HEIGHT - CHARACTER_SIZE, CHARACTER_SIZE, CHARACTER_SIZE)

# Create the obstacles
obstacle1 = pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE), -OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE)
obstacle2 = pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE), -OBSTACLE_SIZE - OBSTACLE_GAP, OBSTACLE_SIZE, OBSTACLE_SIZE)

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character.left > 0:
        character.x -= CHARACTER_SPEED
    if keys[pygame.K_RIGHT] and character.right < SCREEN_WIDTH:
        character.x += CHARACTER_SPEED

    # Move obstacles
    obstacle1.y += OBSTACLE_SPEED
    obstacle2.y += OBSTACLE_SPEED

    # Check for collision with obstacles
    if character.colliderect(obstacle1) or character.colliderect(obstacle2):
        running = False

    # Respawn obstacles when they go off-screen
    if obstacle1.top > SCREEN_HEIGHT:
        obstacle1 = pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE), -OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE)
    if obstacle2.top > SCREEN_HEIGHT:
        obstacle2 = pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE), -OBSTACLE_SIZE - OBSTACLE_GAP, OBSTACLE_SIZE, OBSTACLE_SIZE)

    # Clear the screen
    screen.fill(WHITE)

    # Draw character and obstacles
    pygame.draw.rect(screen, RED, character)
    pygame.draw.rect(screen, RED, obstacle1)
    pygame.draw.rect(screen, RED, obstacle2)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()