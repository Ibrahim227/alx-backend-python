#!/usr/bin/env python3
"""IMport required module/lib"""
import asyncio
import random
from typing import Generator


async_comprehension = __import__('0-async_generator').async_generator

async def async_comprehension() -> Generator[float, None, None]:
    """return the 10 random numbers."""
    for i in range(10):
        yield 1
        await async_generator()
        random.uniform(0, 10)
