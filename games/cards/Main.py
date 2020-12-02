from games.cards.Card import Card
from games.cards.DeckOfCards import DeckOfCards
from games.cards.Player import Player
from games.cards.CardGame import CardGame

P1='Raz'
P2='Shalev'
First_game=CardGame(P1,P2,20)

First_game.player1.show()
First_game.player2.show()

for i in range(20):
    p1_card = First_game.player1.get_card()
    p2_card = First_game.player2.get_card()
    print(p1_card, p2_card)
    index_val_p1 = p1_card.values.index(p1_card.value)
    index_suit_p1 = p1_card.suits.index(p1_card.suit)
    index_val_p2 = p2_card.values.index(p2_card.value)
    index_suit_p2 = p2_card.suits.index(p2_card.suit)

    if index_val_p1>index_val_p2:
        First_game.player2.add_card(p1_card)
        First_game.player2.add_card(p2_card)
        print(P1,'Won in Round:',i+1)
        continue
    elif index_val_p1<index_val_p2:
        First_game.player1.add_card(p1_card)
        First_game.player1.add_card(p2_card)
        print(P2,'Won in Round:',i+1)
        continue
    elif index_val_p1==index_val_p2:
        if index_suit_p1 > index_suit_p2:
            First_game.player2.add_card(p1_card)
            First_game.player2.add_card(p2_card)
            print(P1,'Won in Round:',i+1)
            continue
        elif index_suit_p1 < index_suit_p2:
            First_game.player2.add_card(p1_card)
            First_game.player2.add_card(p2_card)
            print(P2,'Won in Round:',i+1)
            continue
print('-----------------------------')
First_game.player2.show()
First_game.player1.show()
print('-----------------------------')
First_game.get_winner()







