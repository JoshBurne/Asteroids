import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions_check(self, CircleShape):
        print(f"Self position type: {type(self.position)}")
        print(f"Other position type: {type(CircleShape.position)}")
        print(f"Self position: {self.position}")
        print(f"Other position: {CircleShape.position}")
        distance = self.position.distance_to(CircleShape.position)
        combined_r = self.radius + CircleShape.radius
        if distance <= combined_r:
            return True
        return False