from First_Project.games.cards.DeckOfCards import DeckOfCards
from First_Project.games.cards.Card import Card
import random
class Player():

    # מחלקה שמגדירה שחקן
    # לכל שחקן, יש חבילת קלפים. את הקלפים הוא מקבל מחבילת הקלפים של המשחק
    # המתודה מקבלת את כמות הקלפים שיוחלקו לכל שחקן ואת שמו
    # במידה והאובייקט שחקן יקבל אורך חבילה שהוא לא INT, תעלה שגיאה מסוג TYPE

    def __init__(self, name, len_pack):
        if type(len_pack) is int:
            if len_pack > 26 or len_pack < 0:
                len_pack = 26
        else:
            raise TypeError("Invalid type, int type is needed")
        self.name = name
        self.len_pack = len_pack
        self.pack = []

    # מתודה שמחלקת חבילת קלפים אישית לשחקן לפי אורך החבילה שהגדרנו לשחקנים
    # במידה ובחבילת הקלפים אין קלפים בכלל, המתודה לא תבצע כלום
    # המתודה מקבלת את חבילת הקלפים ממנה מחלקים קלפים לשחקנים, במידה וזה לא אובייקט של חבילת קלפים
    # תעלה שגיאה מסוג TYPE

    def set_hand(self, game_deck):
         if type(game_deck) == DeckOfCards:
             if len(game_deck.deck) == 0:
                 pass
             else:
                for i in range(self.len_pack):
                    r_card = game_deck.deal_one()
                    self.pack.append(r_card)
         else:
            raise TypeError ("Invalid type, DeckOfCards type is needed ")


    # מתודה שמושכת קלף אקראי מהשחקן
    # ומוחקת אותו מהחבילה שלו

    def get_card(self):
        rand_card = random.choice(self.pack)
        self.pack.remove(rand_card)
        return rand_card

    # מתודה שמוסיפה לחבילת הקלפים של השחקן קלף
    # במידה והמתודה לא מקבלת אובייקט קלף, תעלה שגיאה מסוג TYPE

    def add_card(self, card):
        if type(card) == Card:
            self.pack.append(card)
        else:
            raise TypeError('Invalid type, Card type is needed')

    # מתודה שמציגה את פרטי השחקן, שמו וחבילת הקלפים שלו

    def show(self):
        print(f"player name: {self.name}\nplayer hand: {self.pack}")
