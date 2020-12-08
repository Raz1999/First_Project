from First_Project.games.cards.Card import Card
from unittest import TestCase


class TestCard(TestCase):

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