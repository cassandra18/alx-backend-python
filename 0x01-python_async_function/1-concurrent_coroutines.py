#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay
    returns the list of delays in ascending order."""
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []

    for task in asyncio.as_completed(delays):
        result = await task
        completed_delays.append(result)

    return completed_delays
