# CHOP
CHOP Data Exercise
# D3b Data Engineer Exercises

There are two sections, the first is composed of straight coding exercises and the second are exercises based on a provided SQLite database. Each section shouldn’t take more than about an hour, but we provide 24 hours so that you have time to provide code that you’re happy with. You can email your solution or provide a pointer to it hosted somewhere like GitHub/GitLab.

## Coding Section

Write a solution for the functions/classes described below, please consider:

  - Efficiency in both space and time
  - Edge cases and error handling
  - Tests

We prefer you to use python. You can use other languages, but please explain why. 

### Coding Exercise 1: Flatten Nested List

```python
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
```

### Coding Exercise 2: Serialize a Binary Tree


```python
class Node:
    """
    Each node has an integer value, and optionally has left and right children
    """
    pass
    
def serialize_tree(root_node):
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
```

## Data Section

This section consists of short exercises in analysis of a relational health-related database in SQLite, downloadable from here: https://www.dropbox.com/s/mgu1s93kpjsoyhh/openmrs.db?dl=0

This database is a processed version of the public data set for a specific instance of a query tool. The original open MRS data model can be found here: https://wiki.openmrs.org/display/docs/Data+Model. The solutions should be done on the data in SQLite database provided. You can convert it to a database flavor of your choice, but again, explain your choice. 

Key tables include:
- patient
- encounter
- encounter_diagnosis
- lab_result
- diagnosis

Please provide both the data result as well as any code that was run to obtain the result. 

### Data Exercise 1

Provide a list of male patients in the database and the counts of patients by gender.

### Data Exercise 2

Count patients in database diagnosed with DERMITITIS at an encounter.

### Data Exercise 3

Provide a list patients, by MRN, who have had a CD4 count of less than 300.

### Data Exercise 4

Count all female patients above the age of 30 in the database as of today’s date

### Bonus Data Exercise

Describe any potential concerns with either the data itself or the design of the database.
1. For Data Exercise 2 , 'DERMATITIS' is cosidered instead of 'DERMITITIS'
