"""
"""
from typing import List, Literal, Union

from pydantic import Field

from .base import ActionModel, BackgroundImage, CamelModel, ElementModel, SelectAction


class AdaptiveCard(CamelModel):
    """An Adaptive Card, containing a free-form body of card elements, and an optional set of actions."""

    schema_: str = Field(
        "http://adaptivecards.io/schemas/adaptive-card.json", description="The Adaptive Card schema.", alias="$schema"
    )
    type: Literal["AdaptiveCard"] = Field("AdaptiveCard", description="Must be 'AdaptiveCard'.")
    version: str = Field(
        "1.4",
        description="Schema version that this card requires. If a client is lower than this version, the fallbackText "
        "will be rendered. NOTE: Version is not required for cards within an Action.ShowCard. However, it is required "
        "for the top-level card.",
    )
    refresh: str = Field(
        None, description="Defines how the card can be refreshed by making a request to the target Bot."
    )
    authentication: str = Field(
        None,
        description="Defines authentication information to enable on-behalf-of single sign on or just-in-time OAuth.",
    )
    body: List[ElementModel] = Field(
        default_factory=list, description="The card elements to show in the primary card region."
    )
    actions: List[ActionModel] = Field(
        default_factory=list, description="The Actions to show in the card's action bar."
    )
    select_action: SelectAction = Field(
        None,
        description="An Action that will be invoked when the card is tapped or selected. Action.ShowCard is not "
        "supported.",
    )
    fallback_text: str = Field(
        None, description="Text shown when the client doesn't support the version specified (may contain markdown)."
    )
    background_image: Union[BackgroundImage, str] = Field(
        None, description="Specifies the background image of the card."
    )
    min_height: str = Field(None, description="Specifies the minimum height of the card.")
    rtl: bool = Field(
        False,
        description="When true content in this Adaptive Card should be presented right to left. When 'false' content "
        "in this Adaptive Card should be presented left to right. If unset, the default platform behavior will apply.",
    )
    speak: str = Field(
        None, description="Specifies what should be spoken for this entire card. This is simple text or SSML fragment."
    )
    lang: str = Field(
        None, description="The 2-letter ISO-639-1 language used in the card. Used to localize any date/time functions."
    )
    vertical_content_alignment: str = Field(
        None,
        description="Defines how the content should be aligned vertically within the container. Only relevant for "
        "fixed-height cards, or cards with a minHeight specified.",
    )
