from unittest import TestCase
from First_Project.games.cards.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):

    def test_init(self):
        deck1 = DeckOfCards()
        deck2 = DeckOfCards()


    def test_shuffle_deck(self):
        deck1 = DeckOfCards()
        self.assertTrue(deck1.shuffle_deck, 'The deck is shuffled')

    def test_shuffle_deck1(self):
        deck1 = DeckOfCards()
        deck2 = DeckOfCards()


    def test_deal_one(self):
        deck1 = DeckOfCards()
        print(deck1.deal_one())
        self.assertTrue(len(deck1.deck),51)


    def test_show(self):
        deck1 = DeckOfCards()
        check = print(deck1.deck)
        self.assertEqual(deck1.show(),check)
