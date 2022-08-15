"""
"""
from typing import Dict, List, Literal, Union

from pydantic import BaseModel, Field

from .base import (
    BackgroundImage,
    BaseContainers,
    CamelModel,
    ElementModel,
    HorizontalAlignment,
    SelectAction,
    Spacing,
    Style,
    VerticalAlignment,
)


class Container(BaseContainers):
    """Containers group items together."""

    type: Literal["Container"] = Field("Container", description="Must be 'Container'.")
    items: List[ElementModel] = Field(
        default_factory=list, description="The card elements to render inside the " "Container."
    )
    select_action: SelectAction = Field(
        None,
        description="An Action that will be invoked when the Container is "
        "tapped or selected. Action.ShowCard is not supported.",
    )
    style: Style = Field(None, description="Style hint for Container.")
    vertical_content_alignment: VerticalAlignment = Field(
        None,
        description="Defines how the content should be aligned "
        "vertically within the container. When not specified, the value of verticalContentAlignment is inherited from "
        "the parent container. If no parent container has verticalContentAlignment set, it defaults to Top.",
    )
    bleed: bool = Field(None, description="Determines whether the element should bleed through its parent's padding.")
    background_image: Union[BackgroundImage, str] = Field(
        None, description="Specifies the background image. Acceptable formats " "are PNG, JPEG, and GIF"
    )
    min_height: str = Field(None, description="Specifies the minimum height of the container in pixels, like '80px'.")
    rtl: bool = Field(
        False,
        description="When true content in this container should be presented right to left. "
        "When 'false' content in this container should be presented left to right. When unset layout direction will "
        "inherit from parent container or column. If unset in all ancestors, the default platform behavior "
        "will apply.",
    )


class Column(CamelModel):
    """Defines a container that is part of a ColumnSet."""

    id: str = Field(None, description="A unique identifier associated with the item.")
    is_visible: bool = Field(True, description="If false, this item will be removed from the visual tree.")
    requires: Dict[str, str] = Field(
        default_factory=dict,
        description="A series of key/value pairs indicating features that the item requires with corresponding "
        "minimum version. When a feature is missing or of insufficient version, fallback is triggered.",
    )
    items: List[ElementModel] = Field(
        default_factory=list, description="The card elements to render inside the Column."
    )
    background_image: Union[BackgroundImage, str] = Field(
        None, description="Specifies the background image. " "Acceptable formats are PNG, JPEG, and GIF"
    )
    bleed: bool = Field(None, description="Determines whether the column should bleed through its parent’s padding.")
    fallback: "Column" = Field(
        None,
        description="Describes what to do when an unknown item is encountered or the "
        "requires of this or any children can't be met.",
    )
    min_height: str = Field(None, description="Specifies the minimum height of the column in pixels, like '80px'.")
    rtl: bool = Field(
        False,
        description="When true content in this column should be presented right to left. When 'false' content in this "
        "column should be presented left to right. When unset layout direction will inherit from parent container or "
        "column. If unset in all ancestors, the default platform behavior will apply.",
    )
    separator: bool = Field(
        None, description="When true, draw a separating line between this column and the previous column."
    )
    spacing: Spacing = Field(
        None, description="Controls the amount of spacing between this column and the preceding column."
    )
    selectAction: SelectAction = Field(
        None,
        description="An Action that will be invoked when the Column is tapped or selected. "
        "Action.ShowCard is not supported.",
    )
    style: Style = Field(None, description="Style hint for Column.")
    vertical_content_alignment: VerticalAlignment = Field(
        None,
        description="Defines how the content should be aligned vertically within the column. When not specified, the "
        "value of verticalContentAlignment is inherited from the parent container. If no parent container has "
        "verticalContentAlignment set, it defaults to Top.",
    )
    width: Union[str, int] = Field(
        None,
        description="'auto', 'stretch', a number representing relative width of the column in the column group, or in "
        "version 1.1 and higher, a specific pixel width, like '50px'.",
    )


class ColumnSet(BaseContainers):
    """ColumnSet divides a region into Columns, allowing elements to sit side-by-side."""

    type: Literal["ColumnSet"] = Field("ColumnSet", description="Must be 'ColumnSet'.")
    columns: List[Column] = Field(default_factory=list, description="The array of Columns to divide the region into.")
    select_action: SelectAction = Field(
        None,
        description="An Action that will be invoked when the ColumnSet is tapped or selected. Action.ShowCard "
        "is not supported.",
    )
    style: Style = Field(None, description="Style hint for ColumnSet.")
    bleed: bool = Field(None, description="	Determines whether the element should bleed through its parent's padding.")
    min_height: str = Field(None, description="Specifies the minimum height of the column set in pixels, like '80px'.")
    horizontal_alignment: HorizontalAlignment = Field(
        None,
        description="Controls the horizontal alignment of the ColumnSet. When not specified, the value of "
        "horizontalAlignment is inherited from the parent container. If no parent container has horizontalAlignment "
        "set, it defaults to Left.",
    )


class TableColumnDefinition(BaseModel):
    width: str = Field("1", description="How wide should the column be, can be as column numbers or pixels.")


class TableCell(BaseContainers):
    """Represents a cell within a row of a Table element."""

    type: Literal["TableCell"] = Field("TableCell", description="Must be TableCell.")
    items: List[ElementModel] = Field(
        default_factory=list, description="The card elements to render inside the TableCell."
    )
    selectAction: SelectAction = Field(
        None,
        description="An Action that will be invoked when the TableCell is tapped or selected. Action.ShowCard "
        "is not supported.",
    )
    style: Style = Field(None, description="Style hint for TableCell.")
    verticalContentAlignment: VerticalAlignment = Field(
        None,
        description="Defines how the content should be aligned vertically within the container. When not specified, "
        "the value of verticalContentAlignment is inherited from the parent container. If no parent container has "
        "verticalContentAlignment set, it defaults to Top.",
    )
    bleed: bool = Field(None, description="Determines whether the element should bleed through its parent's padding.")
    background_image: BackgroundImage = Field(
        None, description="Specifies the background image. Acceptable formats are PNG, JPEG, and GIF"
    )
    min_height: str = Field(None, description=" 	Specifies the minimum height of the container in pixels, like '80px'.")
    rtl: bool = Field(
        False,
        description="When true content in this container should be presented right to left. When 'false' content in "
        "this container should be presented left to right. When unset layout direction will inherit from parent "
        "container or column. If unset in all ancestors, the default platform behavior will apply.",
    )


class TableRow(BaseModel):
    """"""

    type: Literal["TableRow"] = Field("TableRow", description="Must be TableRow.")
    cells: List[TableCell] = Field(default_factory=list, description="Collection of table cell configurations.")


class Table(BaseContainers):
    """Provides a way to display data in a tabular form."""

    type: Literal["Table"] = Field("Table", description="Must be Table.")
    columns: List[TableColumnDefinition] = Field(
        default_factory=list, description="Defines the number of columns in the table, their sizes, and more."
    )
    rows: List[TableRow] = Field(default_factory=list, description="Defines the rows of the table.")
    first_row_as_header: bool = Field(
        True,
        description="Specifies whether the first row of the table should be treated as a header row, and be announced "
        "as such by accessibility software.",
    )
    show_grid_lines: bool = Field(True, description="Specifies whether grid lines should be displayed.")
    grid_style: Style = Field(
        None, description="Defines the style of the grid. This property currently only controls the grid's color."
    )
    horizontal_cell_content_alignment: HorizontalAlignment = Field(
        None,
        description="Controls how the content of all cells is horizontally aligned by default. When not specified, "
        "horizontal alignment is defined on a per-cell basis.",
    )
    vertical_cell_content_alignment: VerticalAlignment = Field(
        None,
        description="Controls how the content of all cells is vertically aligned by default. When not specified, "
        "vertical alignment is defined on a per-cell basis.",
    )
