from behave import given, when, then
from src.Game import Game

@given('player8 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')
    
@given('game over')
def step_impl(context):
    pass
    
@given('the number of card that deck left is more than 6 ')
def step_impl(context):
    pass

@when('player8 choose to restart')
def step_impl(context):
    pass

@then('game8 restart')
def step_impl(context):
    context.game.restart_phase(True, 6)
    assert context.game.gaming == True
    assert context.game.deck.deck_left != 52
    
    
@given('player9 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@when('player9 choose to exit')
def step_impl(context):
    pass

@then('exit')
def step_impl(context):
    context.game.restart_phase(False)
    assert context.game.gaming == False
    
    
@given('player10 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@when('player10 choose to restart')
def step_impl(context):
    pass

@then('reshuffle the deck')
def step_impl(context):
    pass

@then('game10 restart')
def step_impl(context):
    context.game.restart_phase(True, 5)
    assert context.game.gaming == True
    assert context.game.deck.deck_left == 52
