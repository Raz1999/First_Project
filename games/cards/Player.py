from First_Project.games.cards.DeckOfCards import DeckOfCards
import random
class Player():

    # מחלקה שמגדירה שחקן
    # לכל שחקן, יש חבילת קלפים. את הקלפים הוא מקבל מחבילת הקלפים של המשחק
    # המתודה מקבלת את כמות הקלפים שיוחלקו לכל שחקן ואת שמו

    def __init__(self, name, len_pack):
        if len_pack > 26:
            len_pack = 26
        self.name = name
        self.len_pack = len_pack
        self.pack = []

    # מתודה שמחלקת חבילת קלפים אישית לשחקן

    def set_hand(self,main_pack):
        self.pack.append(main_pack)

    # מתודה שמושכת קלף אקראי מהשחקן

    def get_card(self):
        rand_card = random.choice(self.pack)
        self.pack.remove(rand_card)
        return rand_card

    # מתודה שמוסיפה לחבילת הקלפים של השחקן קלף

    def add_card(self, card):
        self.pack.append(card)

    # מתודה שמציגה את פרטי השחקן, שמו וחבילת הקלפים שלו
    def show(self):
        print(f"player name: {self.name}\nplayer hand: {self.pack}")
