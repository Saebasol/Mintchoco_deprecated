from __future__ import annotations

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

    @classmethod
    def to_tag(cls, list_element: list[dict[str, Any]]):
        return list(map(lambda tag: cls(**tag), list_element))


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


class Count:
    def __init__(self, **count) -> None:
        self._count = count

    @property
    def index(self) -> int:
        return self._count["index"]

    @property
    def title(self) -> str:
        return self._count["title"]

    @property
    def count(self) -> int:
        return self._count["count"]


class BaseHeliotrope:
    def __init__(self, **response) -> None:
        self._response = response

    @property
    def status(self) -> Optional[int]:
        return self._response.get("status")


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
        return self._response["last_checked_time"]

    @property
    def last_mirrored_time(self) -> str:
        return self._response["last_mirrored_time"]

    @property
    def new_item(self) -> str:
        return self._response["new_item"]

    @property
    def server_status(self) -> str:
        return self._response["server_status"]


class HeliotropeCount(BaseHeliotrope):
    def __init__(self, **response: Any) -> None:
        super().__init__(**response)

    @property
    def total(self) -> int:
        return self._response["total"]

    @property
    def list(self):
        return list(map(lambda count: Count(**count), self._response["list"]))


class HeliotropeGalleryInfo(BaseHeliotrope):
    def __init__(self, is_raw: bool = False, **response: Any) -> None:
        self.is_raw = is_raw
        super().__init__(**response)

    @property
    def language_localname(self) -> str:
        return self._response["language_localname"]

    @property
    def language(self) -> str:
        return self._response["language"]

    @property
    def date(self) -> str:
        return self._response["date"]

    @property
    def files(self) -> list[Optional[File]]:
        return list(map(lambda file: File(**file), self._response["files"]))

    @property
    def tags(self) -> list[Tag] | list[RawTag]:
        if self.is_raw:
            return list(map(lambda tag: RawTag(**tag), self._response["tags"]))

        return Tag.to_tag(self._response["tags"])

    @property
    def japanese_title(self) -> Optional[str]:
        return self._response["japanese_title"]

    @property
    def title(self) -> str:
        return self._response["title"]

    @property
    def id(self) -> str:
        return self._response["id"]

    @property
    def type(self) -> str:
        return self._response["type"]


class HeliotropeImages(BaseHeliotrope):
    def __init__(self, **response: Any) -> None:
        super().__init__(**response)

    @property
    def files(self):
        return list(map(lambda file: HeliotropeFile(**file), self._response["files"]))


class HeliotropeInfo(BaseHeliotrope):
    def __init__(self, **response: Any) -> None:
        super().__init__(**response)

    @property
    def index(self):
        return self._response.get("index")

    @property
    def title(self):
        return self._response["title"]

    @property
    def thumbnail(self):
        return self._response["thumbnail"]

    @property
    def artist(self):
        return Tag.to_tag(self._response["artist"])

    @property
    def group(self):
        return Tag.to_tag(self._response["group"])

    @property
    def type(self):
        return Tag(**self._response["type"])

    @property
    def language(self):
        return Tag(**self._response["language"])

    @property
    def series(self):
        return Tag.to_tag(self._response["series"])

    @property
    def characters(self):
        return Tag.to_tag(self._response["characters"])

    @property
    def tags(self):
        return Tag.to_tag(self._response["tags"])


class HeliotropeSearch(BaseHeliotrope):
    def __init__(self, **response) -> None:
        super().__init__(**response)

    @property
    def result(self):
        return list(
            map(lambda result: HeliotropeInfo(**result), self._response["result"])
        )

    @property
    def count(self):
        return self._response["count"]


class HeliotropeList(BaseHeliotrope):
    def __init__(self, **response) -> None:
        super().__init__(**response)

    @property
    def list(self):
        return list(map(lambda info: HeliotropeInfo(**info), self._response["list"]))
