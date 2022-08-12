"""
"""
from typing import List, Literal

import httpx
from pydantic import Field

from .base import CamelModel
from .cards import AdaptiveCard


class Card(CamelModel):
    """"""

    content_type: str = Field(
        "application/vnd.microsoft.card.adaptive", description="Field must be set to Adaptive " "Card type."
    )
    content_url: str = Field(None, description="")
    content: AdaptiveCard = Field(None, description="Card object to send")


class MessageModel(CamelModel):
    """"""

    type: Literal["message"] = Field("message", description="Must be message.")
    attachments: List[Card] = Field(default_factory=list, description="Array contains a set of card objects.")


class Client:
    def __init__(self, url) -> None:
        self._url = url
        self._message = MessageModel()

    def create_adaptive_card(self) -> AdaptiveCard:
        card = Card()
        card.content = AdaptiveCard()

        return card.content

    def post(self) -> httpx.Response:
        """Post the card to the given webhook url"""
        return httpx.post(self._url, data=self._message.dict())

    async def post_async(self) -> httpx.Response:
        """Post the card to the given webhook url"""
        async with httpx.AsyncClient() as client:
            return await client.post(self._url, data=self._message.dict())
