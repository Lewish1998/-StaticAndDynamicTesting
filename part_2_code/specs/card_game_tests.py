import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('heart', 1)
        self.card2 = Card('diamond', 3)

    def testHasSuit(self):
        self.assertEqual('heart', self.card1.suit)

    def testHasValue(self):
        self.assertEqual(3, self.card2.value)

    def testCheckAce(self):
        test = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, test)
          
    def testHighestCard(self):
        test = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, test)
        
    def testCardsTotal(self):
        cards = [self.card1, self.card2]
        test=CardGame.cards_total(self, cards)
        self.assertEqual('You have a total of 4', test)

#     def cards_total(self, cards):
#   total
#   for card in cards:
#     total += card.value
#     return "You have a total of" + total