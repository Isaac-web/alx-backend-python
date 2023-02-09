#!/usr/bin/env python3
"""
Contains an async generator that loops 10 time sleeps
for 1 second in each iteration and yeilds a value in
each iteration.
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Returns the values gotten from async_generator in a list
    """
    return [x async for x in async_generator()]
