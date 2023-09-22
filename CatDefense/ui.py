import pygame
from settings import *

class UI:
    def __init__(self):
        self.game_paused = False
        self.ally = [1, 0, 0, 0, 0]
        self.allyRect = [None] * len(self.ally)  # Initialize the allyRect list

    def showButton(self):
        button_width = 50  # Width of each button
        button_height = 30  # Height of each button
        button_margin = 10  # Margin between buttons

        x = 10  # Starting x-coordinate for the first button
        y = 10  # Starting y-coordinate for all buttons

        for idx, ally_value in enumerate(self.ally):
            self.allyRect[idx] = pygame.Rect(x, y, button_width, button_height)
            pygame.draw.rect(pygame.display.get_surface(), (10, 10, 0), self.allyRect[idx])

            x += button_width + button_margin  # Update x-coordinate for the next button

        pygame.display.update()

    def handleButtonClick(self, pos):
        for idx, rect in enumerate(self.allyRect):
            if rect.collidepoint(pos):
                if self.ally[idx] != 0:
                    self.generateAlly(idx)

    def generateAlly(self, idx):
        ally_type = list(allyData.keys())[idx]  # Get the ally type based on the index

        # Retrieve ally attributes from allyData dictionary
        health = allyData[ally_type]['health']
        exp = allyData[ally_type]['exp']
        damage = allyData[ally_type]['damage']
        attack_type = allyData[ally_type]['attack_type']
        attack_sound = allyData[ally_type]['attack_sound']
        speed = allyData[ally_type]['speed']
        resistance = allyData[ally_type]['resistance']
        attack_radius = allyData[ally_type]['attack_radius']
        graphic = allyData[ally_type]['graphic']




