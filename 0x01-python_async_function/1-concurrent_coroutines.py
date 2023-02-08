#!usr/bin/env python3
"""
This module spawns multiple coroutines at the same time
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """Spawns wait_random n multiple times"""
    return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
