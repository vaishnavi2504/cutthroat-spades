import Card
import pygame
from Utilities import load_image


class Player():
    def __init__(self, location):
        self.score = 0
        self.bid = 0
        self.cards = []
        self.location = location
        self.num_cards = 0
        self.playerIcon = PlayerIcon(location)

    def assign_card(self, card):
        if self.num_cards < 13:
            self.cards.append(card)
            self.num_cards += 1
            return True
        else:
            return False

class PlayerIcon(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('images/person-icon.png', -1)
        self.location = location
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        if location == 'N':
            self.rect.midtop = 650, 10
        elif location == 'S':
            self.rect.midbottom = 650, 760
        elif location == 'W':
            self.rect.midleft = 10, 400
        elif location == 'E':
            self.rect.midright = 1290, 400

