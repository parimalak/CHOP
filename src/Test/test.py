# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:27:47 2017

@author: Parimala Killada
"""

import unittest
from coding_Exercise import flatten_list,serialize_tree,deserialize_tree

class flatten_list_TestCase(unittest.TestCase):
    """Tests for `flatten_list`."""

    def test_is_flatten_list1(self):
        """"""
        self.assertEqual(flatten_list([2,[[3,[4,6]], 5]]),[2,3,4,6,5])
        self.assertEqual(flatten_list([]),[])
    
    def test_is_serialize_tree(self):
        self.assertEqual(serialize_tree(deserialize_tree([1,2,3,None,4,2,None])),[1,2,3,None,4,2,None])
        self.assertEqual(serialize_tree(deserialize_tree(([]),[])))
 
if __name__ == '__main__':
    unittest.main()
