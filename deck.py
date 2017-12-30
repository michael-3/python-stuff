from enum import Enum
from collections import namedtuple
import random

class Suite(Enum):
    DIAMOND = 0
    CLOVER = 1
    HEART = 2
    SPADE = 3

# A deck will be represented as a list of tuples where the first element is the
# value and the second element is the suite. ('A', SPADE)
class Deck(object):

    values = ['A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    Card = namedtuple('Card', 'value suite')

    def __init__(self):
        self.deck = []
        for value in Deck.values:
            for suite in Suite:
                self.deck.append(Deck.Card(value, suite))

    def draw(self):
        return self.deck.pop()

    # Yates shuffle algorithm
    def shuffle(self):
        for i in xrange(len(self.deck)-1, -1, -1):
            n = random.randint(0,i)
            self.deck[i], self.deck[n] = self.deck[n], self.deck[i]

    def __len__(self):
        return len(self.deck)
