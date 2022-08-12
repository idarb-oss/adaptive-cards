"""
"""
from enum import Enum

from pydantic import Field

from .base import CamelModel


class ImageFillMode(Enum):
    """
    Describes how the image should fill the area.
    See More: https://adaptivecards.io/explorer/BackgroundImage.html
    """

    COVER = "cover"
    REPEAT_HORIZONTALLY = "repeatHorizontally"
    REPEAT_VERTICALLY = "repeatVertically"
    REPEAT = "repeat"


class HorizontalAlignment(Enum):
    """
    Describes how the image should be aligned if it must be cropped or if using repeat fill mode.

    See More: https://adaptivecards.io/explorer/BackgroundImage.html
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class VerticalAlignment(Enum):
    """
    Describes how the image should be aligned if it must be cropped or if using repeat fill mode.

    See More: https://adaptivecards.io/explorer/BackgroundImage.html
    """

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class Style(Enum):
    """
    Style hint for Container.

    See More: https://adaptivecards.io/explorer/Container.html
    """

    DEFAULT = "default"
    EMPHASIS = "emphasis"
    GOOD = "good"
    ATTENTION = "attention"
    WARNING = "warning"
    ACCENT = "accent"


class BlockElementHeight(Enum):
    """
    Specifies the height of the element.
    """

    AUTO = "auto"
    STRETCH = "stretch"


class Spacing(Enum):
    """
    Controls the amount of spacing between this element and the preceding element.
    """

    DEFAULT = "default"
    NONE = "none"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"
    PADDING = "padding"


class Colors(Enum):
    """Controls the color of TextBlock elements."""

    DEFAULT = "default"
    DARK = "dark"
    LIGHT = "light"
    ACCENT = "accent"
    GOOD = "good"
    WARNING = "warning"
    ATTENTION = "attention"


class FontType(Enum):
    """Type of font to use for rendering"""

    DEFAULT = "default"
    MONOSPACE = "monospace"


class FontSize(Enum):
    """Controls size of text."""

    DEFAULT = "default"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"


class FontWeight(Enum):
    """Controls the weight of TextBlock elements."""

    DEFAULT = "default"
    LIGHTER = "lighter"
    BOLDER = "bolder"


class TextBlockStyle(Enum):
    """The style of this TextBlock for accessibility purposes."""

    DEFAULT = "default"
    HEADING = "heading"


class ActionStyle(Enum):
    """Controls the style of an Action, which influences how the action is displayed, spoken, etc."""

    DEFAULT = "default"
    POSITIVE = "positive"
    DESTRUCTIVE = "destructive"


class ActionMode(Enum):
    """Determines whether the action should be displayed as a button or in the overflow menu."""

    PRIMARY = "primary"
    SECONDARY = "secondary"


class AssociatedInputs(Enum):
    """Controls which inputs are associated with the submit action."""

    AUTO = "Auto"
    NONE = "None"


class BackgroundImage(CamelModel):
    """Specifies a background image. Acceptable formats are PNG, JPEG, and GIF"""

    url: str = Field(..., description="The URL (or data url) of the image. Acceptable formats are PNG, JPEG, and GIF")
    fill_mode: ImageFillMode = Field(None, description="Describes how the image should fill the area.")
    horizontal_alignment: HorizontalAlignment = Field(
        None,
        description="Describes how the image should be aligned if it must be cropped or if using repeat fill mode.",
    )
    vertical_alignment: VerticalAlignment = Field(
        None,
        description="Describes how the image should be aligned if it must be cropped or if using repeat fill mode.",
    )
