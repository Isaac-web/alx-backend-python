#!/usr/bin/env python3
"""
This module measures the time async function calls
"""
from time import time
import asyncio
from datetime import datetime
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    return (end - start)/n
