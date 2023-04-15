import pygame
from game_player import Player
from game_platform import Platform

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
SKY_BLUE = (135, 206, 250)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("2D Platformer")

# Create Player object
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60, 50, 60, SCREEN_WIDTH)

# Create Platform object
platform = Platform((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT - 150, 200, 10, BLACK)

# Define cloud positions
clouds = [(100, 100), (400, 50), (600, 120)]

# Game loop
running = True
while running:
    # Control the frame rate of the game loop
    pygame.time.Clock().tick(30)

    # Check for events
    for event in pygame.event.get():
        # If the close button is clicked, exit the game loop
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Player movement and jumping
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP] or keys[pygame.K_TAB]:
        player.jump()

    # Update player position
    player.update()

    # Platform collision detection
    if player.y + player.height >= platform.y and player.x <= platform.x + platform.width and player.x + player.width >= platform.x:
        player.on_platform_collision(platform)

    # Fill the screen with a color (R, G, B)
    screen.fill(SKY_BLUE)

    # Draw clouds
    for cloud_pos in clouds:
        pygame.draw.ellipse(screen, WHITE, (cloud_pos[0], cloud_pos[1], 80, 50))

    # Draw the player character (stickman)
    player.draw(screen, BLACK)

    # Draw the platform
    platform.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
