"""1-async_comprehension.py"""
from typing import List
async_generator = __import__('0-async_generator').async_generator

"""
This module defines an asynchronous coroutine that collects 10 random
numbers generated by async_generator and returns them as a list.
"""


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random float numbers generated by the
    async_generator using asynchronous comprehension.

    Returns:
        List[float]: A list containing 10 random float numbers.
    """
    return [number async for number in async_generator()]
