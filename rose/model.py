from __future__ import annotations
from rose.decorators import change_warn

from typing import Any, List, Literal, Optional


class File:
    def __init__(self, **file) -> None:
        self.__file = file

    @property
    def width(self) -> str:
        return self.__file["width"]

    @property
    def hash(self) -> str:
        return self.__file["hash"]

    @property
    def haswebp(self) -> str:
        return self.__file["haswebp"]

    @property
    def hasavifsmalltn(self) -> str:
        return self.__file["hasavifmallfn"]

    @property
    def name(self) -> str:
        return self.__file["name"]

    @property
    def height(self) -> str:
        return self.__file["height"]

    @property
    def hasavif(self) -> str:
        return self.__file["hasavif"]


class Tag:
    def __init__(self, **tag: Any) -> None:
        self.__tag = tag

    @property
    def value(self) -> str:
        return self.__tag["value"]

    @property
    def url(self) -> str:
        return self.__tag["url"]


class RawTag:
    def __init__(self, **raw_tag: Any) -> None:
        self.__raw_tag = raw_tag

    @property
    def male(self) -> Literal["", "1"]:
        return self.__raw_tag["male"]

    @property
    def female(self) -> Literal["", "1"]:
        return self.__raw_tag["female"]

    @property
    def tag(self) -> str:
        return self.__raw_tag["tag"]

    @property
    def url(self) -> str:
        return self.__raw_tag["url"]


class BaseHeliotrope:
    def __init__(self, **response) -> None:
        self.__response = response

    @property
    def status(self) -> Optional[int]:
        return self.__response.get("status")


class HeliotropeFile:
    def __init__(self, **file: Any) -> None:
        self.__file = file

    @property
    def name(self):
        return self.__file["name"]

    @property
    def image(self):
        return self.__file["image"]


class HeliotropeAbout(BaseHeliotrope):
    def __init__(self, **response: Any) -> None:
        super().__init__(**response)

    @property
    def last_checked_time(self) -> str:
        return self.__response["last_checked_time"]

    @property
    def last_mirrored_time(self) -> str:
        return self.__response["last_mirrored_time"]

    @property
    def new_time(self) -> str:
        return self.__response["new_time"]

    @property
    def server_status(self) -> str:
        return self.__response["server_status"]


class HeliotropeCount(BaseHeliotrope):
    def __init__(self, **response: Any) -> None:
        super().__init__(**response)

    @property
    def total(self) -> int:
        return self.__response["total"]

    @property
    @change_warn
    def list(self) -> List[dict[str, Any]]:
        return self.__response["list"]


    @property
    def thumbnail(self) -> str:
        return self.__thumbnail

    @property
    def artist(self) -> Iterator[HeliotropeValueData]:
        for artist_value in self.__artist:
            yield HeliotropeValueData(**artist_value)

    @property
    def group(self) -> Iterator[HeliotropeValueData]:
        for group_value in self.__group:
            yield HeliotropeValueData(**group_value)

    @property
    def type(self) -> HeliotropeValueData:
        return HeliotropeValueData(**self.__type)

    @property
    def language(self) -> HeliotropeValueData:
        return HeliotropeValueData(**self.__language)

    @property
    def series(self) -> Iterator[HeliotropeValueData]:
        for series_value in self.__series:
            yield HeliotropeValueData(**series_value)

    @property
    def characters(self) -> Iterator[HeliotropeValueData]:
        for character in self.__characters:
            yield HeliotropeValueData(**character)

    @property
    def tags(self) -> Iterator[HeliotropeValueData]:
        for tag in self.__tags:
            yield HeliotropeValueData(**tag)


class HeliotropeList:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status: int = data["status"]
        self.__list = data["list"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def status(self) -> int:
        return self.__status

    @property
    def list(self) -> Iterator[HeliotropeInfo]:
        for list_value in self.__list:
            yield HeliotropeInfo(**list_value)


class HeliotropeImages:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status = data["status"]
        self.__images = data["images"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def status(self) -> int:
        return self.__status

    @property
    def images(self) -> Iterator[HeliotropeImage]:
        for image in self.__images:
            yield HeliotropeImage(**image)


class HeliotropeRankingInfo:
    def __init__(self, **data: Any) -> None:
        self.__index = data["index"]
        self.__count = data["count"]

    @property
    def index(self) -> str:
        return self.__index

    @property
    def count(self) -> int:
        return self.__count


class HeliotropeRanking:
    def __init__(self, **data: Any) -> None:
        self.__count = data["total"]
        self.__list = data["list"]
        self.__month = data["month"]

    @property
    def count(self) -> int:
        return self.__count

    @property
    def ranking(self) -> HeliotropeRankingInfo:
        for info in self.__list:
            yield HeliotropeRankingInfo(**info)

    @property
    def month(self) -> int:
        return self.__month
