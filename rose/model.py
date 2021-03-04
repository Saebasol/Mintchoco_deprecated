from __future__ import annotations

from typing import Any, Iterator, Optional


class HeliotropeFile:
    def __init__(self, **file: Any) -> None:
        self.__file = file
        self.__width = file["width"]
        self.__hash = file["hash"]
        self.__haswebp = file["haswebp"]
        self.__hasavifsmalltn = file["hasavifsmalltn"]
        self.__name = file["name"]
        self.__height = file["height"]
        self.__hasavif = file["hasavif"]

    def to_dict(self) -> dict[str, Any]:
        return self.__file

    @property
    def width(self) -> str:
        return self.__width

    @property
    def hash(self) -> str:
        return self.__hash

    @property
    def haswebp(self) -> Optional[bool]:
        return bool(self.__haswebp)

    @property
    def hasavifsmalltn(self) -> Optional[bool]:
        return bool(self.__hasavifsmalltn)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> str:
        return self.__height

    @property
    def hasavif(self) -> Optional[bool]:
        return bool(self.__hasavif)

    @classmethod
    def parsing_generator(
        cls, value_datas: dict[str, list[dict[str, str]]], key: str
    ) -> Iterator[HeliotropeFile]:
        for value_data in value_datas[key]:
            yield cls(**value_data)


class HeliotropeValueData:
    def __init__(self, **tag: Any) -> None:
        self.__tag = tag
        self.__value = tag["value"]
        self.__url = tag["url"]

    def to_dict(self) -> dict[str, Any]:
        return self.__tag

    @property
    def value(self) -> str:
        return self.__value

    @property
    def url(self) -> str:
        return self.__url


class HeliotropeImage:
    def __init__(self, **image: Any) -> None:
        self.__image = image
        self.__url = image["url"]
        self.__filename = image["filename"]

    def to_dict(self) -> dict[str, Any]:
        return self.__image

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def url(self) -> str:
        return self.__url


class HeliotropeGalleryInfo:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status = data["status"]
        self.__language_localname = data["language_localname"]
        self.__language = data["language"]
        self.__date = data["date"]
        self.__files = data["files"]
        self.__tags = data["tags"]
        self.__japanese_title = data["japanese_title"]
        self.__title = data["title"]
        self.__id = data["id"]
        self.__type = data["type"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def status(self) -> int:
        return self.__status

    @property
    def language_localname(self) -> str:
        return self.__language_localname

    @property
    def language(self) -> str:
        return self.__language

    @property
    def date(self) -> str:
        return self.__date

    @property
    def files(self) -> Iterator[HeliotropeFile]:
        for file in self.__files:
            yield HeliotropeFile(**file)

    @property
    def tags(self) -> Iterator[HeliotropeValueData]:
        for tag in self.__tags:
            yield HeliotropeValueData(**tag)

    @property
    def japanese_title(self) -> Optional[str]:
        return self.__japanese_title

    @property
    def title(self) -> str:
        return self.__title

    @property
    def id(self) -> str:
        return self.__id

    @property
    def type(self) -> str:
        return self.__type


class HeliotropeInfo:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status = data["status"]
        self.__title = data["title"]
        self.__galleryid = data["galleryid"]
        self.__thumbnail = data["thumbnail"]
        self.__artist = data["artist"]
        self.__group = data["group"]
        self.__type = data["type"]
        self.__language = data["language"]
        self.__series = data["series"]
        self.__characters = data["characters"]
        self.__tags = data["tags"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def status(self) -> int:
        return self.__status

    @property
    def title(self) -> HeliotropeValueData:
        return HeliotropeValueData(**self.__title)

    @property
    def galleryid(self) -> str:
        return self.__galleryid

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
