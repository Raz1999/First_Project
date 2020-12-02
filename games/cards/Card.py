from random import *
class Card():
    def __init__(self,value,suit):
        self.values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        self.suits=[u'\u2666',u'\u2660',u'\u2665',u'\u2663']
        self.value=value
        self.suit=suit

    def __repr__(self):
        return (f"{self.value}{self.suit}")
