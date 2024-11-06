import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    # Create the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set up the clock for limiting FPS
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = [player]
    drawable = [player]
    
    # Initialize delta time
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black (background color)
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Limits to 60 FPS, converts milliseconds to seconds
        

if __name__ == "__main__":
    main()
