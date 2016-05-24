#John Gouwar, Aryman Babber, Ian Garinger
#game.py
#May 24 2016
#This is the main game of gin rummy 
from Deck import *
from Player import *
from DiscardPile import *
from Meld import *
def main():
	input("Welcome to the Gin Rummy Extravaganza! Press Enter to continue")
	player1Name = input("What is player 1's name?: ")
	player2Name = input("What is player 2's name?: ")
	Player1 = Player(player1Name); Player2 = Player(player2Name)
	gameOn = True
	while gameOn: #controling loop for the game
		roundOn = True
		while roundOn: #controling loop for round
			deck = Deck()
			deck.shuffle()
			for i in range(10):
				Player1.drawCard(deck)
				Player2.drawCard(deck)
			input("%s, press enter to continue, don't let %s see your actions" % (Player1.getName(), Player2.getName())
			print("\n" * 100) #clearing console because python is silly
			print("Your hand:\n %a" % Player1.getHand())
			
			
	
  
