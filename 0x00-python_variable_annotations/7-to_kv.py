#!/usr/bin/env python3i
"""defines afunction that retuns a tuple of string a number"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """returns a tuple. The first element of the tuple is the string k.
    The second element is the square
    of the int/float v and should be
    annotated as a float.
    """

    return (k, v * v)
