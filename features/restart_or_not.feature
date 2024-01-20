Feature: restart or not
	
	Scenario: restart
		Given player8 name is Amy
        And game over 
        And the number of card that deck left is more than 6 
		When player6 choose to restart
		Then game6 restart


    Scenario: exit
		Given player7 name is Amy
        And game over 
		When player7 choose to exit
		Then exit

    
    Scenario: restart but the number of card that deck left is less than 6
		Given player8 name is Amy
        And game over 
        And the number of card that deck left is less than 6 
		When player8 choose to restart
		Then reshuffle the deck
        But game8 restart
