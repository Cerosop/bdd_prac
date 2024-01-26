Feature: owner add card
	
	Scenario Outline: owner4 have to add card
		Given player4 name is Amy
        And player4 has 1 dark card is Q spade
		And owner4 has 1 dark card is 7 heart
		And player4 has 1 open card is J diamond
		And owner4 has 1 open card is K club
        And next4 card is <next_card>
		When open4 dark card
		Then player4 card point is 20
        But owner4 card point is <owner_point>
        But game result is <game_result>

        Examples:
            | next_card | owner_point | game_result |
            | 4 spade          | 21             |     player loses      |
            | 3 heart        | 20             |     draw     |
            | 5 heart        | 22             |     player wins     |


    Scenario: owner5 win without draw
		Given player5 name is Amy
        And player5 has 1 dark card is Q spade
		And owner5 has 1 dark card is 8 heart
		And player5 has 2 open card is 2 diamond and 2 heart
		And owner5 has 1 open card is K club
		When open5 dark card
        Then player5 card point is 14
		But owner5 card point is 18
        But player5 loses


    Scenario: player6 has 21 point
		Given player6 name is Amy
        And player6 has 1 dark card is A spade
		And owner6 has 1 dark card is 7 heart
		And player6 has 1 open card is Q diamond
		And owner6 has 1 open card is K club
		When go into owner6 draw phase
        Then player6 wins


    Scenario: player7 has over 21 point
		Given player7 name is Amy
        And player7 has 1 dark card is Q spade
		And owner7 has 1 dark card is 7 heart
		And player7 has 2 open card is Q diamond and 2 diamond
		And owner7 has 1 open card is K club
		When go into owner7 draw phase
        Then player7 loses
