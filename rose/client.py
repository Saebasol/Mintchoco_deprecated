from __future__ import annotations
from rose.model import HeliotropeGalleryInfo, HeliotropeInfo

from typing import Any, Optional

import aiohttp

BASE_URL = "https://beta.doujinshiman.ga/"
API_VERSION = "v4"


class Client:
    def __init__(self, hiyobot: str):
        self.hiyobot = hiyobot

    async def request(
        self, method: str, path: str, json: Optional[dict[str, Any]] = None
    ) -> Any:
        headers = {"hiyobot": self.hiyobot}
        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, url, headers=headers, json=json) as r:
                response = await r.json()
                return response

    async def galleryinfo(self, index: int) -> HeliotropeGalleryInfo:
        return HeliotropeGalleryInfo(
            **await self.request("GET", f"/api/hitomi/galleryinfo/{index}")
        )

    async def info(self, index: int) -> HeliotropeInfo:
        return HeliotropeInfo(**await self.request("GET", f"/api/hitomi/info/{index}"))

    async def list_(self, number: int) -> HeliotropeList:
        return HeliotropeList(**await self.request("GET", f"/api/hitomi/list/{number}"))

    async def index(self) -> list[int]:
        return await self.request("GET", f"/api/hitomi/index")

    async def images(self, index: int) -> HeliotropeImages:
        return HeliotropeImages(
            **await self.request("GET", f"/api/hitomi/images/{index}")
        )

    async def ranking(self) -> HeliotropeRanking:
        return HeliotropeRanking(**await self.request("GET", "/api/ranking"))
