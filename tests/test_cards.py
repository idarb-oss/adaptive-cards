from adaptivecards.cards import AdaptiveCard


def test_card_configuration(card: AdaptiveCard):
    assert card.schema_ == "http://adaptivecards.io/schemas/adaptive-card.json"
    assert card.type == "AdaptiveCard"
    assert card.version == "1.4"
    assert card.refresh == None
    assert card.authentication == None
    assert len(card.body) == 0
    assert len(card.actions) == 0
    assert card.select_action == None
    assert card.fallback_text == None
    assert card.background_image == None
    assert card.min_height == None
    assert card.rtl == False
    assert card.speak == None
    assert card.lang == None
    assert card.vertical_content_alignment == None
