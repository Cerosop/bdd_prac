from behave import given, when, then
from src.Game import Game

@given('player2 name is Amy2')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player2 has 1 dark card is Q spade')
def step_impl(context):
    context.game.player_cards.append("Q spade")

@given('owner2 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player2 has 1 open card is J diamond')
def step_impl(context):
    context.game.player_cards.append("J diamond")

@given('owner2 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")
    
@given('next2 card is {next_card}')
def step_impl(context, next_card):
    context.game.deck.deck[0] = next_card

@when('player2 choose to add card')
def step_impl(context):
    context.game.player_add_card_phase()

@then('player2 card point is {player_point: d}')
def step_impl(context, player_point):
    assert context.game.player_point == player_point


@given('player3 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player3 has 1 dark card is Q spade')
def step_impl(context):
    context.game.player_cards.append("Q spade")
    
@given('owner3 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player3 has 1 open card is J diamond')
def step_impl(context):
    context.game.player_cards.append("J diamond")

@given('owner3 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")

@when('player3 choose not to add card')
def step_impl(context):
    context.game.player_add_card_phase(False)

@then('player3 card point is 20')
def step_impl(context):
    assert context.game.player_point == 20


@when('player reply {reply}')
def step_impl(context, reply):
    context.reply = context.game.ask_player_to_add_card(ask = reply)

@then('reply should be {reply_bool}')
def step_impl(context, reply_bool):
    assert str(context.reply) == reply_bool
