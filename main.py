import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    tick_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #allows the user to quit using the "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #fills screen with black (0,0,0)    
        screen.fill((0,0,0))

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)
        # refreshes the display
        pygame.display.flip()
        dt = tick_clock.tick(60) / 1000





if __name__ == "__main__":
    main()
