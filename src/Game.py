from src.Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.gaming = False
        self.player_cards = [] # dark第一張 open:2, 3
        self.player_point = 0
        self.owner_cards = [] # dark第一張 open:2, 3
        self.owner_point = 0
        self.game_result = "" # "player loses" or "player wins" or "draw"
        pass

    def set_player_name(self, name):
        pass
    
    def new_game(self):
        self.player_cards = []
        self.owner_cards = []
        
    def distribute_card(self):
        pass
    
    def ask_player_to_add_card(self, ask = None): # 根據input判斷是否要抽 return bool
        if not ask:
            ask = input()
        pass
    
    def player_add_card_phase(self, choose_to_add_or_not: bool): # 就只需要抽或不抽
        pass
    
    def owner_add_card_phase(self): # 玩家開牌 判斷玩家爆牌沒 莊家開牌 莊家抽不抽 結果判斷
        pass
    
    def restart_phase(self, restart_or_not, deck_left = 6): # 判斷重啟 判斷重洗牌(排少於6張) 更改self.gaming
        pass

    def start_game(self):
        self.gaming = True
        while self.gaming:
            self.new_game()
            self.distribute_card()
            self.player_add_card_phase(self.ask_player_to_add_card())
            self.owner_add_card_phase()
            self.restart_phase()
        
    

    