"""
"""
from typing import Literal

from pydantic import Field

from .base import Colors, ElementModel, FontSize, FontType, FontWeight, HorizontalAlignment, TextBlockStyle


class TextBlock(ElementModel):
    """Displays text, allowing control over font sizes, weight, and color."""

    type: Literal["TextBlock"] = Field("TextBlock", description="Must be 'TextBlock'.")
    text: str = Field(
        ..., description="Text to display. A subset of markdown is supported " "(https://aka.ms/ACTextFeatures)"
    )
    colors: Colors = Field(None, describe="Controls the color of TextBlock elements.")
    fontType: FontType = Field(None, description="Type of font to use for rendering")
    horizontal_alignment: HorizontalAlignment = Field(
        None,
        description="Controls the horizontal text alignment. "
        "When not specified, the value of horizontalAlignment is inherited from the parent container. If no parent "
        "container has horizontalAlignment set, it defaults to Left.",
    )
    is_subtle: bool = Field(None, description="If true, displays text slightly toned down to appear less prominent.")
    maxLines: int = Field(None, description="Specifies the maximum number of lines to display.")
    size: FontSize = Field(None, description="Controls size of text.")
    weight: FontWeight = Field(None, description="Controls the weight of TextBlock elements.")
    wrap: bool = Field(None, description="If true, allow text to wrap. Otherwise, text is clipped.")
    style: TextBlockStyle = Field(None, description="The style of this TextBlock for accessibility purposes.")
