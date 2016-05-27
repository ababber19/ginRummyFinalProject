#John Gouwar, Aryman Babber, Ian Garinger
#game.py
#May 24 2016
#This is the main game of gin rummy 
from Player import *
from Deck import *
from Meld import *
global roundOn
global inTurns
global wantAnotherAction 
def getCardFromPlayer(player, card):
	'''
	This method takes an int that the user input and then returns the card object to be used by the program
	:param player: The Player performing the action(Player object)
	:param card: A int given as the position in the player's hand (using ordinal numbers, not indexing) 
	return: the specific card object from the player's hand
	'''
	return player._hand.index(card - 1)
def takeAction(player, action, deck, discard):
	'''
	This method takes the action a player wants to make a preforms it
	:param player: The player object performing the action 
	:param action: One of the actions defined in README.txt as a string 
	:params deck&discard: will always be the deck and discard pile, just need to be passed to the function
	return: None
	'''
	if action == "draw":
		location = input("Where do you want to draw from (Deck or Discard):" ).lower()
		if location == "deck":
			player.drawCard(deck)
		elif location == "discard":
			player.drawCard(discard)
		else:
			print("Sorry, invalid location!")
			return None
	elif action == "make set":
		setArray = []
		numCards = int(input("How many cards in this set?(3 or 4): "))
		if numCards > 2 and numCards < 5:
			for i in range(numCards):
				card = int(input("Card to add (use rules for naming): "))
				setArray.append(getCardFromPlayer(player, card)) #adds the card to the set tuple
		else:
			print("Sorry, invalid number of cards")
			return None
	elif action == "make run":
		runArray = []
		numCards = int(input("How many cards in this run"))
		if numCards > 0 and numCards <= 11:  #hand size parameters
			for i in range(numCards):
				card = int(input("Card to add (use rules for naming): "))
				runArray.append(getCardFromPlayer(player, card))
		else:
			print("Sorry, invalid number of cards")
			return None
	elif action == "knock":
		player.knock()
		roundOn = False 
		inTurns = False	
		wantAnotherAction = False
	else: #block that condescends them for giving a non-valid action
		print("Fine, be that way")
		return None
def main():
	global roundOn
	global inTurns
	global wantAnotherAction
	print("Welcome to the Gin Rummy Extravaganza! Press Enter to continue")
	input()
	player1Name = input("What is player 1's name?: ")
	player2Name = input("What is player 2's name?: ")
	Player1 = Player(player1Name); Player2 = Player(player2Name)
	gameOn = True
	winner = None #initializing the winner of the game, and stays none if it is a tie 
	while gameOn: #controling loop for the game
		roundOn = True
		player1Turn = True #will help flip flop turns
		while roundOn: #controling loop for round
			deck = Deck()
			deck.deckShuffle()
			discard = DiscardPile()
			for i in range(10):
				Player1.drawCard(deck)
				Player2.drawCard(deck)
			inTurns = True
			while inTurns: #controlling loop for turns 
				if player1Turn:
					input("%s, press enter to continue, don't let %s see your actions" % (Player1.getName(), Player2.getName()))
					print("\n" * 100) #clearing console because python is silly
					print("Your hand:\n %a" % Player1.getHand())
					try: 
						print("Top card of discard pile: " + discard._pile[len(discard._pile)-1])
					except IndexError: #pile is empty
						print("Discard pile is empty")
					wantAnotherAction = True 
					while wantAnotherAction: #controling loop for turn actions
						action = input("What action would you like to take?: ").lower()
						takeAction(Player1, action, deck, discard)
						print("Your hand now:\n %a" % Player1.getHand())
						anotherAction = input("Would you like to preform another action?(Y or N)").lower()
						if "y" not in anotherAction: #anything that isn't yes is a no
							cardToDiscard = int(input("What card would you like to discard?"))
							Player1.discardCard(cardToDiscard, discard)
							wantAnotherAction = False
						player1Turn = False
				else:
					input("%s, press enter to continue, don't let %s see your actions" % (Player2.getName(), Player1.getName()))
					print("\n" * 100) #clearing console because python is silly
					print("Your hand:\n %a" % Player2.getHand())
					wantAnotherAction = True 
					while wantAnotherAction:
						action = input("What action would you like to take?: ").lower()
						takeAction(Player2, action, deck, discard)
						print("Your hand now:\n %a" % Player2.getHand())
						anotherAction = input("Would you like to preform another action?(Y or N)").lower()
						if "y" not in anotherAction: #anything that isn't yes is a no
							cardToDiscard = int(input("What card would you like to discard?"))
							Player1.discardCard(cardToDiscard, discard)
							print(Player1._hand)
							wantAnotherAction = False
					player1Turn = True
		if Player1.getPoints() >= 100 or Player2.getPoints() >= 100: #score cap for the game
			gameOn = False 
	if Player1.getPoints() > Player2.getPoints():
		winner = Player1
	elif Player2.getPoints() < Player1.getPoints():
		winner = Player2
main()
