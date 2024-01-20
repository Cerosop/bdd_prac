Feature: player add card
	
	Scenario Outline: player2 choose to add specific card
		Given player2 name is Amy2
        And player2 has 1 dark card is Q spade
		And owner2 has 1 dark card is 7 heart
		And player2 has 1 open card is J diamond
		And owner2 has 1 open card is K club
		And next2 card is <next_card>
		When player2 choose to add card 
		Then print2 player card point is <player_point>

        Examples:
            | next_card | player_point |
            | A spade          | 21             |
            | 2 heart        | 22             |


    Scenario: player3 choose not to add card
		Given player3 name is Amy
        And player3 has 1 dark card is Q spade
		And owner3 has 1 dark card is 7 heart
		And player3 has 1 open card is J diamond
		And owner3 has 1 open card is K club
		When player3 choose not to add card
		Then player3 card point is 20

	
	Scenario Outline: ask player
		When player reply <reply>
		Then reply should be <reply_bool>

		Examples:
            | reply | reply_bool |
            | Yes          | True             |
            | yes          | True             |
            | No          | False            |
            | no          | False             |
