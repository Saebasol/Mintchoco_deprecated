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
    def width(self) -> int:
        return self.__width

    @property
    def hash(self) -> str:
        return self.__hash

    @property
    def haswebp(self) -> int:
        return bool(self.__haswebp)

    @property
    def hasavifsmalltn(self) -> int:
        return bool(self.__hasavifsmalltn)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> int:
        return self.__height

    @property
    def hasavif(self) -> int:
        return bool(self.__hasavif)

    @classmethod
    def parsing_generator(
        cls, value_datas: dict[str, list[dict[str, str]]], key: str
    ) -> Iterator[HeliotropeFile]:
        for value_data in value_datas[key]:
            yield cls(**value_data)


class HeliotropeTagData:
    def __init__(self, **tags: Any) -> None:
        self.__tags = tags
        self.__male = tags["male"]
        self.__female = tags["female"]
        self.__tag = tags["tag"]
        self.__url = tags["url"]

    def to_dict(self) -> dict[str, Any]:
        return self.__tags

    @property
    def male(self) -> str:
        return self.__male

    @property
    def female(self) -> str:
        return self.__female

    @property
    def tag(self) -> str:
        return self.__tag

    @property
    def url(self) -> str:
        return self.__url


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
        self.__data = image
        self.__name = image["name"]
        self.__image = image["image"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def name(self) -> str:
        return self.__name

    @property
    def image(self) -> str:
        return self.__image


class HeliotropeGalleryInfo:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status = data["status"]
        self.__id = data["id"]
        self.__language = data["language"]
        self.__language_localname = data["language_localname"]
        self.__date = data["date"]
        self.__files = data["files"]
        self.__tags = data["tags"]
        self.__japanese_title = data["japanese_title"]
        self.__title = data["title"]
        self.__type = data["type"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def status(self) -> int:
        return self.__status

    @property
    def id(self) -> str:
        return self.__id

    @property
    def language(self) -> str:
        return self.__language

    @property
    def language_localname(self) -> str:
        return self.__language_localname

    @property
    def date(self) -> str:
        return self.__date

    @property
    def files(self) -> Iterator[HeliotropeFile]:
        for file in self.__files:
            yield HeliotropeFile(**file)

    @property
    def tags(self) -> Iterator[HeliotropeTagData]:
        for tags in self.__tags:
            yield HeliotropeTagData(**tags)

    @property
    def japanese_title(self) -> Optional[str]:
        return self.__japanese_title

    @property
    def title(self) -> str:
        return self.__title

    @property
    def type(self) -> str:
        return self.__type


class HeliotropeInfo:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__title = data["title"]
        self.__thumbnail = data["thumbnail"]
        self.__artist = data["artist"]
        self.__group = data["group"]
        self.__type = data["type"]
        self.__language = data["language"]
        self.__series = data["series"]
        self.__characters = data["characters"]
        self.__tags = data["tags"]
        self.__status = data.get("status")

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def title(self) -> str:
        return self.__title

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
        for character_value in self.__characters:
            yield HeliotropeValueData(**character_value)

    @property
    def tags(self) -> Iterator[HeliotropeValueData]:
        for tag_value in self.__tags:
            yield HeliotropeValueData(**tag_value)

    @property
    def status(self) -> int:
        return self.__status


class HeliotropeList:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__status = data["status"]
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
        self.__files = data["files"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def files(self) -> Iterator[HeliotropeImage]:
        for file in self.__files:
            yield HeliotropeImage(**file)


class HeliotropeCountInfo:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__index = data["index"]
        self.__title = data["title"]
        self.__count = data["count"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def index(self) -> str:
        return self.__index

    @property
    def title(self) -> str:
        return self.__title

    @property
    def count(self) -> int:
        return self.__count


class HeliotropeCount:
    def __init__(self, **data: Any) -> None:
        self.__data = data
        self.__total = data.get("total")
        self.__list = data.get("list")
        self.__message = data.get("message")
        self.__status = data["status"]

    def to_dict(self) -> dict[str, Any]:
        return self.__data

    @property
    def total(self) -> int:
        return self.__total

    @property
    def ranking(self) -> Iterator[HeliotropeCountInfo]:
        for info in self.__list:
            yield HeliotropeCountInfo(**info)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def status(self) -> int:
        return self.__status
