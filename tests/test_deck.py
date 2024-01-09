#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

from src.pycarddeck.deck import Deck
from src.pycarddeck.card import Card, Suit, Value

# Set the seed
SEED = 42


# test empty
test_values = [
    (Deck(), False),
    (Deck(initialise=False), True),
    (Deck(initialise=True, shuffle=True, seed=SEED), False),
    (Deck(n=13), False)
]


@pytest.mark.parametrize('deck, expected', test_values)
def test_empty(deck, expected):
    actual = deck.empty
    assert actual == expected


# test cards_count
test_values = [
    (Deck(), 52),
    (Deck(initialise=False), 0),
    (Deck(shuffle=True, seed=SEED), 52),
    (Deck(n=13), 13),
    (Deck(shuffle=True, n=16, seed=SEED), 16),
]


@pytest.mark.parametrize('deck, expected', test_values)
def test_cards_count(deck, expected):
    actual = deck.cards_count
    assert actual == expected


# test shuffle
test_values = [
    (
        Deck(n=3), Deck(
            n=3,
            override=(
                Card(Suit.SPADES, Value.TWO), Card(Suit.SPADES, Value.ACE),
                Card(Suit.SPADES, Value.THREE)
            )
        )
    )
]


@pytest.mark.parametrize('deck, expected', test_values)
def test_shuffle(deck, expected):

    deck.shuffle(SEED)
    assert deck == expected


# test initialise
test_values = [
    (Deck(), None, False, Deck()),
    (Deck(), 10, False, Deck(n=10)),
    (
        Deck(), 4, True, Deck(
            override=(
                Card(Suit.SPADES, Value.TEN), Card(Suit.HEARTS, Value.JACK),
                Card(Suit.HEARTS, Value.KING), Card(Suit.SPADES, Value.FOUR)
            )
        )
    )
]


@pytest.mark.parametrize('deck, n, shuffle, expected', test_values)
def test_initialise(deck, n, shuffle, expected):
    deck.initialise(n=n, shuffle=shuffle, seed=SEED)
    assert deck == expected


# test clear
test_values = [
    (Deck(), Deck(override=tuple())),
    (Deck(n=10), Deck(override=tuple())),
    (Deck(n=10, shuffle=True, seed=SEED), Deck(override=tuple()))
]


@pytest.mark.parametrize('deck, expected', test_values)
def test_clear(deck, expected):
    deck.clear()
    assert deck == expected


# test draw
test_values = [
    (Deck(), 0, []),
    (Deck(), 1, [Card(Suit.SPADES, Value.ACE)]),
    (Deck(shuffle=True, seed=SEED), 1, [Card(Suit.SPADES, Value.TEN)]),
    (
        Deck(), 3,
        [
            Card(Suit.SPADES, Value.ACE), Card(Suit.SPADES, Value.TWO),
            Card(Suit.SPADES, Value.THREE)
        ]
    ),
    (
        Deck(n=2), 3,
        [
            Card(Suit.SPADES, Value.ACE), Card(Suit.SPADES, Value.TWO)
        ]
    )
]


@pytest.mark.parametrize('deck, n, expected', test_values)
def test_draw(deck, n, expected):
    actual = list(deck.draw(n))
    assert actual == expected


# test draw_bottom
test_values = [
    (Deck(), 0, []),
    (Deck(), 1, [Card(Suit.CLUBS, Value.KING)]),
    (Deck(shuffle=True, seed=SEED), 1, [Card(Suit.CLUBS, Value.TWO)]),
    (
        Deck(), 3,
        [
            Card(Suit.CLUBS, Value.KING), Card(Suit.CLUBS, Value.QUEEN),
            Card(Suit.CLUBS, Value.JACK)
        ]
    ),
    (
        Deck(n=2), 3,
        [
            Card(Suit.SPADES, Value.TWO), Card(Suit.SPADES, Value.ACE)
        ]
    )
]


@pytest.mark.parametrize('deck, n, expected', test_values)
def test_draw_bottom(deck, n, expected):
    actual = list(deck.draw_bottom(n))
    assert actual == expected


# test draw_random
test_values = [
    (Deck(), 0, []),
    (Deck(), 1, [Card(Suit.CLUBS, Value.TWO)]),
    (Deck(shuffle=True, seed=SEED), 1, [Card(Suit.DIAMONDS, Value.QUEEN)]),
    (
        Deck(), 3,
        [
            Card(Suit.CLUBS, Value.TWO), Card(Suit.SPADES, Value.EIGHT),
            Card(Suit.SPADES, Value.TWO)
        ]
    ),
    (
        Deck(n=2), 3,
        [
            Card(Suit.SPADES, Value.ACE), Card(Suit.SPADES, Value.TWO)
        ]
    )
]


@pytest.mark.parametrize('deck, n, expected', test_values)
def test_draw_random(deck, n, expected):
    actual = list(deck.draw_random(n, seed=SEED))
    assert actual == expected


# test add_card
test_values = [
    (
        Deck(override=tuple()), Card(Suit.SPADES, Value.TWO), 0,
        Deck(override=(Card(Suit.SPADES, Value.TWO),))
    ),
    (
        Deck(override=(Card(Suit.SPADES, Value.TWO),)),
        Card(Suit.SPADES, Value.KING), 0,
        Deck(
            override=(
                Card(Suit.SPADES, Value.KING), Card(Suit.SPADES, Value.TWO)
            )
        )

    ),
    (
        Deck(override=(Card(Suit.SPADES, Value.TWO),)),
        Card(Suit.SPADES, Value.KING), None,
        Deck(
            override=(
                Card(Suit.SPADES, Value.KING), Card(Suit.SPADES, Value.TWO)
            )
        )

    )
]


@pytest.mark.parametrize('deck, card, position, expected', test_values)
def test_add_card(deck, card, position, expected):
    deck.add_card(card, seed=SEED)
    assert deck == expected


# test add_cards
test_values = [
    (
        Deck(override=tuple()), [Card(Suit.SPADES, Value.TWO)],
        Deck(override=(Card(Suit.SPADES, Value.TWO),))
    ),
    (
        Deck(override=(Card(Suit.SPADES, Value.TWO),)),
        [Card(Suit.SPADES, Value.KING)],
        Deck(
            override=(
                Card(Suit.SPADES, Value.KING), Card(Suit.SPADES, Value.TWO)
            )
        )

    ),
    (
        Deck(override=(Card(Suit.SPADES, Value.TWO),)),
        [Card(Suit.SPADES, Value.KING), Card(Suit.DIAMONDS, Value.KING)],
        Deck(
            override=(
                Card(Suit.SPADES, Value.KING), Card(Suit.SPADES, Value.TWO),
                Card(Suit.DIAMONDS, Value.KING)
            )
        )

    )
]


@pytest.mark.parametrize('deck, cards, expected', test_values)
def test_add_cards(deck, cards, expected):
    deck.add_cards(cards, seed=SEED)
    assert deck == expected

