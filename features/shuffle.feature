Feature: shuffle
	
	Scenario: prepare a new shuffled deck
		Given a new shuffled deck
		When create another new shuffled deck
		Then first deck is different from second deck
        But every card in second deck is not repeat