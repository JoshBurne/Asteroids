import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        #allows the user to quit using the "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fills screen with black (0,0,0)    
        screen.fill((0,0,0))
        # refreshes the display
        pygame.display.flip()




if __name__ == "__main__":
    main()
