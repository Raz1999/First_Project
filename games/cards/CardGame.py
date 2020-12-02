from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards

class CardGame():
    def __init__(self, name1, name2, num_cards = 10):
        self.num_cards=num_cards
        self.player1 = Player(name1, num_cards)
        self.player2 = Player(name2, num_cards)
        self.game_deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        if len(self.game_deck.deck)==52:
            self.game_deck.shuffle_deck()
            for i in range(self.num_cards):
                r_card=self.game_deck.deal_one()
                self.player1.set_hand(r_card)

            for i in range(self.num_cards):
                r2_card=self.game_deck.deal_one()
                self.player2.set_hand(r2_card)
        else:
            print("Error")

    def get_winner(self):
        if len(self.player1.pack)<len(self.player2.pack):
            return print(f'The winner is: {self.player1.name}')
        elif len(self.player1.pack)>len(self.player2.pack):
            return print(f'The winner is: {self.player2.name}')
        else:
            # len(self.player1.pack)==len(self.player2.pack)
            return print("There is no winner - tied")