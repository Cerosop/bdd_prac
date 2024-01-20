from behave import given, when, then
from src.Game import Game

@given('player4 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player4 has 1 dark card is Q spade')
def step_impl(context):
    context.game.player_cards.append("Q spade")

@given('owner4 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player4 has 1 open card is J diamond')
def step_impl(context):
    context.game.player_cards.append("J diamond")

@given('owner4 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")

@given('next4 card is {next_card}')
def step_impl(context, next_card):
    context.game.deck.deck[0] = next_card

@when('open4 dark card')
def step_impl(context):
    context.game.owner_add_card_phase()

@then('player4 card point is 20')
def step_impl(context):
    assert context.game.player_point == 20

@then('owner4 card point is {owner_point: d}')
def step_impl(context, owner_point):
    assert context.game.owner_point == owner_point

@then('game result is {game_result}')
def step_impl(context, game_result):
    assert context.game.game_result == game_result


@given('player5 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player5 has 1 dark card is Q spade')
def step_impl(context):
    context.game.player_cards.append("Q spade")

@given('owner5 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player5 has 2 open card is 2 diamond and 2 heart')
def step_impl(context):
    context.game.player_cards.append("2 diamond")
    context.game.player_cards.append("2 heart")

@given('owner5 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")

@when('open5 dark card')
def step_impl(context):
    context.game.owner_add_card_phase()

@then('player5 card point is 14')
def step_impl(context):
    assert context.game.player_point == 14

@then('owner5 card point is 17')
def step_impl(context):
    assert context.game.owner_point == 17

@then('player5 loses')
def step_impl(context):
    assert context.game.game_result == "player loses"


@given('player6 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player6 has 1 dark card is A spade')
def step_impl(context):
    context.game.player_cards.append("A spade")

@given('owner6 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player6 has 1 open card is Q diamond')
def step_impl(context):
    context.game.player_cards.append("J diamond")

@given('owner6 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")

@when('go into owner6 draw phase')
def step_impl(context):
    context.game.owner_add_card_phase()

@then('player6 wins')
def step_impl(context):
    assert context.game.game_result == "player wins"


@given('player7 name is Amy')
def step_impl(context):
    context.game = Game()
    context.game.set_player_name('Amy')

@given('player7 has 1 dark card is Q spade')
def step_impl(context):
    context.game.player_cards.append("Q spade")

@given('owner7 has 1 dark card is 7 heart')
def step_impl(context):
    context.game.owner_cards.append("7 heart")

@given('player7 has 2 open card is Q diamond and 2 diamond')
def step_impl(context):
    context.game.player_cards.append("Q diamond")
    context.game.player_cards.append("2 diamond")

@given('owner7 has 1 open card is K club')
def step_impl(context):
    context.game.owner_cards.append("K club")

@when('go into owner7 draw phase')
def step_impl(context):
    context.game.owner_add_card_phase()

@then('player7 loses')
def step_impl(context):
    assert context.game.game_result == "player loses"