from First_Project.games.cards.Card import Card
from unittest import TestCase


class TestCard(TestCase):

    def setUp(self):
        self.card1 = Card(10,u'\u2660')
        self.card2 = Card(9, u'\u2660')
        self.card3 = Card(9,u'\u2663')
        self.card4 = Card(9,u'\u2666')


    def tearDown(self):
        print('Test is complete')


    # בדיקה למתודה INIT של אובייקט מסוג קלף, מוודאים שבמידה והקלף מקבל ערך וצורה לא תקינים, מעלה שגיאה
    # בנוסף, בדקנו שעבור ערכים תקינים, לא עולה שגיאה במקרה


    def test_init(self):
        with self.assertRaises(TypeError):
            card1 = Card(20, u'\u2666')
        with self.assertRaises(TypeError):
            card2 = Card(5,30)
        with self.assertRaises(TypeError):
            card3 = Card('oz','hadar')
        card4 = (Card('A',u'\u2666'))


    # בדיקה למתודה __GT__, של אובייקט מסוג קלף
    # מוודא שהמתודה אכן משווה בין הקלפים, ומחזירה תוצאה מתאימה בהתאם לערכי הקלפים


    def test_gt(self):
        self.assertTrue(self.card1.__gt__(self.card2))
        self.assertFalse(self.card2.__gt__(self.card1))
        self.assertTrue(self.card3.__gt__(self.card2))
        self.assertFalse(self.card4.__gt__(self.card2))


