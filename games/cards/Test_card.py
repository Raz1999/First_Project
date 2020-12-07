from First_Project.games.cards.Card import Card
from unittest import TestCase


class TestCard(TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            card1 = Card(20, u'\u2666')
        with self.assertRaises(TypeError):
            card2 = Card(5,30)
        with self.assertRaises(TypeError):
            card3 = Card('oz','hadar')