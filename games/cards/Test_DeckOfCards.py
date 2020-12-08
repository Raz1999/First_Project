from First_Project.games.cards.Card import Card
from First_Project.games.cards.DeckOfCards import DeckOfCards
from unittest import TestCase


class TestDeckOfCards(TestCase):

    def setUp(self):
       self.deck1 = DeckOfCards()
       self.copy_deck = self.deck1.deck.copy()
       print('The test is starting')


    def tearDown(self):
        print("The test completed")


    # בדיקה לINIT של האובייקט מסוג חבילת קלפים
    # בדקנו שאכן, המתודה מכניסה 52 קלפים לחבילה, שונים אחד מהשני, מסוג CARD


    def test_init(self):
        list1 = []
        for i in self.deck1.deck:
            if type(i) == Card:
                if i not in list1:
                    list1.append(i)
        self.assertEqual(len(list1), 52)


    # בדיקה למתודה שמערבבת את הקלפים בחבילה
    # בדקנו שאכן החבילה עורבבה, והקלפים בה שינו את מיקומם ושאף קלף לא נעלם


    def test_shuffle_deck(self):
        self.assertNotEqual(self.deck1.shuffle_deck(),self.copy_deck)
        self.assertCountEqual(self.deck1.deck,self.copy_deck)


    # בדיקה למתודה שמחלקת קלף אחד
    # בדקנו שאכן המתודה מוציאה את הקלף שהיא בחרה מחבילת הקלפים, ושאורכה קטן באחד
    # בדקנו שבמידה ויש קלף אחרון בחבילת הקלפים, המתודה עדיין יודעת לחלק אותו ולא לפגוע ברשימה
    # לכן נשארת רשימה ריקה מקלפים, אך היא עדיין רשימה באורך 0


    def test_deal_one(self):
        self.assertNotIn(self.deck1.deal_one(),self.deck1.deck)
        self.assertEqual(len(self.deck1.deck)+1,len(self.copy_deck))
        deck2 = DeckOfCards()
        deck2.deck = [Card(2, u'\u2666')]
        deck2.deal_one()
        self.assertEqual(len(deck2.deck),0)
        self.assertIsInstance(deck2.deck,list)
        self.assertIs(deck2.deal_one(),None)

