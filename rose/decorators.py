from typing import Any, Callable, TypeVar, cast
from functools import wraps
from warnings import warn

CA = TypeVar("CA", bound=Callable[..., Any])


def change_warn(f: CA) -> CA:
    @wraps(f)
    def wrapper(self: Any, *args: Any, **kwargs: Any):
        warn("Will change in Heliotrope 4.1.0")
        return f(self, *args, **kwargs)

    return cast(CA, wrapper)
