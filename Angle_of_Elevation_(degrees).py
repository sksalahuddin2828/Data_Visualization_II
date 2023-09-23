import numpy as np
import matplotlib.pyplot as plt
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angle of Elevation and Depression")

# Define the observer and target positions
observer_x, observer_y = WIDTH // 2, HEIGHT - 50
target_x, target_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Calculate angle of elevation
    angle_elevation = np.degrees(np.arctan2(target_y - observer_y, target_x - observer_x))

    # Draw the observer and target
    pygame.draw.circle(screen, RED, (observer_x, observer_y), 10)
    pygame.draw.circle(screen, RED, (target_x, target_y), 10)

    # Draw the line of sight
    pygame.draw.line(screen, RED, (observer_x, observer_y), (target_x, target_y), 2)

    # Display the angle of elevation
    font = pygame.font.Font(None, 36)
    text = font.render(f"Angle of Elevation: {angle_elevation:.2f} degrees", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
