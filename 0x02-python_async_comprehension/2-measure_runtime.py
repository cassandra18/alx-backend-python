"""2-measure_runtime.py"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
This module defines a coroutine that measures the runtime of executing
the async_comprehension coroutine four times in parallel.
"""


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing the
    async_comprehension coroutine four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()

    return end_time - start_time
