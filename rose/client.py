import asyncio
import functools
from typing import Any

import aiohttp

from .model import GalleryInfo, Index, Info, Integrated, List_, Images


class _Client:
    def __init__(self, authorization):
        self.authorization = authorization

    async def request(self, method, endpoint, json=None):
        headers = {"Authorization": self.authorization}
        url = "https://doujinshiman.ga/" + "v3" + endpoint
        async with aiohttp.ClientSession() as cs:
            async with cs.request(method, url, headers=headers, json=json) as r:
                response = await r.json()
                return response

    async def galleryinfo(self, index: int):
        response = await self.request("GET", f"/api/hitomi/galleryinfo/{index}")
        return GalleryInfo(response)

    async def info(self, index: int):
        response = await self.request("GET", f"/api/hitomi/info/{index}")
        return Info(response)

    async def integrated(self, index: int):
        response = await self.request("GET", f"/api/hitomi/integrated/{index}")
        return Integrated(response)

    async def list_(self, number: int):
        response = await self.request("GET", f"/api/hitomi/list/{number}")
        return List_(response)

    async def index(self):
        response = await self.request("GET", f"/api/hitomi/index")
        return Index(response)

    async def images(self, index: int):
        response = await self.request("GET", f"/api/hitomi/images/{index}")
        return Images(response)


class Client(_Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str) -> Any:
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
