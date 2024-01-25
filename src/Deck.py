import random
class Deck:
    def __init__(self):
        self.suits = ['spade', 'heart', 'diamond', 'club']
        self.numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10' ,'J', 'Q', 'K']
        card_id = list(range(0, 51))
        random.shuffle(card_id)
        self.deck = []#越前面越上面 每次隨機生成(都要不一樣) ex['7 heart', 'A diamond', ...]代表愛心7在最上面方塊A第二
        for i in range(0, 51):
            self.deck.append(self.numbers[card_id[i] % 13] + ' ' + self.suits[card_id[i] % 4])
        self.deck_left = 52
        

    def draw(self): # 抽最上面一張出去
        if self.deck_left == 0:
            return None
        self.deck_left -= 1
        return self.deck[51 - self.deck_left]
        
    
    def deck_left(self): # 排堆剩幾張
        return self.deck_left