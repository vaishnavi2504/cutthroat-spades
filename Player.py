import Card


class Player():
    def __init__(self):
        self.score = 0
        self.bid = 0
        self.cards = []
        self.num_cards = 0

    def assign_card(self, card):
        if self.num_cards < 13:
            self.cards.append(card)
            self.num_cards += 1
            return True
        else:
            return False
