from __future__ import annotations

from typing import Any, Iterator, Optional


class HeliotropeFile:
    def __init__(self, **file: Any):
        self.to_dict = file
        self.width: str = file["width"]
        self.hash: str = file["hash"]
        self.haswebp: Optional[bool] = bool(file["haswebp"])
        self.hasavifsmalltn: Optional[bool] = bool(file["hasavifsmalltn"])
        self.name: str = file["name"]
        self.height: str = file["height"]
        self.hasavif: Optional[bool] = bool(file["hasavif"])

    @classmethod
    def parsing(
        cls, value_datas: dict[str, list[dict[str, str]]], key: str
    ) -> Iterator[HeliotropeFile]:
        for value_data in value_datas[key]:
            yield cls(**value_data)


class HeliotropeValueData:
    def __init__(self, **tag: Any) -> None:
        self.to_dict = tag
        self.value = tag["value"]
        self.tag = tag["tag"]

    @classmethod
    def parsing(
        cls, value_datas: dict[str, list[dict[str, str]]], key: str
    ) -> Iterator[HeliotropeValueData]:
        for value_data in value_datas[key]:
            yield cls(**value_data)


class HeliotropeImage:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.url: str = data["url"]
        self.filename: str = data["filename"]

    @classmethod
    def parsing(
        cls, value_datas: dict[str, list[dict[str, str]]], key: str
    ) -> Iterator[HeliotropeImage]:
        for value_data in value_datas[key]:
            yield cls(**value_data)


class HeliotropeGalleryInfo:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.status: int = data["status"]
        self.language_localname: str = data["language_localname"]
        self.language: str = data["language"]
        self.date: str = data["date"]
        self.files = HeliotropeFile.parsing(data, "files")
        self.tags = HeliotropeValueData.parsing(data, "tags")
        self.japanese_title: str = data["japanese_title"]
        self.title: str = data["title"]
        self.id: str = data["id"]
        self.type: str = data["type"]


class HeliotropeInfo:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.status: int = data["status"]
        self.title = HeliotropeValueData.parsing(data, "title")
        self.galleyid = data["galleryid"]
        self.artist = HeliotropeValueData.parsing(data, "artist")
        self.group = HeliotropeValueData.parsing(data, "group")
        self.type = HeliotropeValueData.parsing(data, "type")
        self.language = HeliotropeValueData.parsing(data, "language")
        self.series = HeliotropeValueData.parsing(data, "series")
        self.characters = HeliotropeValueData.parsing(data, "characters")
        self.tags = HeliotropeValueData.parsing(data, "tags")


class HeliotropeIntegrated:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.data: tuple[
            Optional[HeliotropeGalleryInfo], Optional[HeliotropeInfo]
        ] = tuple(data["data"])


class HeliotropeList:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.status: int = data["status"]
        self.list: list[HeliotropeInfo] = data["list"]


class HeliotropeImages:
    def __init__(self, **data: Any) -> None:
        self.to_dict = data
        self.status: int = data["status"]
        self.images = HeliotropeImage.parsing(data, "images")
