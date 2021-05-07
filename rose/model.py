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


class HeliotropeGalleryInfo(BaseHeliotrope):
    def __init__(self, is_raw: bool = False, **response: Any) -> None:
        self.is_raw = is_raw
        super().__init__(**response)

    @property
    def language_localname(self) -> str:
        return self.__response["language_localname"]

    @property
    def language(self) -> str:
        return self.__response["language"]

    @property
    def date(self) -> str:
        return self.__response["date"]

    @property
    def files(self) -> list[Optional[File]]:
        return list(map(lambda file: File(**file), self.__response["files"]))

    @property
    def tags(self) -> list[Optional[Tag | RawTag]]:
        if self.is_raw:
            return list(map(lambda tag: RawTag(**tag), self.__response["tags"]))

        return list(map(lambda tag: Tag(**tag), self.__response["tags"]))

    @property
    def japanese_title(self) -> Optional[str]:
        return self.__response["japanese_title"]

    @property
    def title(self) -> str:
        return self.__response["title"]

    @property
    def id(self) -> str:
        return self.__response["id"]

    @property
    def type(self) -> str:
        return self.__response["type"]



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
