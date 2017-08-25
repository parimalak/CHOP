# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:27:47 2017

@author: Parimala Killada
"""

import unittest
from coding_Exercise import flatten_list

class flatten_list_TestCase(unittest.TestCase):
    """Tests for `flatten_list`."""

    def test_is_flatten_list1(self):
        """"""
        self.assertTrue(flatten_list([2,[[3,[4]], 5]]))

if __name__ == '__main__':
    unittest.main()