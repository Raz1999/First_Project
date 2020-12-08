from First_Project.games.cards.Player import Player
from First_Project.games.cards.DeckOfCards import DeckOfCards

class CardGame():

    # מחלקה שמגדירה את משחק הקלפים וחוקיו.
    # מתודה שמקבלת את שמות שתי השחקנים ומספר הקלפים שיש לחלק לכל שחקן
    # המתודה יוצרת חבילת קלפים אקראית חדשה
    # במידה והמחלקה מקבלת מספר קלפים, שהוא לא מספר, עולה שגיאה מסוג TYPE

    def __init__(self, name1, name2, num_cards = 10):
        if type(num_cards) != int:
            raise TypeError('Invalid Type, int type is needed')
        else:
            self.num_cards = num_cards
            self.player1 = Player(name1, num_cards)
            self.player2 = Player(name2, num_cards)
            self.game_deck = DeckOfCards()
            self.new_game()

    # מתודה שמערבבת את חבילת הקלפים ומחלקת קלפים לשתי השחקנים
    # המתודה פועלת רק כאשר המשחק עוד לא התחיל, נקראית מהקונסטרקטור
    # במידה והמתודה תופעל באמצע המשחק, תחזיר שגיאה מסוג System


    def new_game(self):
        if len(self.game_deck.deck)==52:
            self.game_deck.shuffle_deck()
            self.player1.set_hand(self.game_deck)
            self.player2.set_hand(self.game_deck)

        else:
            raise SystemError("the game is already began")

    # מתודה שמכריעה מי הזוכה במשחק, מחזירה אותו ומדפיסה הודעה בהתאם

    def get_winner(self):
        if len(self.player1.pack)<len(self.player2.pack):
            return self.player1.name, print(f'The winner is: {self.player1.name}')
        elif len(self.player1.pack)>len(self.player2.pack):
            return self.player2.name,print(f'The winner is: {self.player2.name}')
        else:
            return None,print("There is no winner - tied")