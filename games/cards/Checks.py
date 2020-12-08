# This is not interesting Orly!.
# from games.cards.Card import Card
# from games.cards.DeckOfCards import DeckOfCards
# from games.cards.Player import Player
#
# deck1=DeckOfCards()
# deck1.show()
#
# index_val_p1 = p1_card.values.index(p1_card.value)
# index_suit_p1 = p1_card.suits.index(p1_card.suit)
# index_val_p2 = p2_card.values.index(p2_card.value)
# index_suit_p2 = p2_card.suits.index(p2_card.suit)
#
# if index_val_p1 > index_val_p2:
#     First_game.player2.add_card(p1_card)
#     First_game.player2.add_card(p2_card)
#     print(P1, 'Won in Round:', i + 1)
#     continue
# elif index_val_p1 < index_val_p2:
#     First_game.player1.add_card(p1_card)
#     First_game.player1.add_card(p2_card)
#     print(P2, 'Won in Round:', i + 1)
#     continue
# elif index_val_p1 == index_val_p2:
#     if index_suit_p1 > index_suit_p2:
#         First_game.player2.add_card(p1_card)
#         First_game.player2.add_card(p2_card)
#         print(P1, 'Won in Round:', i + 1)
#         continue
#     elif index_suit_p1 < index_suit_p2:
#         First_game.player1.add_card(p1_card)
#         First_game.player1.add_card(p2_card)
#         print(P2, 'Won in Round:', i + 1)
#         continue
if type(54) == int:
    print('Gever')
else:
    print('Oz')

player2 = Player('Name', 4)
test_deck2 = DeckOfCards()
player2.set_hand(test_deck2)
self.assertEqual(len(player2.pack), player2.len_pack)
for i in player2.pack:
    self.assertIsInstance(i, Card)
for j in player2.pack:
    self.assertNotIn(j, test_deck2.deck)

player3 = Player('Name', 26)
test_deck3 = DeckOfCards()
player3.set_hand(test_deck3)
self.assertEqual(len(player3.pack), player3.len_pack)
for i in player3.pack:
    self.assertIsInstance(i, Card)
for j in player3.pack:
    self.assertNotIn(j, test_deck3.deck)

player4 = Player('Name', 0)
test_deck4 = DeckOfCards()
player4.set_hand(test_deck4)
self.assertEqual(len(player4.pack), player4.len_pack)
for i in player4.pack:
    self.assertIsInstance(i, Card)
for j in player4.pack:
    self.assertNotIn(j, test_deck4.deck)

player5 = Player('Name', 27)
test_deck5 = DeckOfCards()
player5.set_hand(test_deck5)
self.assertEqual(len(player5.pack), player5.len_pack)
for i in player5.pack:
    self.assertIsInstance(i, Card)
for j in player5.pack:
    self.assertNotIn(j, test_deck5.deck)

player6 = Player('Name', -5)
test_deck6 = DeckOfCards()
player6.set_hand(test_deck6)
self.assertEqual(len(player6.pack), player6.len_pack)
for i in player6.pack:
    self.assertIsInstance(i, Card)
for j in player6.pack:
    self.assertNotIn(j, test_deck6.deck)

player7 = Player('Name', 'Two')
test_deck7 = DeckOfCards()
player7.set_hand(test_deck7)
self.assertEqual(len(player7.pack), player7.len_pack)
for i in player7.pack:
    self.assertIsInstance(i, Card)
for j in player7.pack:
    self.assertNotIn(j, test_deck7.deck)



# len(self.player1.pack)==len(self.player2.pack)