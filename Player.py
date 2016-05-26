#John Gouwar, Aryman Babber, Ian Garinger 
#Player.py 
#May 14, 2016
#Implementation of the Player class
class Player:
	def __init__(self, name):
		self._name = name 
		self._hand = [] #empty array for hand 
		self._points = 0 
		self._melds = [] #empty array for meld objects 
#Accessors 
	def getName(self):
		return self._name
	def getHand(self):
		return self._hand
	def getPoints(self):
		return self._points 
	def getSets(self):
		return self._sets
#Mutators 
	def drawCard(self, location):
		'''
		This method draws a card from a given location(deck or discard pile)
		:param location: either Deck or DiscardPile objects where the card will be drawn from
		return: None
		'''
		drawnCard = location.draw()
		self._hand.append(drawnCard)
	def discardCard(self, card, discardPile):
		'''
		This methods takes a card from the player's hand and puts it on top of the discard pile 
		:param card: card object in hand
		:param discardPile: discardPile object initialized in game, same value every time 
		return: None
		'''
		index = self._hand.find(card) #finds the index of the card to pop
		dicardedCard = self._hand.pop(index)
		discardPile._pile.append(card)
	def makeSet(self, cards):
		'''
		This method tests if the cards in the argv can form a legal set and then makes a meld object 
		:param cards: A tuple of all of the arguments(card objects) passed to the function 
		return: None
		'''
		legalSet = True 
		firstCard = cards[0] #card to test against 
		setArray = []
		for card in cards:
			if card.getValue() == firstCard.getValue():
				setArray.append(card)
			else:
				return None
		if legalSet:
			meld = Meld("Set", setArray)
			self._melds.append(meld)
	def makeRun(self, cards):
		'''
		This method tests if the cards in the argv can form a legal run and then makes a meld object
		:param cards: A tuple of all of the arguments(card objects) passed to the function 
		return: None
		'''
		legalRun = True 
		#NEED A WAY TO SORT THE LIST OF CARDS EFFECTIVELY 	
		runArray = [] 
		prevCard = cards[0] #card to test against for legal run 
		for i in range(1, len(cards)):
			if cards[i].getValue() == 1+prevCard.getValue() and cards[i].getSuit == prevCard.getSuit():
				runArray.append(cards[i])
			else:
				return None
			if legalRun:
				meld = Meld("Run", runArray)
				self._melds.append(meld)
	def knock(self):
		'''
		This method is how a player ends the round. They will have made all of their melds and this will calculate their score by adding meld values and removing
		deadwood values.
		return: Total points accrued from the current round 
		'''
		global roundOn 
		pointsAccrued = 0 

		for elt in self._hand:
			if type(elt) == Meld: #checks if it is of class meld 
				pointsAccrued += elt.getPoints()
			else: #deadwood cards
				try: #values are strings which works only for non-face cards
					pointsAccrued -= elt.getValue()
				except TypeError:
					if elt.getValue() == "Ace":
						pointsAccrued -= 1
					else:
						pointsAccrued -= 10 
		roundOn = False 	
 
 
