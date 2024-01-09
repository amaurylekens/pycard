#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

from pycarddeck.card import Card, Suit, Value

# test value
test_values = [
    (Card(Suit.DIAMONDS, Value.ACE), Value.ACE),
    (Card(Suit.HEARTS, Value.TWO), Value.TWO),
    (Card(Suit.CLUBS, Value.FIVE), Value.FIVE)
]


@pytest.mark.parametrize('card, expected', test_values)
def test_value(card, expected):
    actual = card.value
    assert actual == expected


# test suit
test_values = [
    (Card(Suit.DIAMONDS, Value.ACE), Suit.DIAMONDS),
    (Card(Suit.HEARTS, Value.TWO), Suit.HEARTS),
    (Card(Suit.CLUBS, Value.FIVE), Suit.CLUBS)
]


@pytest.mark.parametrize('card, expected', test_values)
def test_suit(card, expected):
    actual = card.suit
    assert actual == expected


# test __lt__
test_values = [
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    )
]


@pytest.mark.parametrize(
    'card_a, card_b, suit_ordered, suit_ranking, expected', test_values
)
def test_lt(card_a, card_b, suit_ordered, suit_ranking, expected):
    Card.suit_ordered = suit_ordered
    Card.suit_ranking = suit_ranking
    actual = card_a.__lt__(card_b)
    assert actual == expected


# test __eq__
test_values = [
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    )
]


@pytest.mark.parametrize(
    'card_a, card_b, suit_ordered, suit_ranking, expected', test_values
)
def test_lt(card_a, card_b, suit_ordered, suit_ranking, expected):
    Card.suit_ordered = suit_ordered
    Card.suit_ranking = suit_ranking
    actual = card_a.__eq__(card_b)
    assert actual == expected


# test __le__
test_values = [
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.DIAMONDS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.DIAMONDS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        False
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        False,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.TWO), Card(Suit.CLUBS, Value.TWO),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    ),
    (
        Card(Suit.DIAMONDS, Value.ACE), Card(Suit.CLUBS, Value.FOUR),
        True,
        {
            Suit.CLUBS: 0, Suit.SPADES: 1, Suit.HEARTS: 2,
            Suit.DIAMONDS: 3
        },
        True
    )
]


@pytest.mark.parametrize(
    'card_a, card_b, suit_ordered, suit_ranking, expected', test_values
)
def test_lt(card_a, card_b, suit_ordered, suit_ranking, expected):
    Card.suit_ordered = suit_ordered
    Card.suit_ranking = suit_ranking
    actual = card_a.__le__(card_b)
    assert actual == expected

