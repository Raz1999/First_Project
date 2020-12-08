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

    # בדיקה לINIT של המחלקה המגדירה שחקן
    # בבדיקה זו אנו בודקים עבור ערכים שונים, שאורך החבילה של השחקן יהיה המספר שהגדרנו לו
    # ובמידה והמספר שלילי או מעל 26, החבילה תיהיה באורך 26
    # במידה והשחקן מקבל אורך חבילה שהוא לא מסוג INT תעלה שגיאה מסוך TYPE

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
            player8 = Player('name', 4.5)

    # בדיקה למתודה המחלקת לשחקן חבילת קלפים מחבילת המשחק
    # ביצענו בדיקה עבור נתוני קצה, ועבור ערך בין טווח זה
    # אין צורך להציב ערכים מסוגים נוספים שכן לא נקבל כאלה בעקבות השגיאה שתעלה בקונסרקטור
    # בנוסף, בדקנו שכאשר חבילת הקלפים ריקה, ממנה מחלקים קלפים, חבילת השחקן לא משתנה והוא לא מקבל קלפים

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

    # בדיקה למתודה שלוקחת מהשחקן קלף אקראי
    # בדקנו שהקלף הנבחר אכן מהחבילה של השחקן, ושהוא אובייקט מסוג קלף
    # בדקנו שקלף אכן ירד מחבילת הקלפים של השחקן, ושאורך החבילה ירד באחד

    def test_get_card(self):
        copy_pack = self.player1.pack.copy()
        rand_card = self.player1.get_card()
        self.assertIn(rand_card, copy_pack)
        self.assertIsInstance(rand_card, Card)
        self.assertNotIn(rand_card, self.player1.pack)
        self.assertEqual(len(self.player1.pack) + 1,len(copy_pack))

    # בדיקה למתודה שמוסיפה לשחקן קלף
    # המתודה מקבלת אובייקט מסוג קלף
    # בדקנו שכאשר המתודה מקבל אובייקט קלף, היא אכן מוסיפה את הקלף לחבילת השחקן, ושאורך החבילה גדל באחד
    # בנוסף בדקנו שכאשר המתודה הזו מקבלת משתנה מסוג אחר, עולה שגיאה מסוג TYPE
    # בדקנו גם שכאשר אנו מוסיפים לשחקן חפיסה שלמה, זה מעלה שגיאה

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

# אפשר להוסיף חפיסה, לבדוק את זה ולהוסיף