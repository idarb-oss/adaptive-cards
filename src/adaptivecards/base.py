"""
"""
from typing import Dict

from humps import camelize
from pydantic import BaseModel, Field

from .types import ActionMode, ActionStyle, BlockElementHeight, Spacing


def _to_camel(string: str):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = _to_camel
        allow_population_by_field_name = True


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
