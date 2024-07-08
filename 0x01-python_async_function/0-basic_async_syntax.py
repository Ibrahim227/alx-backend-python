#!/usr/bin/env python3
"""Import required module/lib"""
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """ takes in an integer argument and eventually  returns it."""
    delay = random.uniform(0, max_delay)
    return delay
