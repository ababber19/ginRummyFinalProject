#John Gouwar, Aryman Babber, Ian Garinger
#game.py
#May 24 2016
#This is the main game of gin rummy 
from Player import *
from Deck import *
from Meld import *
def getCardFromPlayer(player, card):
	'''
	This method takes a string that the user input and then returns the card object to be used by the program
	:param player: The Player performing the action(Player object)
	:param card: A string given in this form:ValueSuit, each as a single letter or number 
	return: the specific card object from the player's hand
	'''
	if card[0].isdigit()
def takeAction(player, action):
	'''
	This method takes the action a player wants to make a preforms it
	:param player: The player object performing the action 
	:param action: One of the actions defined in README.txt as a string 
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
		setTuple = ()
		numCards = int(input("How many cards in this set?(3 or 4): "))
		if numCards > 2 and numCards < 5:
			for i in range(numCards):
				card = input("Card to add (use rules for naming): ")
				setTuple.append(getCardFromPlayer(player, card)) #adds the card to the set tuple
		else:
			print("Sorry, invalid num of times")
			return None
def main():
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
			if player1Turn:
				input("%s, press enter to continue, don't let %s see your actions" % (Player1.getName(), Player2.getName()))
				print("\n" * 100) #clearing console because python is silly
				print("Your hand:\n %a" % Player1.getHand())
				wantAnotherAction = True 
				while wantAnotherAction: #controling loop for turn actions
					action = input("What action would you like to take?: ").lower()
					takeAction(Player1, action)
			else:
				input("%s, press enter to continue, don't let %s see your actions" % (Player2.getName(), Player1.getName()))
				print("\n" * 100) #clearing console because python is silly
				print("Your hand:\n %a" % Player2.getHand())
				wantAnotherAction = True 
				while wantAnotherAction:
					action = input("What action would you like to take?: ").lower()
					takeAction(Player2, action)
		if Player1.getPoints() >= 100 or Player2.getPoints() >= 100: #score cap for the game
			gameOn = False 
	if Player1.getPoints() > Player2.getPoints():
		winner = Player1
	elif Player2.getPoints() < Player1.getPoints():
		winner = Player2
main()
			 
			
	
  
