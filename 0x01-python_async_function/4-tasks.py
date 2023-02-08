#!/usr/bin/env python3
"""
Module on asyncio in python
"""
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """Spawns wait_random n multiple times"""
    return await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
