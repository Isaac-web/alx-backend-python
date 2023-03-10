#!/usr/bin/env python3
"""
This module spawns multiple coroutines at the same time
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n multiple times"""
    items = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]

    return items
