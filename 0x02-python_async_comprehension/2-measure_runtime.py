#!/usr/bin/env python3
"""Import required module/lib"""
import asyncio
from random import uniform
from typing import Generator, List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """should measure the total runtime and return it."""
    
