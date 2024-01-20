from behave import given, when, then
from src.Deck import Deck

@given('a new shuffled deck')
def step_impl(context):
    context.deck1 = Deck()

@when('create another new shuffled deck')
def step_impl(context):
    context.deck2 = Deck()

@then('first deck is different from second deck')
def step_impl(context):
    x = False
    for i in range(52):
        if context.deck1.deck[i] != context.deck2.deck[i]:
            x = True
            break
    assert x == True
            
    
@then('every card in second deck is not repeat')
def step_impl(context):
    assert len(set(context.deck2.deck)) == 52
