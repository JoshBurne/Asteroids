from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x, y, radius) 
        self.radius = radius
        
        
        
    def draw (self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            new_velocity_pos = self.velocity.rotate(random_angle)
            new_velocity_neg = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velocity_pos * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velocity_neg * 1.2
            
            

