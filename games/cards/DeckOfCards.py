import random
from games.cards.Card import Card
class DeckOfCards():
    def __init__(self):
        self.deck = []
        self.values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.suits=[u'\u2666',u'\u2660',u'\u2665',u'\u2663']
        for i in self.values:
            for j in self.suits:
                card = Card(i,j)
                self.deck.append(card)

    def shuffle_deck(self,):
        random.shuffle(self.deck)
        return print("The deck is shuffled")

    def deal_one(self):
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card


    def show(self):
       return print(f"{self.deck}")
