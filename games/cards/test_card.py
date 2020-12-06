from unittest import TestCase
from games.cards.Card import Card

class TestCard(TestCase):

    def test_Repr1(self):
        card1 = Card(2,u'\u2666')
        self.assertTrue(card1.value,2)
        self.assertTrue(card1.suit,u'\u2666')
        print(card1)

    def test_Repr2(self):
        card2 = Card(-4,None)
        self.assertTrue(card2.value,-4)

    def test_Repr3(self):
        card3 = Card(None, u'\u2660')
        self.assertTrue(card3.suit,u'\u2660')
        print(card3)

    def test_Repr4(self):
        card4 = Card('Two','Heart')
        self.assertTrue(card4.value, 'Two')
        self.assertTrue(card4.suit,'Heart')