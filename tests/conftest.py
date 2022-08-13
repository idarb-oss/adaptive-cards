import pytest

from adaptivecards.cards import AdaptiveCard


@pytest.fixture
def card():
    new_card = AdaptiveCard()
    yield new_card
