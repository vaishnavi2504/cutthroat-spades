import pygame
from pygame.locals import *
from Utilities import *
import random
import Player
import Card


def main():
    # init everything
    pygame.init()
    screen = pygame.display.set_mode((1300, 800))
    pygame.display.set_caption('Cutthroat Killer Spades')
    clock = pygame.time.Clock()

    # show background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 102, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # define a dictionary with all the cards
    cards = init_cards()

    # define 4 players
    players = []
    players.append(Player.Player())
    players.append(Player.Player())
    players.append(Player.Player())
    players.append(Player.Player())

    # start a new game
    start_game(cards, players)

    while 1:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        # allsprites.draw(screen)
        pygame.display.flip()


def start_game(cards, players):
    assign_cards(cards, players)


def init_cards():
    cards = {}

    for suit in suits:
        for value in values:
            cards[suit+value] = Card.Card(suit, value)

    return cards


def assign_cards(cards, players):
    for card in cards:
        ranValue = random.randint(0, 3)
        while not (players[ranValue].assign_card(cards[card])):
            ranValue = random.randint(0, 3)

    pass


if __name__ == '__main__':
    main()
