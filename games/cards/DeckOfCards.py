import random
from games.cards.Card import Card
class DeckOfCards():

    # המחלקה מגדירה חפיסת קלפים. כל קלף הוא אובייקט מסוג Card.
    # כאשר נגדיר חפיסת קלפים חדשה, יוגרלו 52 קלפים. כל שילוב אפשרי בין הערכים לצורות.

    def __init__(self):
        self.deck = []
        self.values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.suits=[u'\u2666',u'\u2660',u'\u2665',u'\u2663']
        for i in self.values:
            for j in self.suits:
                card = Card(i,j)
                self.deck.append(card)

    # מתודה שמערבבת את האובייקטיים מסוג Card, בתוך חפיסת הקלפים.

    def shuffle_deck(self,):
        random.shuffle(self.deck)
        return print("The deck is shuffled")

    # מתודה שמוציאה קלף מהחבילה באופן אקראי

    def deal_one(self):
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        return random_card

    # מתודה שמציגה את חפיסת הקלפים

    def show(self):
       return print(f"{self.deck}")
