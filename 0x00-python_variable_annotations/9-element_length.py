#!/usr/bin/env python3
"""
Contains an anotatted function
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list"""
    return [(i, len(i)) for i in lst]
