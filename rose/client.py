from __future__ import annotations

from typing import Any, Optional

import aiohttp

from rose.model import (
    HeliotropeGalleryInfo,
    HeliotropeImages,
    HeliotropeInfo,
    HeliotropeIntegrated,
    HeliotropeList,
)


class Client:
    def __init__(self, authorization: str):
        self.authorization = authorization

    async def request(
        self, method: str, path: str, json: Optional[dict[str, Any]] = None
    ) -> Any:
        headers = {"Authorization": self.authorization}
        url = "https://doujinshiman.ga/" + "v3" + path
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

    async def integrated(self, index: int) -> HeliotropeIntegrated:
        return HeliotropeIntegrated(
            **await self.request("GET", f"/api/hitomi/integrated/{index}")
        )

    async def list_(self, number: int) -> HeliotropeList:
        return HeliotropeList(**await self.request("GET", f"/api/hitomi/list/{number}"))

    async def index(self) -> list[int]:
        return await self.request("GET", f"/api/hitomi/index")

    async def images(self, index: int) -> HeliotropeImages:
        return HeliotropeImages(
            **await self.request("GET", f"/api/hitomi/images/{index}")
        )
