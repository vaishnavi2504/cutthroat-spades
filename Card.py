import pygame
from Utilities import load_image


class Card(pygame.sprite.Sprite):
    def __init__(self, suit, value):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.suit = suit
        self.value = value
        self.image, self.rect = load_image('images/card-back.jpg', -1)

    def set_position(self, pos):
        self.rect.midtop = pos

