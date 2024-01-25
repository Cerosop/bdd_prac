from src.Deck import Deck
from src.Game import Game

def main():
    game = Game()
    print ("Welcome to BlackJack!")
    print ("Please enter your name:")
    name = input()
    game.set_player_name(name)
    game.start_game()

if __name__ == "__main__":
    main()

