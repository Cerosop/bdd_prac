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
        self.player_name = ""

    def set_player_name(self, name):
        self.player_name = name
    
    def new_game(self):
        self.player_cards = []
        self.owner_cards = []
        self.player_point = 0
        self.owner_point = 0
        
    def distribute_card(self):
        self.player_cards.append(self.deck.draw())
        self.owner_cards.append(self.deck.draw())
        self.player_cards.append(self.deck.draw())
        self.owner_cards.append(self.deck.draw())
        print(self.player_name + " get a dark card is " + self.player_cards[0])
        print("ownerget a dark card ")
        print(self.player_name + " get a open card is " + self.player_cards[1])
        print("owner get a open card is " + self.owner_cards[1])
        
    def ask_player_to_add_card(self, ask = None): # 根據input判斷是否要抽 return bool
        print("Do you want to add card?")
        ask = input()
        if ask == 'y' or ask == 'Yes' or ask == 'yes':
            return True
        elif ask == 'n' or ask == 'No' or ask == 'no':
            return False
    
    def player_add_card_phase(self, choose_to_add_or_not: bool): # 就只需要抽或不抽
        A_amount = 0
        for i in range(0, len(self.player_cards)):
            if self.player_cards[i][0] == 'A':
                A_amount += 1

        for i in range(0, len(self.player_cards)):
            if self.player_cards[i][0] == 'J' or self.player_cards[i][0] == 'Q' or self.player_cards[i][0] == 'K':
                self.player_point += 10
            elif self.player_cards[i][0] == 'A':
                self.player_point += 11
            elif self.player_cards[i][0] == '1' and self.player_cards[i][1] == '0':
                self.player_point += 10
            else:
                self.player_point += int(self.player_cards[i][0])
        while(self.player_point > 21 and A_amount > 0):
            self.player_point -= 10
            A_amount -= 1
        if(choose_to_add_or_not):
            self.player_cards.append(self.deck.draw())
            print(self.player_name + " get a open card is " + self.player_cards[len(self.player_cards) - 1])
            self.player_point = 0
            A_amount = 0
            for i in range(0, len(self.player_cards)):
                if self.player_cards[i][0] == 'A':
                    A_amount += 1

            for i in range(0, len(self.player_cards)):
                if self.player_cards[i][0] == 'J' or self.player_cards[i][0] == 'Q' or self.player_cards[i][0] == 'K':
                    self.player_point += 10
                elif self.player_cards[i][0] == 'A':
                    self.player_point += 11
                elif self.player_cards[i][0] == '1' and self.player_cards[i][1] == '0':
                    self.player_point += 10
                else:
                    self.player_point += int(self.player_cards[i][0])
            while(self.player_point > 21 and A_amount > 0):
                self.player_point -= 10
                A_amount -= 1
            self.player_add_card_phase(self.ask_player_to_add_card())
    
    def owner_add_card_phase(self): # 玩家開牌 判斷玩家爆牌沒 莊家開牌 莊家抽不抽 結果判斷
        # 玩家開牌 判斷玩家爆牌沒
        self.player_point = 0
        A_amount = 0
        for i in range(0, len(self.player_cards)):
            if self.player_cards[i][0] == 'A':
                A_amount += 1

        for i in range(0, len(self.player_cards)):
            if self.player_cards[i][0] == 'J' or self.player_cards[i][0] == 'Q' or self.player_cards[i][0] == 'K':
                self.player_point += 10
            elif self.player_cards[i][0] == 'A':
                self.player_point += 11
            elif self.player_cards[i][0] == '1' and self.player_cards[i][1] == '0':
                self.player_point += 10
            else:
                self.player_point += int(self.player_cards[i][0])
        while(self.player_point > 21 and A_amount > 0):
            self.player_point -= 10
            A_amount -= 1
        
        if self.player_point > 21:
            self.game_result = "player loses"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return
        
        if self.player_point == 21:
            self.game_result = "player wins"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return

        # 莊家開牌 莊家抽不抽 結果判斷
        def calculate_owner_point():
            A_amount = 0
            for i in range(0, len(self.owner_cards)):
                if self.owner_cards[i][0] == 'A':
                    A_amount += 1

            for i in range(0, len(self.owner_cards)):
                if self.owner_cards[i][0] == 'J' or self.owner_cards[i][0] == 'Q' or self.owner_cards[i][0] == 'K':
                    self.owner_point += 10
                elif self.owner_cards[i][0] == 'A':
                    self.owner_point += 11
                elif self.owner_cards[i][0] == '1' and self.owner_cards[i][1] == '0':
                    self.owner_point += 10
                else:
                    self.owner_point += int(self.owner_cards[i][0])

            while(self.owner_point > 21 and A_amount > 0):
                self.owner_point -= 10
                A_amount -= 1

        calculate_owner_point()
        while(self.owner_point < 18):
            self.owner_cards.append(self.deck.draw())
            self.owner_point = 0
            calculate_owner_point()

        for i in range(2, len(self.owner_cards)):
            print("owner get a open card is " + self.owner_cards[i])
            

        if self.owner_point > 21:
            self.game_result = "player wins"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return
        
        if self.owner_point == 21:
            self.game_result = "player loses"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))            
            return
        
        # 結果判斷 因為玩家和莊家爆牌和剛好21點已經判斷過了 所以玩家和莊家點數一定小於21
        if self.owner_point > self.player_point:
            self.game_result = "player loses"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return
        
        if self.owner_point < self.player_point:
            self.game_result = "player wins"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return
        
        if self.owner_point == self.player_point:
            self.game_result ="draw"
            print("this round is over")
            print("owner's dark card is " + self.owner_cards[0])
            print(self.player_name + "'s card are " + str(self.player_cards))
            print("owner's card are " + str(self.owner_cards))
            return
    
    def restart_phase(self): # 判斷重啟 判斷重洗牌(排少於6張) 更改self.gaming
        deck_left = self.deck.deck_left
        if deck_left < 6:
            print("The rest of card is less then 6,do you want to restart? (y/n)")
            restart = input()
            if restart == 'y':
                newgame = Game()
                newgame.set_player_name(self.player_name)
                newgame.start_game()
            else:
                print("Game over")
                self.gaming = False
        else:
            self.deck_left = deck_left
            print("------------------next round-------------------")
            print("Do yo want to start next round? (y/n)")
            next_round = input()
            if next_round == 'n':
                print("Game stop")
                self.gaming = False


    def start_game(self):
        self.gaming = True
        while self.gaming:
            self.new_game()
            self.distribute_card()
            self.player_add_card_phase(self.ask_player_to_add_card())
            self.owner_add_card_phase()
            print(self.game_result)
            self.restart_phase()
        
    

    