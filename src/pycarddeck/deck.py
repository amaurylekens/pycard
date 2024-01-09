#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

import random
from typing import Optional, Generator, List, Iterator, Tuple

from src.pycarddeck.card import Card, Suit, Value


class Deck:
    def __init__(
        self, initialise: bool = True, shuffle: bool = False,
        n: Optional[int] = None, override: Optional[Tuple[Card], ...] = None,
        seed: Optional[int] = None
    ):

        """
        :param initialise:
        :param shuffle
        :param n:
        :param override:
        :param seed:
        """

        self._deck: list = list()

        if initialise:
            self.initialise(shuffle, n, seed)

        if override is not None:
            self._deck = list(override)

    @property
    def empty(self) -> bool:

        """
        Says if the deck is empty.

        :return: True if the deck is empty.
        :rtype: bool
        """

        return len(self._deck) == 0

    @property
    def cards_count(self) -> int:

        """
        Number of remaining cards in the deck.

        :return: Number of remaining cards in the decks.
        :rtype: int
        """

        return len(self._deck)

    def initialise(
        self, shuffle: bool = False, n: Optional[int] = None,
        seed: Optional[int] = None
    ) -> None:

        """
        Initialize the deck. The deck can be shuffled and the number of the
        first card to keep can be specified.

        :param shuffle: Bool to say if the cards have to be shuffled.
        :type shuffle: bool
        :param n: Number of first cards kept.
        :type n: int
        :param seed: Seed for shuffling operation.
        :type seed: int
        """

        self.clear()

        for suit in Suit:
            for value in Value:
                self._deck.append(Card(suit, value))

        if shuffle:
            self.shuffle(seed)

        if n:
            self._deck = self._deck[:n]

    def clear(self) -> None:

        """
        That empties the deck.
        """

        self._deck = list()

    def shuffle(self, seed: Optional[int]) -> None:

        """
        Shuffles the deck.
        """

        if seed:
            random.seed(seed)

        random.shuffle(self._deck)

    def draw(self, n: int = 1) -> Generator[Card, None, None]:

        """
        Method that yields the topmost card from the deck.

        :param n: Number of cards to yield.
        :type n: int
        :return: generator - generator of cards to deal.
        :rtype: Generator[Card, None, None]
        """

        for i in range(n):

            if self.empty:
                break

            yield self._deck.pop(0)

    def draw_bottom(self, n: int = 1) -> Generator[Card, None, None]:

        """
        Yields the bottommost card from the deck.

        :param n: Number of cards to yield.
        :type n: int
        :return: generator - generator of cards to deal.
        :rtype: Generator[Card, None, None]
        """

        for i in range(n):

            if self.empty:
                break

            yield self._deck.pop(-1)

    def draw_random(
        self, n: int = 1, seed: Optional[int] = None
    ) -> Generator[Card, None, None]:

        """
        Yields the bottommost card from the deck.

        :param n: Number of cards to yield.
        :type n: int
        :param seed: Seed for the random drawing.
        :type seed: int
        :return: generator - generator of cards to deal.
        :rtype: Generator[Card, None, None]
        """

        if seed:
            random.seed(seed)

        for i in range(n):

            if self.empty:
                break

            index = random.randint(0, len(self._deck)-1)
            yield self._deck.pop(index)

    def add_card(
        self, card: Card, position: Optional[int] = None,
        seed: Optional[int] = None
    ) -> None:

        """
        Inserts a single card into the deck.

        :param card: Card to insert
        :type card: Card
        :param position: To insert card to a specific position of the deck
                         (0 = top of the deck). By default, the position is
                         random.
        :type position: Optional[int]
        :param seed: Seed for the random position (when position is random).
        :type seed: Optional[int]
        """

        if seed:
            random.seed(seed)

        if position:
            self._deck.insert(position, card)

        else:
            self._deck.insert(random.randint(0, len(self._deck)), card)

    def add_cards(
        self, cards: List[Card], seed: Optional[int] = None
    ) -> None:

        """
        Inserts many cards into the deck at random position.

        :param cards: List of card to insert.
        :type cards: List[Card]
        :param seed: Seed for the random positions (when position is random).
        :type seed: Optional[int]
        """

        for card in cards:
            self.add_card(card, seed=seed)

    def __iter__(self) -> Iterator[Card]:

        return iter(self._deck)

    def __eq__(self, other: Deck) -> bool:

        return self._deck == other._deck


if __name__ == "__main__":
    deck = Deck()

    for card in deck:

        print(card)
