#!/usr/bin/env python3
"""IMport required module/lib"""
import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> Generator[float, None, None]:
    """return the 10 random numbers."""
    return [i async for i in async_generator()]
