import pygame
from settings import *

class Ally:
    def __init__(self, spawn_position, allyType):
        self.displayScreen = pygame.display.get_surface()
        self.position = pygame.Vector2(spawn_position)  # Enemy position as a 2D vector
        self.velocity = pygame.Vector2(allyData[allyType]['speed'], 0)  # Enemy velocity (movement speed)
        self.image = pygame.image.load(allyData[allyType]['graphic']).convert_alpha()
        self.rect = self.image.get_rect()
    def updateAlly(self):
        # Update the position based on the velocity
        self.position += self.velocity

        # Update the rectangular bounding box position
        self.rect.topleft = self.position

        # Perform additional logic, such as checking for collisions or applying enemy behavior

    def detect(self, allies):
        detection_range = 200  # Define the detection range for the enemy
        for ally in allies:
            distance = self.position.distance_to(ally.position)
            if distance <= detection_range:
                return True
        return False
    def drawAlly(self):
        self.displayScreen.blit(self.image, self.position)

    def move_towards_nearest_target(self, targets):
        if not targets:
            return

        nearest_target = min(targets, key=lambda target: self.position.distance_to(target.position))
        direction = nearest_target.position - self.position
        direction.normalize_ip()

        # Set the enemy's velocity to move towards the nearest target
        self.velocity *= direction