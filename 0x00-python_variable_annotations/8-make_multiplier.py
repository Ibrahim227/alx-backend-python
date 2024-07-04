#!/usr/bin/env python3
"""Import module/lib"""
from typing import Callable


def make_multiplier(multiplier: float) -> float:
    """returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """multiples the float by multiplier"""
        return n * multiplier
    return multiply
