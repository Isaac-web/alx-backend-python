#!/usr/bin/env python3
"""
This module contains a function that returns
an tuple of strings and numbers
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
    Returns the arguments k and v in a tuple
    """
    return k, v**2
