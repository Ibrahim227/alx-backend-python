#!/usr/bin/env python3
"""Import Module/Lib"""
import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    """class TestAccessNestedMap inherits from unittest.TestCase"""
    @parameterized.expand([])

    def test_access_nested_map(self):
        """method to test that the method returns what it is supposed to"""
        result = utils.access_nested_map(
