#!/usr/bin/env python3
"""defines a function that returns the sum of the input list as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list as float"""

    return sum(mxd_lst)
