"""
"""
from enum import Enum
from typing import Dict

from humps import camelize
from pydantic import BaseModel, Field


def _to_camel(string: str):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True


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


class ElementModel(CamelModel):
    """"""

    fallback: "ElementModel" = Field(
        None,
        description="Describes what to do when an unknown element is encountered or the requires of this or any "
        "children can't be met.",
    )
    height: BlockElementHeight = Field(None, description="Specifies the height of the element.")
    separator: bool = Field(None, description="When true, draw a separating line at the top of the element.")
    spacing: Spacing = Field(
        None, description="Controls the amount of spacing between this element and the preceding element."
    )
    id: str = Field(None, description="A unique identifier associated with the item.")
    is_visible: bool = Field(True, description="If false, this item will be removed from the visual tree.")
    requires: Dict[str, str] = Field(
        default_factory=dict,
        description="A series of key/value pairs indicating features that the item requires with corresponding "
        "minimum version. When a feature is missing or of insufficient version, fallback is triggered.",
    )


class ActionModel(CamelModel):
    """"""

    title: str = Field(None, description="Label for button or link that represents this action.")
    icon_url: str = Field(
        None,
        description="Optional icon to be shown on the action in conjunction with the title. "
        "Supports data URI in version 1.2+",
    )
    id: str = Field(None, description="A unique identifier associated with this Action.")
    style: ActionStyle = Field(
        None,
        description="Controls the style of an Action, which influences how the action is " "displayed, spoken, etc.",
    )
    fallback: "ActionModel" = Field(
        None,
        description="Describes what to do when an unknown element is encountered or "
        "the requires of this or any children can’t be met.",
    )
    tooltip: str = Field(
        None,
        description="Defines text that should be displayed to the end user as they hover the "
        "mouse over the action, and read when using narration software.",
    )
    is_enabled: bool = Field(True, description="Determines whether the action should be enabled.")
    mode: ActionMode = Field(
        None, description="Determines whether the action should be displayed as a button or in " "the overflow menu."
    )
    requires: Dict[str, str] = Field(
        default_factory=dict,
        description="A series of key/value pairs indicating "
        "features that the item requires with corresponding minimum version. When a feature is missing or of "
        "insufficient version, fallback is triggered.",
    )


class SelectAction(ActionModel):
    """"""

    pass


class BaseContainers(CamelModel):
    """"""

    fallback: ElementModel = Field(
        None,
        description="Describes what to do when an unknown element is encountered or "
        "the requires of this or any children can't be met.",
    )
    height: BlockElementHeight = Field(None, description="Specifies the height of the element.")
    separator: bool = Field(None, description="When true, draw a separating line at the top of the element.")
    spacing: Spacing = Field(
        None, description="Controls the amount of spacing between this element and the preceding element."
    )
    id: str = Field(None, description="A unique identifier associated with the item.")
    is_visible: bool = Field(True, description="If false, this item will be removed from the visual tree.")
    requires: Dict[str, str] = Field(
        default_factory=dict,
        description="A series of key/value pairs indicating features that "
        "the item requires with corresponding minimum version. When a feature is missing or of insufficient version, "
        "fallback is triggered.",
    )
