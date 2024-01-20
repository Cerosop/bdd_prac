from behave import given, when, then
from src.Game import Game
from src.Deck import Deck

@given('player name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('next 4 card is [A spade, 7 heart, J diamond, K club]')
def step_impl(context):
    deck = Deck()
    deck.deck[0] = 'A spade'
    deck.deck[1] = '7 heart'
    deck.deck[2] = 'J diamond'
    deck.deck[3] = 'K club'
    context.game.deck = deck

@when('distribute_card')
def step_impl(context):
    context.game.distribute_card()

@then('player has 1 dark card is A spade, 1 open card is J diamond')
def step_impl(context):
    assert context.game.player_cards == ['A spade', 'J diamond']

@then('owner has 1 dark card is 7 heart, owner has 1 open card is K club')
def step_impl(context):
    assert context.game.owner_cards == ['7 heart', 'K club']