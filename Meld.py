#John Gouwar
#Meld.py
#May 14 2016
#An implementation of the meld Class
class Meld:
	def __init__(self, version, cards):
		self._version = version #will either be Set Or Run
		self._cards = cards #will be a tuple of the cards 
		self._pointsWorth = 0 #initializing the points worth variable 
		for card in cards:
			try:
				self._pointsWorth += int(card.getValue)
			except TypeError: #Face cards exception
				if card.getValue() == "Ace":
					self._pointsWorth += 1
				else: #all other face cards 
					self._pointsWorth += 10
	#accesors 
	def getVersion(self):
		return self._version
	def getCards(self):
		return self._cards 
	def getPointsWorth(self):
		return self._pointsWorth
