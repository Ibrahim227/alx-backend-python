#!/usr/bin/env python3
"""Import required module/lib"""
import asyncio
import time
from random import uniform
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """should measure the total runtime and return it."""
    start = time()
    async_exe = [async_comprehension() for i in range(4)]
    result = await asyncio.gather(*async_exe)
    end = time()

    return end - start
