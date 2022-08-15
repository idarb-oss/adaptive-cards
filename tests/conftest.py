import pytest

from msadaptivecards.cards import AdaptiveCard


@pytest.fixture
def card():
    new_card = AdaptiveCard()
    yield new_card
