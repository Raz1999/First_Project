from games.cards.DeckOfCards import DeckOfCards
import random
class Player():
    def __init__(self, name, len_pack):
        if len_pack > 26:
            len_pack = 26
        self.name = name
        self.len_pack = len_pack
        self.pack = []


    def set_hand(self,main_pack):
        self.pack.append(main_pack)

    def get_card(self):
        rand_card = random.choice(self.pack)
        self.pack.remove(rand_card)
        return rand_card

    def add_card(self, card):
        self.pack.append(card)

    def show(self):
        print(f"player name: {self.name}\nplayer hand: {self.pack}")
