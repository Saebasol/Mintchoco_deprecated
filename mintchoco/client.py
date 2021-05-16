from __future__ import annotations

from typing import Any, Optional

import aiohttp
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

BASE_URL = "https://beta.doujinshiman.ga/"
API_VERSION = "v4"

API_URL = BASE_URL + API_VERSION


class Client:
    def __init__(self, hiyobot: str):
        self.hiyobot = hiyobot

    async def request(
        self, method: str, path: str, json: Optional[dict[str, Any]] = None
    ) -> Any:
        headers = {"hiyobot": self.hiyobot}
        url = BASE_URL + path
        if "api" in path:
            url = API_URL + path
        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, url, headers=headers, json=json) as r:
                return await r.json()

    async def about(self) -> HeliotropeAbout:
        return HeliotropeAbout(**await self.request("GET", "about?json=true"))

    async def count(
        self, index: Optional[int] = None
    ) -> BaseHeliotrope | HeliotropeCount:
        if index:
            return BaseHeliotrope(
                **await self.request("POST", "/api/count", {"index": index})
            )
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

    async def search(self, query: str, offset=0) -> HeliotropeSearch:
        return HeliotropeSearch(
            **await self.request(
                "POST", f"/api/hitomi/search?q={query}&offset={offset}"
            )
        )
