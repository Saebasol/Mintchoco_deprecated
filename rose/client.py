from __future__ import annotations

from typing import Any, Optional

import aiohttp

from rose.model import (
    HeliotropeAbout,
    HeliotropeCount,
    HeliotropeGalleryInfo,
    HeliotropeImages,
    HeliotropeInfo,
    HeliotropeList,
)


class Client:
    def __init__(self, headers: dict = None) -> None:
        self.headers = headers

    async def request(
        self, method: str, path: str, json: Optional[dict[str, Any]] = None
    ) -> Any:
        url = "https://doujinshiman.ga/" + "v4" + path
        async with aiohttp.ClientSession(headers=self.headers) as cs:
            async with cs.request(method, url, json=json) as r:
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

    async def images(self, index: int) -> HeliotropeImages:
        return HeliotropeImages(
            **await self.request("GET", f"/api/hitomi/images/{index}")
        )

    async def count(self) -> HeliotropeCount:
        return HeliotropeCount(**await self.request("GET", "/api/count"))

    async def about(self) -> HeliotropeAbout:
        return HeliotropeAbout(**await self.request("GET", "/about?json=True"))
