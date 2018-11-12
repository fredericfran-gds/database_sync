#!/usr/bin/env python

"""
This module defines the test cases for the Config class

"""

import unittest
from .config import Config


class TestConfigClass(unittest.TestCase):
    """
    This class tests the Config class

    """

    def test_init(self):
        """
        This function test that the class Config can be initialized

        """
        try:
            _ = Config()
        except ValueError as err:
            self.fail("error raised unexpectedly when config object created: {}".format(err))


if __name__ == "__main__":
    unittest.main()
