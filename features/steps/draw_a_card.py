from behave import given, when, then
from src.Deck import Deck

@given('a deck with top of 4 card is [A spade, 2 spade, 3 spade, 4 spade]')
def step_impl(context):
    context.deck = Deck()
    context.deck.deck[0] = 'A spade'
    context.deck.deck[1] = '2 spade'
    context.deck.deck[2] = '3 spade'
    context.deck.deck[3] = '4 spade'

@given('already draw one card')
def step_impl(context):
    context.deck.draw()

@when('draw a card twice')
def step_impl(context):
    context.card1 = context.deck.draw()
    context.card2 = context.deck.draw()

@then('first card is 2 spade')
def step_impl(context):
    assert context.card1 == '2 spade'
    
@then('second card is 3 spade')
def step_impl(context):
    assert context.card2 == '3 spade'