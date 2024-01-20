Feature: draw a card
	
	Scenario: draw 2 card
		Given a deck with top of 4 card is [A spade, 2 spade, 3 spade, 4 spade]
        And already draw one card
		When draw a card twice
		Then first card is 2 spade
        But second card is 3 spade