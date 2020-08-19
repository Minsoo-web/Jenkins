from typing import Any
import os


def isfile(path: str) -> bool:
    return os.path.isfile(path=path)


def isdir(path: str) -> bool:
    return os.path.isdir(path=path)


def equals(obj_1: Any, obj_2: Any, *, deep=False):
    if deep:
        return obj_1 is obj_2
    return obj_1 == obj_2
