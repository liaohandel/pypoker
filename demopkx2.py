
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, count):
        count = min(count, self.count())
        return [self.cards.pop() for _ in range(count)]
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        
        #self.shuffle(self.cards)
        return self

def main():
    deck = Deck()
    deck.shuffle()

    hand = deck.deal_hand(5)
    print(hand)
    hand = deck.deal_hand(5)
    print(hand)


if __name__ == '__main__':
    main()