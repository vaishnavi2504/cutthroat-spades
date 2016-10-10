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
    players.append(Player.Player('N', background))
    players.append(Player.Player('S', background))
    players.append(Player.Player('W', background))
    players.append(Player.Player('E', background))

    player_sprites = pygame.sprite.RenderPlain((players[0].playerIcon, players[1].playerIcon,
                                               players[2].playerIcon, players[3].playerIcon))

    # start a new game
    start_game(cards, players)

    myfont = pygame.font.SysFont("monospace", 16)

    while 1:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        player_sprites.draw(screen)

        # Display scores/bids
        score_text = myfont.render("Tricks {0}".format(players[0].tricks_won), 1, (0, 0, 0))
        screen.blit(score_text, (background.get_width() / 2 + 80, 20))
        bid_text = myfont.render("Bid {0}".format(players[0].bid), 1, (0, 0, 0))
        screen.blit(bid_text, (background.get_width() / 2 + 80, 40))

        score_text = myfont.render("Tricks {0}".format(players[1].tricks_won), 1, (0, 0, 0))
        screen.blit(score_text, (background.get_width() / 2 + 80, background.get_height() - 100))
        bid_text = myfont.render("Bid {0}".format(players[1].bid), 1, (0, 0, 0))
        screen.blit(bid_text, (background.get_width() / 2 + 80, background.get_height() - 80))

        score_text = myfont.render("Tricks {0}".format(players[2].tricks_won), 1, (0, 0, 0))
        screen.blit(score_text, (background.get_width() - 100, background.get_height() / 2 + 80))
        bid_text = myfont.render("Bid {0}".format(players[2].bid), 1, (0, 0, 0))
        screen.blit(bid_text, (background.get_width() - 100, background.get_height() / 2 + 100))

        score_text = myfont.render("Tricks {0}".format(players[3].tricks_won), 1, (0, 0, 0))
        screen.blit(score_text, (15, background.get_height() / 2 + 80))
        bid_text = myfont.render("Bid {0}".format(players[3].bid), 1, (0, 0, 0))
        screen.blit(bid_text, (15, background.get_height() / 2 + 100))


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
