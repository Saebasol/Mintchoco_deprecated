from __future__ import annotations

from typing import Any, Optional
from types import TracebackType

from aiohttp.client import ClientSession
from mintchoco.model import (
    BaseHeliotrope,
    HeliotropeAbout,
    HeliotropeCount,
    HeliotropeGalleryInfo,
    HeliotropeImages,
    HeliotropeInfo,
    HeliotropeList,
    HeliotropeSearch,
)

BASE_URL = "https://heliotrope.me/"
API_VERSION = "v4"

API_URL = BASE_URL + API_VERSION


class Client:
    def __init__(
        self,
        hiyobot: Optional[str] = None,
        client_session: Optional[ClientSession] = None,
    ) -> None:
        self.hiyobot = hiyobot
        self.client_session = client_session

    async def request(
        self, method: str, path: str, json: Optional[dict[str, Any]] = None
    ) -> Any:
        url = BASE_URL + path
        if "api" in path:
            url = API_URL + path

        if not self.client_session:
            self.client_session = ClientSession()

        if self.hiyobot:
            self.client_session.headers.update({"hiyobot": self.hiyobot})

        async with self.client_session.request(method, url, json=json) as r:
            return await r.json()

    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.client_session:
            await self.client_session.close()

    async def about(self) -> HeliotropeAbout:
        return HeliotropeAbout(**await self.request("GET", "about?json=true"))

    async def post_count(self, index: int) -> BaseHeliotrope | HeliotropeCount:
        return BaseHeliotrope(
            **await self.request("POST", "/api/count", {"index": index})
        )

    async def get_count(self) -> HeliotropeCount:
        return HeliotropeCount(**await self.request("GET", "/api/count"))

    async def galleryinfo(self, index: int) -> HeliotropeGalleryInfo:
        return HeliotropeGalleryInfo(
            **await self.request("GET", f"/api/hitomi/galleryinfo/{index}")
        )

    async def images(self, index: int) -> HeliotropeImages:
        return HeliotropeImages(
            **await self.request("GET", f"/api/hitomi/images/{index}")
        )

    async def info(self, index: int) -> HeliotropeInfo:
        return HeliotropeInfo(**await self.request("GET", f"/api/hitomi/info/{index}"))

    async def list(self, number: int) -> HeliotropeList:
        return HeliotropeList(**await self.request("GET", f"/api/hitomi/list/{number}"))

    async def search(self, query: str, offset: int = 0) -> HeliotropeSearch:
        return HeliotropeSearch(
            **await self.request("GET", f"/api/hitomi/search?q={query}&offset={offset}")
        )
