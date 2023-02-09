#!/usr/bin/env python3
"""
Contains an async generator that loops 10 time sleeps
for 1 second in each iteration and yeilds a value in
each iteration.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    Loops for 10 times and yeilds a random value
    after 1 a second in each iteration
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
