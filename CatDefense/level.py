import random
import pygame
import sys
from settings import *
from enemy import *
from ally import *

class Level:
    def __init__(self):
        self.displayScreen = pygame.display.get_surface()
        self.enemy_count = 5  # Total number of enemies to spawn in this level
        self.allies_count = 3  # Total number of allies to spawn in this level
        self.enemies_spawned = 0  # Counter for enemies already spawned
        self.allies_spawned = 0  # Counter for allies already spawned
        self.enemies = []  # List to hold enemy objects
        self.allies = []  # List to hold ally objects

    def run(self):
        # Spawn enemies until the desired count is reached
        while self.enemies_spawned < self.enemy_count:
            # Randomly choose a y-coordinate along the rightmost line of the screen
            spawn_y = random.randint(HEIGHT // 2, HEIGHT)
            enemy = Enemy((WIDTH, spawn_y), 'sai')  # Assuming you have an Enemy class that handles enemy attributes and behavior
            self.enemies.append(enemy)
            self.enemies_spawned += 1

        # Spawn allies until the desired count is reached
        while self.allies_spawned < self.allies_count:
            # Randomly choose a y-coordinate along the leftmost line of the screen
            spawn_y = random.randint(HEIGHT // 2, HEIGHT)
            ally = Ally((0, spawn_y), 'cat')  # Assuming you have an Ally class that handles ally attributes and behavior
            self.allies.append(ally)
            self.allies_spawned += 1

        # Update and draw enemies
        for enemy in self.enemies:
            enemy.updateEnemy()
            if enemy.detect(self.allies):  # Check if enemy detects any allies
                # Move towards the nearest ally and attack (you need to implement these methods)
                enemy.move_towards_nearest_target(self.allies)

            enemy.drawEnemy()

            # Update and draw allies
        for ally in self.allies:
            ally.updateAlly()
            if ally.detect(self.enemies):  # Check if ally detects any enemies
                # Move towards the nearest enemy and attack (you need to implement these methods)
                ally.move_towards_nearest_target(self.enemies)

            ally.drawAlly()