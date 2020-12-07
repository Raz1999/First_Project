from First_Project.games.cards.CardGame import CardGame
from unittest import TestCase


class TestCardGame(TestCase):

    def setUp(self):
        self.test_game = CardGame("name1", "name2", 10)
        name1 = len(self.test_game.player1.pack)
        name2 = len(self.test_game.player2.pack)


    def tearDown(self):
        print('The test complete')


    def test_init(self):
        with self.assertRaises(TypeError):
            game1 = CardGame("name1", "name2", "check")
            game2 = CardGame("name1", "name2", 4.7)
        game3 = CardGame("name1", "name2")
        self.assertEqual(game3.num_cards, 10)
        game4 = CardGame("name1", "name2", 12)
        self.assertEqual(game4.num_cards, 12)


    def test_new_game(self):
        game_1 = CardGame("name1", "name2",10)
        with self.assertRaises(SystemError):
            game_1.new_game()


    def test_get_winner(self):
        game1 = CardGame("shalev", "raz", 10)
        game1.player1.pack.pop()
        self.assertIn(game1.player1.name, game1.get_winner())
        game2 = CardGame("shalev", "raz", 10)
        game2.player2.pack.pop()
        self.assertIn(game1.player2.name, game2.get_winner())
        self.assertIn(None,self.test_game.get_winner())




