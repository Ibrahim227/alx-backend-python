#!/usr/bin/env python3
"""Import required module/lib"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield a random number between 0 and 10."""
    for i in range(10):
        yield i
        await asyncio.sleep(1)
        random.uniform(0, 10)
