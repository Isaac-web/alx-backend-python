#!/usr/bin/env python3
"""
This module create a coroutine.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay):
    """
    Returns a coroutine.
    Args:
        max_delay: (int) the number of seconds to be delayed.
    """
    return asyncio.Task(wait_random(max_delay))
