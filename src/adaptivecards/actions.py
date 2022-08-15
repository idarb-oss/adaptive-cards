"""
"""
from typing import Literal, Union

from pydantic import Field

from .base import AssociatedInputs, SelectAction


class OpenUrl(SelectAction):
    """
    When invoked, show the given url either by launching it in an external web browser or showing within an
    embedded web browser.
    """

    type: Literal["Action.OpenUrl"] = Field("Action.OpenUrl", description="Must be 'Action.OpenUrl'.")
    url: str = Field(..., description="The URL to open.")


class Submit(SelectAction):
    """
    Gathers input fields, merges with optional data field, and sends an event to the client. It is up to the client to
    determine how this data is processed. For example: With BotFramework bots, the client would send an activity
    through the messaging medium to the bot. The inputs that are gathered are those on the current card, and in the
    case of a show card those on any parent cards.

    See https://docs.microsoft.com/en-us/adaptive-cards/authoring-cards/input-validation for more details.
    """

    type: Literal["Action.Submit"] = Field("Action.Submit", description="Must be 'Action.Submit'.")
    data: Union[str, dict] = Field(
        None,
        description="Initial data that input fields will be combined with. "
        "These are essentially 'hidden' properties.",
    )
    associated_inputs: AssociatedInputs = Field(
        None, description="Controls which inputs are associated with the " "submit action."
    )
