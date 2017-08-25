# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:07:35 2017

@author: Parimala Killada
"""

##Coding_Exercise1
##Flatten Nested List


from collections import Iterable
def flatten_list(nested_list):
    
    """
    Flatten an arbitrarily nested list

    Parameters
    ----------
    nested_list : nested list of int
        List with item to be either integers or list
        Example: [2,[[3,[4]], 5]]

    Returns
    -------
    flat_list : list of int
        A flattened list with only integers
        Example: [2,3,4,5]
    """
    for x in nested_list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten_list(x)
        else:
            yield x

#Coding Exercise 2
#Serialize a Binary Tree 
     
class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         

def serialize_tree(root):
    """
    Serializes a tree from top to bottom, left to right to a list of values

    Parameters
    ----------
    root_node : root node of a binary tree
        The tree is not ordered or balanced, it's just a binary tree
        Example:
            1
           / \
          2   3
         / \ / \
           4 2
      
    Returns
    -------
    serial_tree :  A list of serialized values
        Example: [1,2,3,None,4,2,None]

    """
    result = []
    current_nodes = [root]
    level_not_empty = True

    while level_not_empty:
        level_not_empty = False
        next_nodes = []

        for node in current_nodes:
            if node == None:
                result.append(None)
                next_nodes.append(None)
                next_nodes.append(None)
            else:
                result.append(node.val)

                left_child = (node.left)
                right_child = (node.right)

                if left_child != None:
                    level_not_empty = True
                if right_child != None:
                    level_not_empty = True

                next_nodes.append(left_child)
                next_nodes.append(right_child)

        current_nodes = next_nodes

    while result and result[-1] == None:
        result.pop()
    return result

    
def deserialize_tree(values):
    """Build a tree from a list and return its root."""
    if not values:
        return None

    nodes = [None for _ in values]
    if values[0] == None:
        raise ValueError('Node missing at index 0')

    root = Node(values[0])
    nodes[0] = root

    index = 1
    while index < len(values):
        value = values[index]
        if value != None:
            parent_index = int((index + 1) / 2) - 1
            parent_node = nodes[parent_index]
            if parent_node == None:
                raise ValueError(
                    'Node missing at index {}'
                    .format(parent_index)
                )
            child_node = Node(value)
            if index % 2:  # is odd
                parent_node.left= child_node
            else:
                parent_node.right = child_node
            nodes[index] = child_node
        index += 1

    return root
    
if __name__ == '__main__':
    l =[2,[[3,[4,6]], 5]]
    l = flatten_list(l)
    print(list(l))
    
    lis =[1,2,3,None,4,2,None]
    print(serialize_tree(deserialize_tree(lis)))
    
    