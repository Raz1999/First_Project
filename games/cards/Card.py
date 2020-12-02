from random import *
class Card():
    # האובייקט קארד, מגדיר שלאובייקט מסוג CARD יש ערכים מ2 עד A
    # בנוסף, לאובייקט יש גם צורה. לכל צורה יש ערך, כאן הערך מגולם על ידי האינדקס. צורה שעם ערך גדול יותר, נמצאת באינדקס גדול יותר

    def __init__(self,value,suit):
        self.values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.suits=[u'\u2666',u'\u2660',u'\u2665',u'\u2663']
        self.value=value
        self.suit=suit

    # מציג את הערך וצורת הקלף בהדפסה
    def __repr__(self):
        return (f"{self.value}{self.suit}")

