"""
"""
from enum import Enum
from typing import Dict

from humps import camelize
from pydantic import BaseModel, Field


def _to_camel(string: str):
    return camelize(string)


class CamelModel(BaseModel):
    """
    Standard configuration for Pydantic BaseModel to generate camel cased json which is what adaptive cards uses.
    """

    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True


class ImageFillMode(Enum):
    """
    Describes how the image should fill the area.
    See More: https://adaptivecards.io/explorer/BackgroundImage.html

    Attributes:
        COVER (str):
            The background image covers the entire width of the container. Its aspect ratio is preserved.
            Content may be clipped if the aspect ratio of the image doesn't match the aspect ratio of the container.
            verticalAlignment is respected (horizontalAlignment is meaningless since it's stretched width). This is
            the default mode and is the equivalent to the current model.
        REPEAT_HORIZONTALLY (str):
            The background image isn't stretched. It is repeated in the x axis as many times as necessary to cover
            the container's width. verticalAlignment is honored (default is top), horizontalAlignment is ignored.
        REPEAT_VERTICALLY (str):
            The background image isn't stretched. It is repeated in the y axis as many times as necessary to cover the
            container's height. verticalAlignment is ignored, horizontalAlignment is honored (default is left).
        REPEAT (str):
            The background image isn't stretched. It is repeated first in the x axis then in the y axis as many times
            as necessary to cover the entire container. Both horizontalAlignment and verticalAlignment are
            honored (defaults are left and top).
    """

    COVER = "cover"
    REPEAT_HORIZONTALLY = "repeatHorizontally"
    REPEAT_VERTICALLY = "repeatVertically"
    REPEAT = "repeat"


class HorizontalAlignment(Enum):
    """
    Describes how the image should be aligned if it must be cropped or if using repeat fill mode.

    See More: https://adaptivecards.io/explorer/BackgroundImage.html

    Attributes:
        LEFT:
            Position to the left.
        CENTER:
            Position in the center.
        RIGHT:
            Position to the right.
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class VerticalAlignment(Enum):
    """
    Describes how the image should be aligned if it must be cropped or if using repeat fill mode.

    See More: https://adaptivecards.io/explorer/BackgroundImage.html

    Attributes:
        TOP:
            Position to the top.
        CENTER:
            Position in the center.
        BOTTOM:
            Position to the bottom.
    """

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class Style(Enum):
    """
    Style hint for Container.

    See More: https://adaptivecards.io/explorer/Container.html

    Attributes:
        DEFAULT:
            Default style with
        EMPHASIS:
            Emphasis the background color of the container
        GOOD:
            'Good' background color, a green color type
        ATTENTION:
            'Attention' color, orange/red color type
        WARNING:
            'Warning' color, yellow/orange color type
        ACCENT:
            'Accent' color, blue color type
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

    Attributes:
        AUTO:
            The height of the container will be determined by the height of its contents.
        STRETCH:
            The container will stretch its height to the available remaining height of the parent container.
    """

    AUTO = "auto"
    STRETCH = "stretch"


class Spacing(Enum):
    """
    Controls the amount of spacing between this element and the preceding element.

    Attributes:
        DEFAULT:
            Default spacing
        NONE:
            No spacing between elements
        SMALL:
            Small spacing between elements
        MEDIUM:
            Medium spacing between elements
        LARGE:
            Large spacing between elements
        EXTRA_LARGE:
            Extra large spacing between elements
        PADDING:
            Add padding between elements
    """

    DEFAULT = "default"
    NONE = "none"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"
    PADDING = "padding"


class Colors(Enum):
    """
    Controls the color of TextBlock elements.

    Attributes:
        DEFAULT:
            Default black
        DARK:
            Black
        LIGHT:
            Light green
        ACCENT:
            Blue
        GOOD:
            Green
        WARNING:
            Orange
        ATTENTION:
            Yellow
    """

    DEFAULT = "default"
    DARK = "dark"
    LIGHT = "light"
    ACCENT = "accent"
    GOOD = "good"
    WARNING = "warning"
    ATTENTION = "attention"


class FontType(Enum):
    """
    Type of font to use for rendering.

    Attributes:
        DEFAULT:
            Default font
        MONOSPACE:
            Monospace font
    """

    DEFAULT = "default"
    MONOSPACE = "monospace"


class FontSize(Enum):
    """
    Controls size of text.

    Attributes:
        DEFAULT:
            Default size
        SMALL:
            Small font size
        MEDIUM:
            Medium font size
        LARGE:
            Large font size
        EXTRA_LARGE:
            Larger font size
    """

    DEFAULT = "default"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"


class FontWeight(Enum):
    """
    Controls the weight of TextBlock elements.

    Attributes:
        DEFAULT:
            Normal weight for the font
        LIGHTER:
            Font has lighter lines
        BOLDER:
            Bold font size
    """

    DEFAULT = "default"
    LIGHTER = "lighter"
    BOLDER = "bolder"


class TextBlockStyle(Enum):
    """
    The style of this TextBlock for accessibility purposes.

    Attributes:
        DEFAULT:
            This is the default style which provide no special styling or behavior.
        HEADING:
            The TextBlock is a heading. This will apply the heading styling defaults and mark the text block as a
            heading for accessibility.
    """

    DEFAULT = "default"
    HEADING = "heading"


class ActionStyle(Enum):
    """
    Controls the style of an Action, which influences how the action is displayed, spoken, etc.

    Attributes:
        DEFAULT:
            Action is displayed as normal
        POSITIVE:
            Action is displayed with a positive style (typically the button becomes accent color)
        DESTRUCTIVE:
            Action is displayed with a destructive style (typically the button becomes red)
    """

    DEFAULT = "default"
    POSITIVE = "positive"
    DESTRUCTIVE = "destructive"


class ActionMode(Enum):
    """
    Determines whether the action should be displayed as a button or in the overflow menu.

    Attributes:
        PRIMARY:
            Action is displayed as a button.
        SECONDARY:
            Action is placed in an overflow menu (typically a popup menu under a ... button).
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"


class AssociatedInputs(Enum):
    """
    Controls which inputs are associated with the submit action.

    Attributes:
        AUTO:
            Inputs on the current card and any parent cards will be validated and submitted for this Action.
        NONE:
            None of the inputs will be validated or submitted for this Action.
    """

    AUTO = "Auto"
    NONE = "None"


class BackgroundImage(CamelModel):
    """
    Specifies a background image. Acceptable formats are PNG, JPEG, and GIF

    Keyword Args:
        url (str):
            The URL (or data url) of the image. Acceptable formats are PNG, JPEG, and GIF
        fill_mode (ImageFillMode):
            Describes how the image should fill the area.
        horizontal_alignment (HorizontalAlignment):
            Describes how the image should be aligned if it must be cropped or if using repeat fill mode.
        vertical_alignment (VerticalAlignment):
            Describes how the image should be aligned if it must be cropped or if using repeat fill mode.
    """

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
    """
    Base model for element types

    Keyword Args:
        fallback (ElementModel):
            Describes what to do when an unknown element is encountered or the requires of this or any children
            can't be met.
        height (BlockElementHeight):
            Specifies the height of the element.
        separator (bool):
            When true, draw a separating line at the top of the element.
        spacing (Spacing):
            Controls the amount of spacing between this element and the preceding element.
        id (str):
            A unique identifier associated with the item.
        is_visible (bool):
            If false, this item will be removed from the visual tree.
        requires (Dict[str, str]):
            A series of key/value pairs indicating features that the item requires with corresponding minimum version.
            When a feature is missing or of insufficient version, fallback is triggered.

    """

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
        None,
        description="A series of key/value pairs indicating features that the item requires with corresponding "
        "minimum version. When a feature is missing or of insufficient version, fallback is triggered.",
    )


class ActionModel(CamelModel):
    """
    Base model for all action types

    Keyword Args:
        title (str):
            Label for button or link that represents this action.
        icon_url (str):
            Optional icon to be shown on the action in conjunction with the title. Supports data URI in version 1.2+
        id (str):
            A unique identifier associated with this Action.
        style (ActionStyle):
            Controls the style of an Action, which influences how the action is displayed, spoken, etc.
        fallback (ActionModel):
            Describes what to do when an unknown element is encountered or the requires of this or any
            children can't be met.
        tooltip (str):
            Defines text that should be displayed to the end user as they hover the mouse over the action,
            and read when using narration software.
        is_enabled (bool):
            Determines whether the action should be enabled.
        mode (ActionMode):
            Determines whether the action should be displayed as a button or in the overflow menu.
        requires (Dict[str, str]):
            A series of key/value pairs indicating features that the item requires with corresponding minimum version.
            When a feature is missing or of insufficient version, fallback is triggered.
    """

    title: str = Field(None, description="Label for button or link that represents this action.")
    icon_url: str = Field(
        None,
        description="Optional icon to be shown on the action in conjunction with the title. "
        "Supports data URI in version 1.2+",
    )
    id: str = Field(None, description="A unique identifier associated with this Action.")
    style: ActionStyle = Field(
        None,
        description="Controls the style of an Action, which influences how the action is displayed, spoken, etc.",
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
        None, description="Determines whether the action should be displayed as a button or in the overflow menu."
    )
    requires: Dict[str, str] = Field(
        default_factory=dict,
        description="A series of key/value pairs indicating "
        "features that the item requires with corresponding minimum version. When a feature is missing or of "
        "insufficient version, fallback is triggered.",
    )


class SelectAction(ActionModel):
    """
    Marker model for select actions.
    """

    pass


class BaseContainers(CamelModel):
    """
    Base model for all containers.

    Keyword Args:
        fallback (ElementModel):
            Describes what to do when an unknown element is encountered or the requires of this or any children
            can't be met.
         height (BlockElementHeight):
            Specifies the height of the element.
         separator (bool):
            When true, draw a separating line at the top of the element.
         spacing (Spacing):
            Controls the amount of spacing between this element and the preceding element.
         id (str):
            A unique identifier associated with the item.
         is_visible:
            If false, this item will be removed from the visual tree.
         requires (Dict[str, str]):
            A series of key/value pairs indicating features that the item requires with corresponding minimum version.
            When a feature is missing or of insufficient version, fallback is triggered.
    """

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
