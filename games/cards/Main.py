from First_Project.games.cards.Card import Card
from First_Project.games.cards.DeckOfCards import DeckOfCards
from First_Project.games.cards.Player import Player
from First_Project.games.cards.CardGame import CardGame

P1 = input("Enter player 1 name: ")
P2 = input("Enter player 2 name: ")
Card_num = int(input("Enter number of card to dill\n(between 1-26): "))
Rounds=int(input("Enter number of game rounds: "))
First_game = CardGame(P1,P2,Card_num)

First_game.player1.show()
First_game.player2.show()

for i in range(1,Rounds+1):
    if len(First_game.player1.pack) == 0 or len(First_game.player2.pack) == 0:
        break
    p1_card = First_game.player1.get_card()
    p2_card = First_game.player2.get_card()
    print(p1_card, p2_card)

    if p1_card > p2_card:
        First_game.player2.add_card(p1_card)
        First_game.player2.add_card(p2_card)
        print(f'The winner in round: {i}, is {First_game.player1.name}')
    else:
        First_game.player1.add_card(p1_card)
        First_game.player1.add_card(p2_card)
        print(f'The winner in round: {i}, is {First_game.player2.name}')


print('-----------------------------')
First_game.player2.show()
First_game.player1.show()
print('-----------------------------')
First_game.get_winner()




