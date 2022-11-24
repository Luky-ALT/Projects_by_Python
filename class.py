class Card():
    SPADES = "Spades"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    COLORS = SPADES, HEARTS, DIAMONDS, CLUBS

    LOW_RANKS = tuple(str(number) for number in range(2, 11))
    HIGH_RANKS = JACK, QUEEN, KING, ACE = "JACK", "QUEEN", "KING", "ACE"
    RANKS = LOW_RANKS + HIGH_RANKS

    def __init__(self, color, rank):
        color = color.capitalize()
        rank = str(rank)
        if color not in Card.COLORS:
            raise ValueError(f"Invalid color {color}.")  # raise sluzi na vyvolanie chyyby
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid ranked{rank}.")
        self.color = color
        self.rank = rank

    def rank_value(self):
        return self.RANKS.index(self.rank)

    def is_high(self):
        return self.rank in Card.HIGH_RANKS

    def __eq__(self, other):  # sa pouziva, ked jedna karta sa rovna druhej
        return self.color == other.color and self.rank == other.rank

    def __lt__(a, b):
        return a.rank_value() < b.rank_value()

    def __repr__(self):
        return f'Card("{self.color}","{self.rank}")'

    if __name__ == "__main__":
        main()
