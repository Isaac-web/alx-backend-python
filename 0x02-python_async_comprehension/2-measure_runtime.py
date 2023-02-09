#!/usr/bin/env python
"""
This module measures the time taken by a set
of asynchronous coroutines
"""
import asyncio
from time import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Returns the time taken to measure the execution
    of four async_comprehension calls.
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return end - start
