import Card
import pygame
from Utilities import load_image


class Player():
    def __init__(self, location, background):
        self.bid = 0
        self.tricks_won = 0
        self.cards = []
        self.location = location
        self.num_cards = 0
        self.background = background
        self.playerIcon = PlayerIcon(location, background)

    def assign_card(self, card):
        if self.num_cards < 13:
            self.cards.append(card)
            self.num_cards += 1
            return True
        else:
            return False

class PlayerIcon(pygame.sprite.Sprite):
    def __init__(self, location, background):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('images/person-icon.png', -1)
        self.location = location
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        font = pygame.font.Font(None, 36)
        if location == 'N':
            self.rect.midtop = background.get_width() / 2, 10
            text = font.render("Tim", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=100)
            background.blit(text, textpos)
        elif location == 'S':
            self.rect.midbottom = 650, 760
            text = font.render("You", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2, centery=background.get_height() - 130)
            background.blit(text, textpos)
        elif location == 'W':
            self.rect.midleft = 10, 400
            text = font.render("Gary", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=35, centery=background.get_height() / 2 + 50)
            background.blit(text, textpos)
        elif location == 'E':
            self.rect.midright = 1290, 400
            text = font.render("Sam", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() - 40, centery=background.get_height() / 2 + 50)
            background.blit(text, textpos)

