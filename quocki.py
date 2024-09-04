import pygame
import math
import time

# Constants
WIDTH, HEIGHT = 600, 400
RED = (218, 37, 29)
YELLOW = (255, 255, 0)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chào Mừng 79 Năm Ngày Quốc Khánh CHXHCN Việt Nam")
clock = pygame.time.Clock()


# Function to draw the star
def draw_star(surface, color, center, size, fill_percentage=100):
    """Draw a star with fill percentage on the surface."""
    points = []
    for i in range(5):
        angle = math.pi * 2 * i / 5 - math.pi / 2
        outer_point = (
            center[0] + size * math.cos(angle),
            center[1] + size * math.sin(angle)
        )
        points.append(outer_point)

        inner_angle = angle + math.pi / 5
        inner_point = (
            center[0] + size * 0.38 * math.cos(inner_angle),
            center[1] + size * 0.38 * math.sin(inner_angle)
        )
        points.append(inner_point)

    # Calculate the number of points to draw based on fill percentage
    num_points = max(3, int(len(points) * fill_percentage / 100))
    pygame.draw.polygon(surface, color, points[:num_points])


# Function to handle drawing the background fill and star
def draw_scene(fill_percentage):
    """Draw the scene including the red background and the yellow star."""
    # Fill background red based on percentage
    fill_width = int(WIDTH * fill_percentage / 100)
    screen.fill((0, 0, 0))  # Clear the screen with black
    pygame.draw.rect(screen, RED, (0, 0, fill_width, HEIGHT))

    # Draw star fill after 50% background fill
    if fill_percentage > 50:
        star_center = (WIDTH // 2, HEIGHT // 2)
        star_size = min(WIDTH, HEIGHT) // 5
        star_fill = (fill_percentage - 50) * 2  # Adjust star fill percentage
        draw_star(screen, YELLOW, star_center, star_size, star_fill)


# Main loop
def main():
    fill_percentage = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the scene
        draw_scene(fill_percentage)

        # Update the display
        pygame.display.flip()

        # Increment the fill percentage and reset if complete
        if fill_percentage < 100:
            fill_percentage += 0.5
        else:
            time.sleep(1)  # Pause for 1 second when finished
            fill_percentage = 0  # Reset to repeat the effect

        # Limit the frame rate to FPS
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()


# Run the main loop
if __name__ == "__main__":
    main()
