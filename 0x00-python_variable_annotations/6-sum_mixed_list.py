#!/usr/bin/env python3
"""
This module contains a function that
returns a the sum of elemens of a list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the list as a float
    """
    return sum(mxd_lst)
