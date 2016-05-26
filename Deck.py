#John Gouwar, Aryman Babber, Ian Garinger 
#Deck.py
#May 14 2016
#An implementation of the Deck class 
import random

class Card:
    def __init__(self, suit, value):
        self._suit   = suit
        self._value = value
        self._faceUp = False #default face for card is down 
    def getSuit(self):
        return self._suit
    def getValue(self):
        return self._value
    def isFaceUp(self):
        #Returns a bool    
        return self._faceUp
    def __repr__(self):
        return "%s of %s" %(self.getValue(), self.getSuit())
class Deck:
    def __init__(self):
        #the deck is an array of cards
        self._deck = []
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["Ace", "2", "3","4","5","6","7","8","9","10","Jack","Queen","King"]
        #two  for loops for suit and number
        for i in range(len(suits)):
            for j in range(len(values)):
                card = Card(suits[i], values[j])
                self._deck.append(card)                
    def getDeck(self):
        return self._deck
    def deckShuffle(self):
        random.shuffle(self._deck)
    def draw(self):
        return self._deck.pop(0)

class DiscardPile:
    def __init__(self):
        self._pile = []
    
    def draw(self):
        '''
        Draws the top/last card from the pile
        '''
        #in case the discard pile is currently empty
        if len(self._pile) == 0:
            return None
        else:
            return self._pile.pop()
            
