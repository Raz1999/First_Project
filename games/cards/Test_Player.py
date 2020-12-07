from First_Project.games.cards.Card import Card
from First_Project.games.cards.Player import Player
from First_Project.games.cards.DeckOfCards import DeckOfCards
from unittest import TestCase


class TestPlayer(TestCase):

    def setUp(self):
        self.card1 = Card('J',u'\u2663')
        self.card2 = Card('Q', u'\u2663')
        self.card3 = Card('K', u'\u2663')
        self.r_card = Card('A', u'\u2663')
        self.player1 = Player('name',3)
        self.player2 = Player('name',3)
        self.player3 = Player("name",0)
        self.player4 = Player("name", 26)
        self.player1.pack = [self.card1, self.card2, self.card3]

    def tearDown(self):
        print('Test is completed')

    def test_init(self):
        player5 = Player("name", -4)
        player6 = Player("name", 27)
        self.assertEqual(self.player2.len_pack, 3)
        self.assertEqual(self.player3.len_pack, 0)
        self.assertEqual(self.player4.len_pack, 26)
        self.assertEqual(player5.len_pack, 26)
        self.assertEqual(player6.len_pack, 26)
        with self.assertRaises(TypeError):
            player7 = Player("name", "abc")


    def test_set_hand(self):
        deck1 = DeckOfCards()
        self.player2.set_hand(deck1)
        deck2 = DeckOfCards()
        self.player3.set_hand(deck2)
        deck3 = DeckOfCards()
        self.player4.set_hand(deck3)
        self.assertEqual(len(self.player2.pack),3)
        self.assertEqual(len(self.player3.pack),0)
        self.assertEqual(len(self.player4.pack),26)
        deck4 = DeckOfCards()
        deck4.deck = []
        player_1 = Player('name', 10)
        player_1.set_hand(deck4)
        self.assertEqual(len(player_1.pack), 0)




    def test_get_card(self):
        copy_pack = self.player1.pack.copy()
        rand_card = self.player1.get_card()
        self.assertIn(rand_card, copy_pack)
        self.assertIsInstance(rand_card, Card)
        self.assertNotIn(rand_card, self.player1.pack)
        self.assertEqual(len(self.player1.pack) + 1,len(copy_pack))


    def test_add_card(self):
        self.player1.add_card(self.r_card)
        self.assertIn(self.r_card,self.player1.pack)
        self.assertEqual(self.player1.len_pack + 1, len(self.player1.pack))
        with self.assertRaises(TypeError):
            self.player1.add_card(4)
        with self.assertRaises(TypeError):
            self.player1.add_card('Four')
        deck1 = DeckOfCards()
        with self.assertRaises(TypeError):
            self.player1.add_card(deck1)

