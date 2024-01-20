from behave import given, when, then
from src.Game import Game

@given('a game')
def step_impl(context):
    context.game = Game()

@when('player name is Amy')
def step_impl(context):
    context.game.set_player_name('Amy')

@then('game start')
def step_impl(context):
    context.game.new_game()
    assert context.game.player_cards == []
    assert context.game.owner_cards == []
    