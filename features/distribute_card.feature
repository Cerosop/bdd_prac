Feature: distribute card
	
	Scenario: distribute_card
		Given player name is Amy
        And next 4 card is [A spade, 7 heart, J diamond, K club]
		When distribute_card
		Then player has 1 dark card is A spade, player has 1 open card is J diamond
		But owner has 1 dark card is 7 heart, owner has 1 open card is K club

