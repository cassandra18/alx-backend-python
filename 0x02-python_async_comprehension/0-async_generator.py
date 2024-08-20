"""0-async_generator.py"""
import asyncio
import random
from typing import AsyncGenerator

"""
This module defines an asynchronous generator coroutine that
yields random float numbers between 0 and 10, with a delay of 1 second
between each yield.
"""


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random float numbers
    between 0 and 10. Each number is yielded after a 1-second delay.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
