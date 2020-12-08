from random import *
class Card:

    # האובייקט קארד, מגדיר שלאובייקט מסוג CARD יש ערכים מ2 עד A, הערכים מסודרים ברשימה לפי האינדקס
    # בנוסף, לאובייקט יש גם צורה. לכל צורה יש ערך, כאן הערך מגולם על ידי האינדקס. צורה שעם ערך גדול יותר, נמצאת באינדקס גדול יותר

    def __init__(self,value,suit):
        self.values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.suits=[u'\u2666',u'\u2660',u'\u2665',u'\u2663']
        if value in self.values and suit in self.suits:
            self.suit = suit
            self.value = value
        else:
            raise TypeError('Invalid value and suit, this is Card game!')


    # מציג את הערך וצורת הקלף בהדפסה
    def __repr__(self):
        return (f"{self.value}{self.suit}")


    # מתודה שמשווה בין שתי אובייקטים מסוג קלף, ומחזירה את הקלף הגדול יותר
    # המתודה בודקת קודם כל את ערך הקלף, כמו במשחק רגיל
    # במידה והערך שווה, המתודה משווה את הצורה של הקלף, והצורה שנמצאת באינדקס גדול יותר, מנצחת.


    def __gt__(self, other):
        index_val_p1 = self.values.index(self.value)
        index_suit_p1 = self.suits.index(self.suit)
        index_val_p2 = other.values.index(other.value)
        index_suit_p2 = other.suits.index(other.suit)
        if index_val_p1 > index_val_p2:
            return True
        elif index_val_p1 < index_val_p2:
            return False
        elif index_val_p1 == index_val_p2:
            if index_suit_p1 > index_suit_p2:
                return True
            else:
                return False