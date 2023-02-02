#!/usr/bin/python3
"""
Contains a function that returns the square
of it parameter
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a square of multiplier
    """
    def multiplier_function(value: float) -> float:
        return multiplier * value

    return multiplier_function
