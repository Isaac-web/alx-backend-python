#!/bin/usr/env python3
"""
This module spawns multiple coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n multiple times"""
    return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
