#!/usr/bin/env python3
"""This module contains a coroutine function
"""
import asyncio
from random import random


async def wait_random(max_delay=10):
    """
    Returns a random number after waiting for some time
    """

    wait_time = random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
