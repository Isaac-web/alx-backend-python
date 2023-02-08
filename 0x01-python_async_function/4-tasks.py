#!/usr/bin/env python3
"""
Module on asyncio in python
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n multiple times"""
    items = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))

    items.sort()
    return items
